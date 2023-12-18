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
from datetime import date, timedelta, datetime
from models import *
from sqlalchemy import desc
from flask import jsonify
from sqlalchemy import func
from collections import defaultdict
import uuid


app = Flask(__name__)

# from import_rsf import scheduler

app.secret_key = 'Gudang_Data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/toko'
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
    retail_sales_facts = RetailSalesFact.query.order_by(desc(RetailSalesFact.retail_id)).all()
    return render_template('fact_table.html', retail_sales_facts=retail_sales_facts)

# @app.route('/promotions')
# def display_promotions():
#     promotion_dimension = PromotionDimension.query.all()
#     retail_sales_facts = RetailSalesFact.query.all()
#     product_dimension = ProductDimension.query.all()
#     return render_template('promotions.html', promotion_dimension=promotion_dimension, retail_sales_facts=retail_sales_facts, product_dimension=product_dimension)

@app.route('/promotions')
def display_promotions():
    promotion_dimension = PromotionDimension.query.all()
    products_info = {}

    for promo in promotion_dimension:
        sold_products_query = db.session.query(
            ProductDimension.product_description,
            func.sum(RetailSalesFact.sales_quantity).label('total_sales')
        ).join(RetailSalesFact, RetailSalesFact.product_key == ProductDimension.product_key) \
            .filter(RetailSalesFact.promotion_key == promo.promotion_key) \
            .group_by(ProductDimension.product_description).all()

        sold_products = {product.product_description: product.total_sales or 0 for product in sold_products_query}

        unsold_products_query = db.session.query(
            ProductDimension.product_description,
            func.sum(RetailSalesFact.sales_quantity).label('total_sales')
        ).outerjoin(RetailSalesFact, (RetailSalesFact.product_key == ProductDimension.product_key) & (RetailSalesFact.promotion_key == promo.promotion_key)) \
            .filter(RetailSalesFact.retail_id.is_(None)) \
            .group_by(ProductDimension.product_description).all()

        unsold_products = {product.product_description: product.total_sales or 0 for product in unsold_products_query}

        sold = {}
        unsold = {}

        for product_desc, total_sales in sold_products.items():
            transaction_count = db.session.query(func.count(RetailSalesFact.product_key)) \
                .filter(RetailSalesFact.promotion_key == promo.promotion_key) \
                .filter(RetailSalesFact.product_key == ProductDimension.product_key) \
                .filter(ProductDimension.product_description == product_desc) \
                .scalar()

            if total_sales >= 5 and transaction_count >= 2:
                sold[product_desc] = (total_sales, transaction_count)
            else:
                unsold[product_desc] = (total_sales, transaction_count)

        for product_desc, total_sales in unsold_products.items():
            if product_desc not in sold and total_sales <= 5:
                unsold[product_desc] = (total_sales, 0)

        products_info[promo.promotion_key] = {
            'sold': [f"{product_desc} ({total_sales[0]} item, {total_sales[1]} Transaction)" for product_desc, total_sales in sold.items()],
            'unsold': [f"{product_desc} ({total_sales[0]} item, {total_sales[1]} Transaction)" for product_desc, total_sales in unsold.items()]
        }

    return render_template('promotions.html', products_info=products_info, promotion_dimension=promotion_dimension)


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
        StoreDimension.store_name,
        func.sum(RetailSalesFact.extended_gross_profit_dollar_amount).label('total_profit'),
        func.sum(RetailSalesFact.extended_sales_dollar_amount).label('total_sales')
    ).join(StoreDimension, RetailSalesFact.store_key == StoreDimension.store_key).filter(
        RetailSalesFact.product_key == product_key,
        RetailSalesFact.date_key >= start_date,
        RetailSalesFact.date_key <= end_date
    ).group_by(StoreDimension.store_key, StoreDimension.store_name)

    results = query.all()

    store_keys = [result[0] for result in results]
    store_names = [result[1] for result in results]
    gross_margin_values = [(result[2] / result[3] * 100) if result[3] else 0 for result in results]

    data = {
        "store_keys": store_keys,
        "store_names": store_names,
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
        StoreDimension.store_name, 
        (RetailSalesFact.extended_gross_profit_dollar_amount).label('total_profit')
    ).join(StoreDimension, RetailSalesFact.store_key == StoreDimension.store_key).filter(
        RetailSalesFact.product_key == product_key,
        RetailSalesFact.date_key >= start_date,
        RetailSalesFact.date_key <= end_date
    ).group_by(StoreDimension.store_key, StoreDimension.store_name)

    results = query.all()

    store_names = [result.store_name for result in results] 
    gross_profit_values = [result.total_profit for result in results]

    data = {
        "store_names": store_names,
        "gross_profit_values": gross_profit_values
    }

    return jsonify(data)

@app.route('/snapshot')
def snapshot_simulation():
    retail_inventory_snapshot_facts = RetailInventorySnapshotFacts.query.all()
    historic_retail_inventory_snapshot_fact = HistoricRetailInventorySnapshotFact.query.all()
    return render_template('snapshot.html', retail_inventory_snapshot_facts=retail_inventory_snapshot_facts, historic_retail_inventory_snapshot_fact=historic_retail_inventory_snapshot_fact)

