from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class DateDimension(db.Model):
    __tablename__ = 'date_dimension'
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
    __tablename__ = 'product_dimension'
    product_key = db.Column(db.String(5), primary_key=True, unique=True)
    SKU_number = db.Column(db.String(8))
    product_description = db.Column(db.String(255))
    brand_description = db.Column(db.String(255))
    category_description = db.Column(db.String(255))
    price = db.Column(db.Float)
    cost = db.Column(db.Float)
    def __repr__(self):
        return f'<ProductDimension product_key={self.product_key}>'

class StoreDimension(db.Model):
    __tablename__ = 'store_dimension'
    store_key = db.Column(db.String(5), primary_key=True)
    store_number = db.Column(db.String(3))
    store_name = db.Column(db.String(255))
    store_district = db.Column(db.String(255))
    store_region = db.Column(db.String(255))
    def __repr__(self):
        return f'<StoreDimension store_key={self.store_key}>'

class CashierDimension(db.Model):
    __tablename__ = 'cashier_dimension'
    cashier_key = db.Column(db.String(10), primary_key=True)
    cashier_employee_id = db.Column(db.String(10))
    cashier_name = db.Column(db.String(255))

class PromotionDimension(db.Model):
    __tablename__ = 'promotion_dimension'
    promotion_key = db.Column(db.String(5), primary_key=True)
    promotion_code = db.Column(db.String(25))
    promotion_name = db.Column(db.String(25))
    promotion_media_type = db.Column(db.String(25))
    promotion_begin_date = db.Column(db.Date)
    promotion_end_date = db.Column(db.Date)
    promotion_percentage = db.Column(db.Float)
    def __repr__(self):
        return f'<PromotionDimension promotion_key={self.promotion_key}>'

class PaymentMethodDimension(db.Model):
    __tablename__ = 'payment_method_dimension'
    payment_method_key = db.Column(db.String(5), primary_key=True)
    payment_method_description = db.Column(db.String(255))
    payment_method_group = db.Column(db.String(25))

class TravellerShopperDimension(db.Model):
    __tablename__ = 'traveller_shopper_dimension'
    traveller_id = db.Column(db.String(10), primary_key=True)
    traveller_type = db.Column(db.String(25))

class RetailSalesFact(db.Model):
    __tablename__ = 'retail_sales_facts'
    retail_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_key = db.Column(db.Integer, db.ForeignKey('date_dimension.date_key'))
    product_key = db.Column(db.String(5), db.ForeignKey('product_dimension.product_key'))
    store_key = db.Column(db.String(5), db.ForeignKey('store_dimension.store_key'))
    promotion_key = db.Column(db.String(5), db.ForeignKey('promotion_dimension.promotion_key'))
    cashier_key = db.Column(db.String(10), db.ForeignKey('cashier_dimension.cashier_key'))
    payment_method_key = db.Column(db.String(50), db.ForeignKey('payment_method_dimension.payment_method_key'))
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