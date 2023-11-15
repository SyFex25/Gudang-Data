import base64
import sys
import os
import uuid

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, jsonify
from sqlalchemy import func
from datetime import date, timedelta
from models import *

app = Flask(__name__)

from import_data import scheduler

app.secret_key = 'Gudang_Data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/gudang_data_testing_revised'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def display_chart():
    store_dimension = StoreDimension.query.all()
    product_dimension = ProductDimension.query.all()
    promotion_dimension = PromotionDimension.query.all()
    return render_template('index.html', store_dimension=store_dimension, product_dimension=product_dimension, promotion_dimension=promotion_dimension)

@app.route('/create_all_tables')
def create_date_dimension_table():
    try:
        db.create_all()
        return "Tabel database sudah dibuat."
    except Exception as e:
        return f"Error: {e}"

@app.route('/fact-table')
def display_fact_table():
    retail_sales_facts = RetailSalesFact.query.all()
    return render_template('fact_table.html', retail_sales_facts = retail_sales_facts)

@app.route('/promotions')
def display_promotions():
    promotion_dimension = PromotionDimension.query.all()
    retail_sales_facts = RetailSalesFact.query.all()
    product_dimension = ProductDimension.query.all()
    return render_template('promotions.html', promotion_dimension=promotion_dimension, retail_sales_facts=retail_sales_facts, product_dimension=product_dimension)


@app.route('/insert_date_data')
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

@app.route('/gross_margin_data')
def gross_margin_data():
    product_key = request.args.get('product_key')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Konversi tanggal dari format "YYYY-MM-DD" ke "YYYYMMDD" integer
    start_date = int(start_date.replace("-", ""))
    end_date = int(end_date.replace("-", ""))

    # Query data margin sesuai dengan produk dan rentang tanggal
    query = db.session.query(
        StoreDimension.store_key,
        func.sum(RetailSalesFact.extended_gross_profit_dollar_amount).label('total_profit'),
        func.sum(RetailSalesFact.extended_sales_dollar_amount).label('total_sales')
    ).join(StoreDimension, RetailSalesFact.store_key == StoreDimension.store_key).filter(
        RetailSalesFact.product_key == product_key,
        RetailSalesFact.date_key >= start_date,
        RetailSalesFact.date_key <= end_date
    ).group_by(StoreDimension.store_key)

    results = query.all()

    store_keys = [result[0] for result in results]
    gross_margin_values = [(result[1] / result[2] * 100) if result[2] else 0 for result in results]


    data = {
        "store_keys": store_keys,
        "gross_margin_values": gross_margin_values
    }

    return jsonify(data)

@app.route('/gross_profit_data')
def gross_profit_data():
    product_key = request.args.get('product_key')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
   
    # Konversi tanggal dari format "YYYY-MM-DD" ke "YYYYMMDD" integer
    start_date = int(start_date.replace("-", ""))
    end_date = int(end_date.replace("-", ""))

    query = db.session.query(
        StoreDimension.store_key,
        (RetailSalesFact.extended_gross_profit_dollar_amount).label('total_profit')
    ).join(StoreDimension, RetailSalesFact.store_key == StoreDimension.store_key).filter(
        RetailSalesFact.product_key == product_key,
        RetailSalesFact.date_key >= start_date,
        RetailSalesFact.date_key <= end_date
    ).group_by(StoreDimension.store_key)

    results = query.all()

    store_keys = [result[0] for result in results]
    gross_profit_values = [(result[1]) for result in results]
    print('Gross Profit', gross_profit_values)

    data = {
        "store_keys": store_keys,
        "gross_profit_values": gross_profit_values
    }

    return jsonify(data)


@app.route('/promotion_data')
def promotion_data():
    product_key = request.args.get('product_key')
    promotion_name = request.args.get('promotion_name')

    # Query data margin sesuai dengan produk dan rentang tanggal
    query = db.session.query(
        RetailSalesFact.store_key,
        (RetailSalesFact.extended_gross_profit_dollar_amount).label('total_profit')
    ).join(PromotionDimension, RetailSalesFact.promotion_key == PromotionDimension.promotion_key).filter(
        RetailSalesFact.product_key == product_key, PromotionDimension.promotion_name == promotion_name
    ).group_by(RetailSalesFact.store_key)

    results = query.all()

    store_keys = [result[0] for result in results]
    promotion_values = [(result[1]) for result in results]

    data = {
        "store_keys": store_keys,   
        "promotion_values": promotion_values
    }

    return jsonify(data)

def generate_unique_cashier_key():
    unique_code = str(uuid.uuid4().int)[:3]
    cashier_key = f"CASHIER{unique_code}"
    return cashier_key

def generate_unique_key():
    return str(uuid.uuid4())

def get_holiday_dates():
    holiday_dates = ['2023-01-01', '2023-03-25', '2023-12-25', '2023-07-04', '2023-19-04', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23', '2023-04-24', '2023-04-25']
    return holiday_dates