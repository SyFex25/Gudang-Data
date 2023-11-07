import base64
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect, url_for, jsonify
from sqlalchemy import func
from models import db, DateDimension, ProductDimension, StoreDimension, CashierDimension, PromotionDimension, PaymentMethodDimension, TravellerShopperDimension, RetailSalesFact

app = Flask(__name__)

from import_data import scheduler

app.secret_key = 'Gudang_Data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/gudang_data_testing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# migrate = Migrate(app, db)

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

@app.route('/stores')
def display_stores():
    return render_template('stores.html')

@app.route('/cashiers')
def display_cashiers():
    cashier_dimension = CashierDimension.query.all()
    return render_template('cashiers.html', cashier_dimension=cashier_dimension)

@app.route('/products')
def display_products():
    return render_template('products.html')

@app.route('/promotions')
def display_promotions():
    return render_template('promotions.html')

@app.route('/payment-methods')
def display_payment_methods():
    return render_template('payment_methods.html')

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
    print('gross margin', gross_margin_values)

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

    # Query data margin sesuai dengan produk dan rentang tanggal
    query = db.session.query(
        StoreDimension.store_key,
        (RetailSalesFact.extended_gross_profit_dollar_amount).label('total_profit')
    ).join(StoreDimension, RetailSalesFact.store_key == StoreDimension.store_key).filter(
        RetailSalesFact.product_key == product_key,
        RetailSalesFact.date_key >= start_date,
        RetailSalesFact.date_key <= end_date
    ).group_by(StoreDimension.store_key)

    results = query.all()
    # Membuat daftar store_key dan margin
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
        StoreDimension.store_key,
        (RetailSalesFact.extended_gross_profit_dollar_amount).label('total_profit')
    ).join(StoreDimension, RetailSalesFact.store_key == StoreDimension.store_key).filter(
        RetailSalesFact.product_key == product_key,
        RetailSalesFact.date_key >= start_date,
        RetailSalesFact.date_key <= end_date
    ).group_by(StoreDimension.store_key)

    results = query.all()
    # Membuat daftar store_key dan margin
    store_keys = [result[0] for result in results]
    gross_profit_values = [(result[1]) for result in results]
    print('Gross Profit', gross_profit_values)

    data = {
        "store_keys": store_keys,
        "gross_profit_values": gross_profit_values
    }

    return jsonify(data)