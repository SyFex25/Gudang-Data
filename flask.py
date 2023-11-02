from flask import Flask, request, render_template, make_response, session, redirect
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import date, timedelta

app = Flask(__name__)

app.secret_key = 'Gudang_Data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/gudang_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class DateDimension(db.Model):
    date_key = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    full_date_desc = db.Column(db.String(255))
    day_of_week = db.Column(db.String(255))
    calendar_month = db.Column(db.String(255))
    calendar_quarter = db.Column(db.String(255))
    calendar_year = db.Column(db.Integer)
    fiscal_year_month = db.Column(db.String(255))
    holiday_indicator = db.Column(db.String(255))
    weekday_indicator = db.Column(db.String(255))

class ProductDimension(db.Model):
    product_key = db.Column(db.String(10), primary_key=True, unique=True)
    SKU_number = db.Column(db.String(13))
    product_description = db.Column(db.String(255))
    brand_description = db.Column(db.String(255))
    category_description = db.Column(db.String(255))
    cost = db.Column(db.Integer(11))
    
class StoreDimension(db.Model):
    store_key = db.Column(db.String(5), primary_key=True)
    store_number = db.Column(db.String(3))
    store_name = db.Column(db.String(255))
    store_district = db.Column(db.String(255))
    store_region = db.Column(db.String(255))

class CashierDimension(db.Model):
    cashier_key = db.Column(db.String(10), primary_key=True)
    cashier_employee_id = db.Column(db.String(10))
    cashier_name = db.Column(db.String(255))

class PromotionDimension(db.Model):
    promotion_key = db.Column(db.String(25), primary_key=True)
    promotion_code = db.Column(db.String(25))
    promotion_name = db.Column(db.String(25))
    promotion_media_type = db.Column(db.String(25))
    promotion_begin_date = db.Column(db.Date)
    promotion_end_date = db.Column(db.Date)

class PaymentMethodDimension(db.Model):
    payment_method_key = db.Column(db.String(25), primary_key=True)
    payment_method_description = db.Column(db.String(255))
    payment_method_group = db.Column(db.String(25))

class TravellerShopperDimension(db.Model):
    traveller_id = db.Column(db.String(10), primary_key=True)
    traveller_type = db.Column(db.String(25))

@app.route('/create_date_dimension', methods=['POST'])
def create_date_dimension_table():
    try:
        db.create_all()
        return "Tabel date_dimension telah berhasil dibuat."
    except Exception as e:
        return f"Error: {e}"

@app.route('/create_product_dimension', methods=['POST'])
def create_product_dimension_table():
    try:
        db.create_all()
        return "Tabel Product_Dimension telah berhasil dibuat."
    except Exception as e:
        return f"Error: {e}"

@app.route('/create_store_dimension', methods=['POST'])
def create_store_dimension_table():
    try:
        db.create_all()
        return "Tabel store_dimension telah berhasil dibuat."
    except Exception as e:
        return f"Error: {e}"

@app.route('/create_cashier_dimension', methods=['POST'])
def create_cashier_dimension_table():
    try:
        db.create_all()
        return "Tabel cashier_dimension telah berhasil dibuat."
    except Exception as e:
        return f"Error: {e}"

@app.route('/create_promotion_dimension', methods=['POST'])
def create_promotion_dimension_table():
    try:
        db.create_all()
        return "Tabel Promotion_Dimension telah berhasil dibuat."
    except Exception as e:
        return f"Error: {e}"

@app.route('/create_payment_method_dimension', methods=['POST'])
def create_payment_method_dimension_table():
    try:
        db.create_all()
        return "Tabel Payment_Method_Dimension telah berhasil dibuat."
    except Exception as e:
        return f"Error: {e}"

@app.route('/create_traveller_shopper_dimension', methods=['POST'])
def create_traveller_shopper_dimension_table():
    try:
        db.create_all()
        return "Tabel Traveller_Shopper_Dimension telah berhasil dibuat."
    except Exception as e:
        return f"Error: {e}"

