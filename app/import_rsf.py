import csv
import os
import logging
import time
from apscheduler.schedulers.background import BackgroundScheduler
from app import app
from models import db, RetailSalesFact, ProductDimension, PromotionDimension

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  

scheduler = BackgroundScheduler()
scheduler.start()

# Menyimpan file terakhir yang diproses
last_processed_file = None

def import_data_from_csv():
    global last_processed_file

    unprocessed_folder = 'unprocessed_rsf'
    processed_folder = 'processed_rsf'

    with app.app_context():
        try:
            # Mengecek apakah folder ada unprocessed_rsf 
            if not os.path.exists(unprocessed_folder):
                logger.error(f"Folder '{unprocessed_folder}' not found.")
                return

            # Mengecek file-file di dalam folder unprocessed_rsf
            files_to_process = [f for f in os.listdir(unprocessed_folder) if os.path.isfile(os.path.join(unprocessed_folder, f))]

            # Memeriksa apakah folder unprocessed_rsf kosong
            if not files_to_process:
                logger.info("No files to process in 'unprocessed_rsf'.")
                return
            
            # Memeriksa apakah ada file yang belum diproses
            if last_processed_file is not None and last_processed_file in files_to_process:
                index = files_to_process.index(last_processed_file)
                files_to_process = files_to_process[index+1:]  # Hanya proses file setelah file terakhir yang diproses

            for filename in files_to_process:
                filepath = os.path.join(unprocessed_folder, filename)

                # Mengecek apakah item adalah file
                if os.path.isfile(filepath):
                    logger.info(f"Processing file: '{filename}'")
                    logger.info(f"Last processed file: {last_processed_file}")  # Tambahkan log untuk nama file yang sedang diproses

                    with open(filepath, 'r') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        for row in csv_reader:
                            prod_key = row['Product Key']
                            quantities = int(row['Sales Quantity'])
                            promo_key = row['Promotion Key']

                            addon_data = ProductDimension.query.filter_by(product_key=prod_key).first()

                            if addon_data:
                                regular_price = addon_data.price

                                addon_data_promo = PromotionDimension.query.filter_by(promotion_key=promo_key).first()
                                if addon_data_promo: 
                                    disc_unit_price = regular_price * ((addon_data_promo.promotion_percentage)/100)
                                    net_price = regular_price - disc_unit_price

                                    ext_disc_dollar_amt = quantities * disc_unit_price
                                    ext_sales_dollar_amt = quantities * net_price

                                    unit_cost = addon_data.cost
                                    ext_cost_dollar_amt = quantities * unit_cost

                                    ext_gross_profit_dollar_amount = ext_sales_dollar_amt - ext_cost_dollar_amt

                                    retail_sales_fact = RetailSalesFact(
                                        date_key=row['Date Key'],
                                        product_key=prod_key,
                                        store_key=row['Store Key'],
                                        promotion_key=promo_key,
                                        cashier_key=row['Cashier Key'],
                                        payment_method_key=row['Payment Method Key'],
                                        pos_transaction=row['POS Transaction'],
                                        sales_quantity=quantities,
                                        regular_unit_price=regular_price,
                                        discount_unit_price=disc_unit_price,
                                        net_unit_price=net_price,
                                        extended_discount_dollar_amount=ext_disc_dollar_amt,
                                        extended_sales_dollar_amount=ext_sales_dollar_amt,
                                        extended_cost_dollar_amount=ext_cost_dollar_amt,
                                        extended_gross_profit_dollar_amount=ext_gross_profit_dollar_amount
                                    )
                                    db.session.add(retail_sales_fact)
                                    db.session.commit()  # Commit setiap kali data dimasukkan

                    # Memindahkan file ke dalam folder processed_rsf setelah selesai diolah
                    os.rename(filepath, os.path.join(processed_folder, filename))
                    last_processed_file = filename
                    logger.info(f"File '{filename}' processed and moved to '{processed_folder}'.")
                    
                    # Menunggu jeda waktu sebelum membaca file selanjutnya
                    time.sleep(30)
                    last_processed_file = filename  

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            db.session.rollback()

# Jadwalkan fungsi untuk dijalankan setiap 30 detik
logger.info("Scheduling import_data_from_csv job...")
scheduler.add_job(import_data_from_csv, 'interval', seconds=30, id='import_data_job')
logger.info("Job scheduled successfully.")