import csv
import os
from apscheduler.schedulers.background import BackgroundScheduler
from app import app
from models import db, RetailSalesFact, ProductDimension
scheduler = BackgroundScheduler()
scheduler.start()

def import_data_from_csv():
    with app.app_context():
        with open('data.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            header = csv_reader.fieldnames  # Ambil nama kolom dari header
            data_to_remove=[]
            for row in csv_reader:
                prod_key = row['Product Key']
                quantities = int(row['Sales Quantity'])
                
                addon_data = ProductDimension.query.filter_by(product_key=prod_key).first()

                if addon_data:
                    regular_price = addon_data.price
                    promo_key = addon_data.promotion_key

                    if promo_key == '127197534513120974369078029708692804441':
                        disc_unit_price = 1000
                    elif promo_key == '1293676579042382297136886':
                        disc_unit_price = 500
                    elif promo_key == '33121890113396337783002224795346342625':
                        disc_unit_price = 300
                    elif promo_key == '38737260967774587366681226162111705657':
                        disc_unit_price = 400
                    elif promo_key == '8014075331218306379158866005218795500':
                        disc_unit_price = 200
                    else:
                        disc_unit_price = 200

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
        db.session.commit()
        with open('data.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data_to_remove[1:]) 
            print("Data Removed from CSV:", data_to_remove)  

    return "Data has been imported successfully and removed from CSV"

scheduler.add_job(import_data_from_csv, 'interval', seconds=30, id='import_data_job')