@app.route('/insert_cashier_data', methods=['POST'])
def insert_cashier_data():
    try:
        data = request.get_json()
        cashier_employee_id = data['cashier_employee_id']
        cashier_name = data['cashier_name']

        cashier_key = generate_unique_cashier_key()

        new_cashier = CashierDimension(
            cashier_key=cashier_key,
            cashier_employee_id=cashier_employee_id,
            cashier_name=cashier_name
        )

        db.session.add(new_cashier)
        db.session.commit()
        return "Data kasir telah berhasil disisipkan."
    except Exception as e:
        return f"Error: {e}"

@app.route('/insert_store_data', methods=['POST'])
def insert_store_data():
    try:
        data = request.get_json()
        store_number = data['store_number']
        store_name = data['store_name']
        store_district = data['store_district']
        store_region = data['store_region']

        store_key = generate_unique_key()

        new_store = StoreDimension(
            store_key=store_key,
            store_number=store_number,
            store_name=store_name,
            store_district=store_district,
            store_region=store_region
        )

        db.session.add(new_store)
        db.session.commit()
        return "Data toko telah berhasil disisipkan."
    except Exception as e:
        return f"Error: {e}"

@app.route('/insert_date_data', methods=['POST'])
def insert_date_data():
    try:
        start_date = date(2023, 1, 1)
        holiday_dates = get_holiday_dates()

        for i in range(365):
            current_date = start_date + timedelta(days=i)
            date_key = int(current_date.strftime('%Y%m%d'))
            date_str = current_date.strftime('%Y-%m-%d')
            full_date_desc = current_date.strftime('%B %d, %Y')
            day_of_week = current_date.strftime('%A')
            calendar_month = current_date.strftime('%B')
            calendar_year = current_date.year
            fiscal_year_month = f'F{current_date.strftime("%Y-%m")}'

            if 1 <= current_date.month <= 3:
                calendar_quarter = 'Q1'
            elif 4 <= current_date.month <= 6:
                calendar_quarter = 'Q2'
            elif 7 <= current_date.month <= 9:
                calendar_quarter = 'Q3'
            else:
                calendar_quarter = 'Q4'

            if day_of_week in ['Saturday', 'Sunday']:
                weekday_indicator = 'Weekend'
            else:
                weekday_indicator = 'Weekday'

            if date_str in holiday_dates:
                holiday_indicator = 'Holiday'
            else:
                holiday_indicator = 'Non-Holiday'

            existing_date = DateDimension.query.filter_by(date=date_str).first()

            if existing_date:
                existing_date.date_key = date_key
                existing_date.full_date_desc = full_date_desc
                existing_date.day_of_week = day_of_week
                existing_date.calendar_month = calendar_month
                existing_date.calendar_quarter = calendar_quarter
                existing_date.calendar_year = calendar_year
                existing_date.fiscal_year_month = fiscal_year_month
                existing_date.holiday_indicator = holiday_indicator
                existing_date.weekday_indicator = weekday_indicator
            else:
                new_date = DateDimension(
                    date_key=date_key,
                    date=date_str,
                    full_date_desc=full_date_desc,
                    day_of_week=day_of_week,
                    calendar_month=calendar_month,
                    calendar_quarter=calendar_quarter,
                    calendar_year=calendar_year,
                    fiscal_year_month=fiscal_year_month,
                    holiday_indicator=holiday_indicator,
                    weekday_indicator=weekday_indicator
                )

                db.session.add(new_date)

        db.session.commit()
        return "Data tanggal telah berhasil disisipkan atau diperbarui."
    except Exception as e:
        return f"Error: {e}"

def generate_unique_cashier_key():
    unique_code = str(uuid.uuid4().int)[:3]
    cashier_key = f"CASHIER{unique_code}"
    return cashier_key

def generate_unique_key():
    return str(uuid.uuid4())

def get_holiday_dates():
    holiday_dates = ['2023-01-01', '2023-03-25', '2023-12-25', '2023-07-04', '2023-19-04', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23', '2023-04-24', '2023-04-25']
    return holiday_dates

@app.route('/query_gross_profit')
def query_gross_profit():
    pass







if __name__ == '__main__':
    app.run(debug=True)