@app.route('/move_snapshot', methods=['POST'])
def move_snapshot():
    if request.method == 'POST':
        # Get current date
        current_date = datetime.now().date()

        # Get all rows from RetailInventorySnapshotFacts
        retail_snapshots = RetailInventorySnapshotFacts.query.all()
        # Get distinct store keys from RetailInventorySnapshotFacts
        distinct_store_keys = db.session.query(RetailInventorySnapshotFacts.store_key).distinct().all()
        unique_store_keys = [key[0] for key in distinct_store_keys]
        # Create a session
        session = db.session

        # Iterate through each snapshot
        for snapshot in retail_snapshots:
            # Get date from DateDimension based on date_key
            date_dimension_entry = DateDimension.query.filter_by(date_key=snapshot.date_key).first()

            if date_dimension_entry:
                # Calculate the difference in days between current date and the snapshot's date
                date_difference = (current_date - date_dimension_entry.date).days

                # Check if the snapshot's date is older than 30 days from the current date
                if date_difference > 1:
                    # Check if the product_key exists in ProductDimension
                    product_dimension_entry = ProductDimension.query.filter_by(product_key=snapshot.product_key).first()
                    
                    if product_dimension_entry:
                        # Calculate average quantity_on_hand for a certain product on a certain day across stores
                        avg_quantity_on_hand = db.session.query(func.sum(RetailInventorySnapshotFacts.quantity_on_hand) / len(unique_store_keys)) \
                            .filter(RetailInventorySnapshotFacts.product_key == snapshot.product_key) \
                            .filter(RetailInventorySnapshotFacts.date_key == snapshot.date_key) \
                            .scalar()

                        if avg_quantity_on_hand is not None:
                            # Insert into HistoricRetailInventorySnapshotFact with average quantity_on_hand
                            historic_snapshot = HistoricRetailInventorySnapshotFact(
                                date_key=snapshot.date_key,
                                product_key=snapshot.product_key,
                                quantity_on_hand=avg_quantity_on_hand
                                # Add other fields as necessary
                            )
                            session.add(historic_snapshot)

                        # Delete the snapshot data from RetailInventorySnapshotFacts
                        session.delete(snapshot)

        # Commit changes after all operations
        session.commit()

        return jsonify({'message': 'Snapshot data moved to historic table as per criteria'}), 200

    else:
        return jsonify({'message': 'Method not allowed'}), 405



@app.route('/inventory')
def inventory_simulation():
    inventory_receipt_accumulating_fact = InventoryReceiptAccumulatingFact.query.all()
    return render_template('inventory.html', inventory_receipt_accumulating_fact = inventory_receipt_accumulating_fact)

@app.route('/snapshot-historic')
def display_snapshot_historic():
    historic_retail_inventory_snapshot_fact = HistoricRetailInventorySnapshotFact.query.all()
    return render_template('snapshot_historic.html', historic_retail_inventory_snapshot_fact = historic_retail_inventory_snapshot_fact)

@app.route('/move_to_retail_snapshot', methods=['POST'])
def move_to_retail_snapshot():
    if request.method == 'POST':
        # Move all data from HistoricRetailInventorySnapshotFact back to RetailInventorySnapshotFacts
        historic_snapshots = HistoricRetailInventorySnapshotFact.query.all()

        for snapshot in historic_snapshots:
            retail_snapshot = RetailInventorySnapshotFacts(
                date_key=snapshot.date_start,
                product_key=snapshot.product_key,
                store_key=snapshot.store_key,
                quantity_on_hand=snapshot.quantity_on_hand
                # Add other fields as necessary
            )
            db.session.add(retail_snapshot)
            db.session.delete(snapshot)  # Delete from Historic table after moving
            db.session.commit()

        return jsonify({'message': 'Data moved back to RetailInventorySnapshotFacts'}), 200
    else:
        return jsonify({'message': 'Method not allowed'}), 405


@app.route('/inventory-simulation')
def display_inventory_simulation():
    return render_template('inventory_simulation.html')

@app.route('/promotion_data')
def promotion_data():
    product_key = request.args.get('product_key')
    promotion_name = request.args.get('promotion_name')

    # Query data sesuai dengan produk, promosi, dan rentang tanggal
    query = db.session.query(
        RetailSalesFact.store_key,
        StoreDimension.store_name,
        func.sum(RetailSalesFact.extended_gross_profit_dollar_amount).label('total_profit')
    ).join(PromotionDimension, RetailSalesFact.promotion_key == PromotionDimension.promotion_key) \
     .join(StoreDimension, RetailSalesFact.store_key == StoreDimension.store_key) \
     .filter(
        RetailSalesFact.product_key == product_key,
        PromotionDimension.promotion_name == promotion_name
    ).group_by(RetailSalesFact.store_key, StoreDimension.store_name)

    results = query.all()

    store_keys = [result[0] for result in results]
    store_names = [result[1] for result in results]
    promotion_values = [result[2] for result in results]

    data = {
        "store_keys": store_keys,
        "store_names": store_names,
        "promotion_values": promotion_values
    }

    return jsonify(data)

