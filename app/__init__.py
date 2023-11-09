import base64
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, jsonify
from sqlalchemy import func
from models import db, ProductDimension, StoreDimension,PromotionDimension, RetailSalesFact

app = Flask(__name__)

from import_data import scheduler

app.secret_key = 'Gudang_Data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/gudang_data_testing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def display_chart():
    store_dimension = StoreDimension.query.all()
    product_dimension = ProductDimension.query.all()
    promotion_dimension = PromotionDimension.query.all()
    return render_template('index.html', store_dimension=store_dimension, product_dimension=product_dimension, promotion_dimension=promotion_dimension)

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

    # Membuat daftar store_key dan margin
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