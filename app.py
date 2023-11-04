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
    cost = db.Column(db.Integer())

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

class RetailSalesFact(db.Model):
    __tablename__ = 'retail_sales_facts'
    date_key = db.Column(db.Date, primary_key=True)
    product_key = db.Column(db.String(10), primary_key=True)
    store_key = db.Column(db.String(5), primary_key=True)
    promotion_key = db.Column(db.String(255))
    cashier_key = db.Column(db.String(255))
    payment_method_key = db.Column(db.String(255))
    pos_transaction = db.Column(db.String(255))
    sales_quantity = db.Column(db.Integer)
    regular_unit_price = db.Column(db.Numeric(10, 2))
    discount_unit_price = db.Column(db.Numeric(10, 2))
    net_unit_price = db.Column(db.Numeric(10, 2))
    extended_discount_dollar_amount = db.Column(db.Numeric(10, 2))
    extended_sales_dollar_amount = db.Column(db.Numeric(10, 2))
    extended_cost_dollar_amount = db.Column(db.Numeric(10, 2))
    extended_gross_profit_dollar_amount = db.Column(db.Numeric(10, 2))

    def __init__(self, date_key, product_key, store_key, promotion_key, cashier_key, payment_method_key, pos_transaction, sales_quantity, regular_unit_price, discount_unit_price, net_unit_price, extended_discount_dollar_amount, extended_sales_dollar_amount, extended_cost_dollar_amount, extended_gross_profit_dollar_amount):
        self.date_key = date_key
        self.product_key = product_key
        self.store_key = store_key
        self.promotion_key = promotion_key
        self.cashier_key = cashier_key
        self.payment_method_key = payment_method_key
        self.pos_transaction = pos_transaction
        self.sales_quantity = sales_quantity
        self.regular_unit_price = regular_unit_price
        self.discount_unit_price = discount_unit_price
        self.net_unit_price = net_unit_price
        self.extended_discount_dollar_amount = extended_discount_dollar_amount
        self.extended_sales_dollar_amount = extended_sales_dollar_amount
        self.extended_cost_dollar_amount = extended_cost_dollar_amount
        self.extended_gross_profit_dollar_amount = extended_gross_profit_dollar_amount


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

@app.route('/query_gross_profit')
def query_gross_profit():
    results = RetailSalesFact.query.filter(
    RetailSalesFact.store_key == "2123",
    RetailSalesFact.date_key == "2023-11-02",
    RetailSalesFact.product_key == "1035453804963260181506960"
    ).with_entities(RetailSalesFact.extended_gross_profit_dollar_amount).all()
    for a in results:
        print(a[0])

    return "Done"

@app.route('/gross_margin')
def gross_margin():
    # Replace the hardcoded values with actual values or request parameters
    store_key = "2123"  # Replace with the store key you want to query
    date_key = "2023-11-02"  # Replace with the date key you want to query
    product_key = "1035453804963260181506960"  # Replace with the product key you want to query

    # Filter the data for the specified store, date, and product
    query = RetailSalesFact.query.filter(
        RetailSalesFact.store_key == store_key,
        RetailSalesFact.date_key == date_key,
        RetailSalesFact.product_key == product_key
    )

    # Calculate the total sales and total cost for the filtered data
    results = query.with_entities(RetailSalesFact.extended_sales_dollar_amount, RetailSalesFact.extended_cost_dollar_amount).all()

    total_sales = sum(result[0] for result in results)
    total_cost = sum(result[1] for result in results)

    # Calculate the gross margin
    gross_margin = total_sales - total_cost

    return f"Gross Margin for Store {store_key}, Date {date_key}, Product {product_key}: ${gross_margin:.2f}"


@app.route('/sales_dollar_amount')
def sales_dollar_amount():
    results = RetailSalesFact.query.filter(
    RetailSalesFact.store_key == "2123",
    RetailSalesFact.date_key == "date_key",
    RetailSalesFact.product_key == "product_key"
    ).with_entities(RetailSalesFact.extended_sales_dollar_amount).all()
    for a in results:
        print(a[0])

    return "Done"

def generate_unique_cashier_key():
    unique_code = str(uuid.uuid4().int)[:3]
    cashier_key = f"CASHIER{unique_code}"
    return cashier_key

def generate_unique_key():
    return str(uuid.uuid4())

def get_holiday_dates():
    holiday_dates = ['2023-01-01', '2023-03-25', '2023-12-25', '2023-07-04', '2023-19-04', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23', '2023-04-24', '2023-04-25']
    return holiday_dates

if __name__ == '__main__':
    app.run(debug=True)