@app.route('/semi_additive_data')
def semi_additive():
    pass

def generate_unique_cashier_key():
    unique_code = str(uuid.uuid4().int)[:3]
    cashier_key = f"CASHIER{unique_code}"
    return cashier_key

def generate_unique_key():
    return str(uuid.uuid4())

def get_holiday_dates():
    holiday_dates = ['2023-01-01', '2023-03-25', '2023-12-25', '2023-07-04', '2023-19-04', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23', '2023-04-24', '2023-04-25']
    return holiday_dates

@app.route('/convert_date', methods=['POST'])
def convert_date():
    selected_date = request.json.get('date')
    
    if selected_date:
        date_entry = DateDimension.query.filter_by(date=selected_date).first()

        if date_entry:
            date_key = date_entry.date_key

            # Menentukan nama kolom pada basis data berdasarkan nama kolom pada aplikasi
            column_name = request.json.get('columnName')

            if column_name == 'Date Inspected Key':
                # Masukkan dateKey ke kolom date_inspected_key di tabel inventory_receipt_accumulating_fact
                new_entry = InventoryReceiptAccumulatingFact(date_inspected_key=date_key)
            elif column_name == 'Date Bin Placement Key':
                # Masukkan dateKey ke kolom date_bin_placement_key di tabel inventory_receipt_accumulating_fact
                new_entry = InventoryReceiptAccumulatingFact(date_bin_placement_key=date_key)
            else:
                return jsonify({'error': 'Invalid column name'}), 400

            db.session.add(new_entry)
            db.session.commit()

            return jsonify({'dateKey': date_key, 'success': True})  # Memberikan respons berhasil
        else:
            return jsonify({'error': 'Date not found in DateDimension table'}), 404
    else:
        return jsonify({'error': 'Invalid date parameter'}), 400

@app.route('/get_inventory_data')
def get_inventory_data():
    product_key = request.args.get('product_key')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    store_key = request.args.get('store_key')
   
    # Konversi tanggal dari format "YYYY-MM-DD" ke "YYYYMMDD" integer
    start_date = int(start_date.replace("-", ""))
    end_date = int(end_date.replace("-", ""))
    print(start_date,end_date,product_key,store_key)
    
    query = db.session.query(
        HistoricRetailInventorySnapshotFact.date_key,
        HistoricRetailInventorySnapshotFact.quantity_on_hand
    ).filter(
        HistoricRetailInventorySnapshotFact.product_key == product_key,
        HistoricRetailInventorySnapshotFact.date_key >= start_date,
        HistoricRetailInventorySnapshotFact.date_key <= end_date,
        HistoricRetailInventorySnapshotFact.store_key == store_key
    )

    results = query.all()
    date_keys = [(result[0]) for result in results]
    quantity_on_hand = [result[1] for result in results]
    # print('Gross Profit', gross_profit_values)

    data = {
        "date_keys": date_keys,
        "quantity_on_hand": quantity_on_hand
    }
    # print(data)
    return jsonify(data)

@app.route('/total_sales_data')
def get_total_sales_data():
    product_key = request.args.get('product_key')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    start_date = int(start_date.replace("-", ""))
    end_date = int(end_date.replace("-", ""))
    
    query = db.session.query(
        StoreDimension.store_name,  
        func.sum(RetailSalesFact.extended_sales_dollar_amount).label('total_sales')
    ).join(StoreDimension, RetailSalesFact.store_key == StoreDimension.store_key).filter(
        (RetailSalesFact.product_key == product_key) &
        (RetailSalesFact.date_key >= start_date) &
        (RetailSalesFact.date_key <= end_date)
    ).group_by(StoreDimension.store_name)  

    results = query.all()

    store_names = [result[0] for result in results]
    total_sales_values = [result[1] for result in results]

    data = {
        "store_names": store_names,
        "total_sales_values": total_sales_values
    }

    return jsonify(data)

@app.route('/total_sales_qty_data')
def get_total_sales_qty_data():
    product_key = request.args.get('product_key')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    start_date = int(start_date.replace("-", ""))
    end_date = int(end_date.replace("-", ""))
    
    query = db.session.query(
        StoreDimension.store_name,  
        func.sum(RetailSalesFact.sales_quantity).label('total_sales_qty')
    ).join(StoreDimension, RetailSalesFact.store_key == StoreDimension.store_key).filter(
        (RetailSalesFact.product_key == product_key) &
        (RetailSalesFact.date_key >= start_date) &
        (RetailSalesFact.date_key <= end_date)
    ).group_by(StoreDimension.store_name)  

    results = query.all()

    store_names = [result[0] for result in results]
    total_sales_qty_values = [result[1] for result in results]

    data = {
        "store_names": store_names,
        "total_sales_qty_values": total_sales_qty_values
    }

    return jsonify(data)
