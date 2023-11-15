import csv
import os
from apscheduler.schedulers.background import BackgroundScheduler
from app import app
from models import db, RetailSalesFact, ProductDimension

scheduler = BackgroundScheduler()
scheduler.start()

def import_data_from_csv():
    unprocessed_folder = 'unprocessed_rsf'
    processed_folder = 'processed_rsf'

    with app.app_context():
        # Mengecek apakah folder unprocessed_rsf ada
        if not os.path.exists(unprocessed_folder):
            print(f"Folder '{unprocessed_folder}' not found.")
            return

        # data_to_remove = []

        # # Mengecek file-file di dalam folder unprocessed_rsf
        for filename in os.listdir(unprocessed_folder):
            filepath = os.path.join(unprocessed_folder, filename)

            # Mengecek apakah item adalah file
            if os.path.isfile(filepath):
                with open(filepath, 'r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    header = csv_reader.fieldnames  # Ambil nama kolom dari header

                    for row in csv_reader:
                        retail_sales_fact = RetailSalesFact(
                            date_key=row['date_key'],
                            product_key=row['product_key'],
                            store_key=row['store_key'],
                            promotion_key=row['promotion_key'],
                            cashier_key=row['cashier_key'],
                            payment_method_key=row['payment_method_key'],
                            pos_transaction=row['pos_transaction'],
                            sales_quantity=row['sales_quantity'],
                            regular_unit_price=row['regular_unit_price'],
                            discount_unit_price=row['discount_unit_price'],
                            net_unit_price=row['net_unit_price'],
                            extended_discount_dollar_amount=row['extended_discount_dollar_amount'],
                            extended_sales_dollar_amount=row['extended_sales_dollar_amount'],
                            extended_cost_dollar_amount=row['extended_cost_dollar_amount'],
                            extended_gross_profit_dollar_amount=row['extended_gross_profit_dollar_amount']
                        )
                        db.session.add(retail_sales_fact)

                # Memindahkan file ke dalam folder processed_rsf setelah selesai diolah
                os.rename(filepath, os.path.join(processed_folder, filename))
                print(f"File '{filename}' processed and moved to '{processed_folder}'.")

        db.session.commit()

    return "Data has been imported successfully and moved to Processed RSF"

# Menjadwalkan pekerjaan untuk dijalankan setiap 5 detik
scheduler.add_job(import_data_from_csv, 'interval', seconds=5, id='import_data_job')
