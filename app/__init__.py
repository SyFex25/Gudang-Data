import base64
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect, url_for
from models import db, DateDimension, ProductDimension, StoreDimension, CashierDimension, PromotionDimension, PaymentMethodDimension, TravellerShopperDimension, RetailSalesFact

app = Flask(__name__)

from import_data import scheduler

app.secret_key = 'Gudang_Data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/testing_gd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# migrate = Migrate(app, db)

@app.route('/')
def display_chart():
    store_dimension = StoreDimension.query.all()
    product_dimension = ProductDimension.query.all()
    return render_template('index.html', store_dimension=store_dimension, product_dimension=product_dimension)

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

@app.route('/gross_margin')
def gross_margin():
    store_key = "2123"
    date_key = "2023-11-02"
    product_key = "1035453804963260181506960"

    query = RetailSalesFact.query.filter(
        RetailSalesFact.store_key == store_key,
        RetailSalesFact.date_key == date_key,
        RetailSalesFact.product_key == product_key
    )

    results = query.with_entities(RetailSalesFact.extended_sales_dollar_amount, RetailSalesFact.extended_cost_dollar_amount).all()

    total_sales = sum(result[0] for result in results)
    total_cost = sum(result[1] for result in results)
    
    gross_margin = total_sales - total_cost

    return f"Gross Margin for Store {store_key}, Date {date_key}, Product {product_key}: ${gross_margin:.2f}"