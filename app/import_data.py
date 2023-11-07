#untuk memasukkan data ke fact table dari csv setiap 30 detik 
import csv
import os
from apscheduler.schedulers.background import BackgroundScheduler
from app import app
from models import db, RetailSalesFact

scheduler = BackgroundScheduler()
scheduler.start()

def import_data_from_csv():
    with app.app_context():
        data_to_remove = []

        with open('data.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            header = csv_reader.fieldnames  
            data_to_remove.append(header)

            for row in csv_reader:
                retail_sales_fact = RetailSalesFact(
                    date_key=row['Date Key'],
                    product_key=row['Product Key'],
                    store_key=row['Store Key'],
                    promotion_key=row['Promotion Key'],
                    cashier_key=row['Cashier Key'],
                    payment_method_key=row['Payment Method Key'],
                    pos_transaction=row['POS Transaction'],
                    sales_quantity=row['Sales Quantity'],
                    regular_unit_price=row['Regular Unit Price'],
                    discount_unit_price=row['Discount Unit Price'],
                    net_unit_price=row['Net Unit Price'],
                    extended_discount_dollar_amount=row['Extended Discount Dollar Amount'],
                    extended_sales_dollar_amount=row['Extended Sales Dollar Amount'],
                    extended_cost_dollar_amount=row['Extended Cost Dollar Amount'],
                    extended_gross_profit_dollar_amount=row['Extended Gross Profit Dollar Amount']
                )
                db.session.add(retail_sales_fact)

        db.session.commit()

        with open('data.csv', 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data_to_remove[1:]) 

    return "Data has been imported successfully and removed from CSV"

scheduler.add_job(import_data_from_csv, 'interval', seconds=30, id='import_data_job')
