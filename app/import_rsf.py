import csv
import os
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from app import app
from models import db, RetailSalesFact, ProductDimension, PromotionDimension

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()
scheduler.start()

def import_data_from_csv():
    unprocessed_folder = 'unprocessed_rsf'
    processed_folder = 'processed_rsf'

    with app.app_context():
        with db.session.begin():
            try:
                # Mengecek apakah folder unprocessed_rsf ada
                if not os.path.exists(unprocessed_folder):
                    logger.error(f"Folder '{unprocessed_folder}' not found.")
                    return

                # Mengecek file-file di dalam folder unprocessed_rsf
                for filename in os.listdir(unprocessed_folder):
                    filepath = os.path.join(unprocessed_folder, filename)

                    # Mengecek apakah item adalah file
                    if os.path.isfile(filepath):
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
                        # Memindahkan file ke dalam folder processed_rsf setelah selesai diolah
                        os.rename(filepath, os.path.join(processed_folder, filename))
                        logger.info(f"File '{filename}' processed and moved to '{processed_folder}'.")
            except Exception as e:
                logger.error(f"An error occurred: {e}")
                db.session.rollback()

scheduler.add_job(import_data_from_csv, 'interval', seconds=5, id='import_data_job')
