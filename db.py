import mysql.connector
import uuid
from datetime import date, timedelta

def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gudang_data",
            autocommit=True
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_date_dimension_table():
    mydb = connect_to_database()
    
    if mydb:
        mycursor = mydb.cursor()

        create_table_query = """
        CREATE TABLE date_dimension (
            date_key INT PRIMARY KEY,
            date DATE,
            full_date_desc VARCHAR(255),
            day_of_week VARCHAR(255),
            calendar_month VARCHAR(255),
            calendar_quarter VARCHAR(255),
            calendar_year INT,
            fiscal_year_month VARCHAR(255),
            holiday_indicator VARCHAR(255),
            weekday_indicator VARCHAR(255)
        );
        """

        try:
            mycursor.execute(create_table_query)
            mydb.commit()
            print("Tabel date_dimension telah berhasil dibuat.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()

def create_product_dimension_table():
    mydb = connect_to_database()
    
    if mydb:
        mycursor = mydb.cursor()

        create_table_query = """
        CREATE TABLE Product_Dimension (
            product_key VARCHAR(10) UNIQUE PRIMARY KEY,
            SKU_number VARCHAR(13),
            product_description VARCHAR(255),
            brand_description VARCHAR(255),
            category_description VARCHAR(255)
        );
        """

        try:
            mycursor.execute(create_table_query)
            mydb.commit()
            print("Tabel Product_Dimension telah berhasil dibuat.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()

def create_store_dimension_table():
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()

        create_table_query = """
        CREATE TABLE store_dimension (
            store_key VARCHAR(5) PRIMARY KEY,
            store_number VARCHAR(3),
            store_name VARCHAR(255),
            store_district VARCHAR(255),
            store_region VARCHAR(255)
        );
        """

        try:
            mycursor.execute(create_table_query)
            mydb.commit()
            print("Tabel store_dimension telah berhasil dibuat.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()

def create_cashier_dimension_table():
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()

        create_table_query = """
        CREATE TABLE cashier_dimension (
            cashier_key VARCHAR(10) PRIMARY KEY,
            cashier_employee_id VARCHAR(10),
            cashier_name VARCHAR(255)
        );
        """

        try:
            mycursor.execute(create_table_query)
            mydb.commit()
            print("Tabel cashier_dimension telah berhasil dibuat.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()

def create_promotion_dimension_table():
    mydb = connect_to_database()
    
    if mydb:
        mycursor = mydb.cursor()

        create_table_query = """
        CREATE TABLE Promotion_Dimension (
            promotion_key VARCHAR(25) PRIMARY KEY,
            promotion_code VARCHAR(25),
            promotion_name VARCHAR(25),
            promotion_media_type VARCHAR(25),
            promotion_begin_date DATE,
            promotion_end_date DATE
        );
        """

        try:
            mycursor.execute(create_table_query)
            mydb.commit()
            print("Tabel Promotion_Dimension telah berhasil dibuat.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()

def create_payment_method_dimension_table():
    mydb = connect_to_database()
    
    if mydb:
        mycursor = mydb.cursor()

        create_table_query = """
        CREATE TABLE Payment_Method_Dimension (
            payment_method_key VARCHAR(25) PRIMARY KEY,
            payment_method_description VARCHAR(255),
            payment_method_group VARCHAR(25)
        );
        """

        try:
            mycursor.execute(create_table_query)
            mydb.commit()
            print("Tabel Payment_Method_Dimension telah berhasil dibuat.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()

def create_traveller_shopper_dimension_table():
    mydb = connect_to_database()
    
    if mydb:
        mycursor = mydb.cursor()

        create_table_query = """
        CREATE TABLE Traveller_Shopper_Dimension (
            traveller_id VARCHAR(10) PRIMARY KEY,
            traveller_type VARCHAR(25)
        );
        """

        try:
            mycursor.execute(create_table_query)
            mydb.commit()
            print("Tabel Traveller_Shopper_Dimension telah berhasil dibuat.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()

def generate_unique_key():
    return str(uuid.uuid4())

def generate_unique_cashier_key():
    unique_code = str(uuid.uuid4().int)[:3]
    cashier_key = f"CASHIER{unique_code}"
    return cashier_key

def get_holiday_dates():
    holiday_dates = ['2023-01-01', '2023-03-25', '2023-12-25', '2023-07-04', '2023-19-04', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23', '2023-04-24', '2023-04-25']
    return holiday_dates

def insert_cashier_data(cashier_employee_id, cashier_name):
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()

        cashier_key = generate_unique_cashier_key()

        insert_query = """
        INSERT INTO cashier_dimension (cashier_key, cashier_employee_id, cashier_name)
        VALUES (%s, %s, %s)
        """
        data = (cashier_key, cashier_employee_id, cashier_name)

        mycursor.execute(insert_query, data)
        mydb.commit()
        print("Data kasir telah berhasil disisipkan.")

        mycursor.close()
        mydb.close()

def insert_store_data(store_number, store_name, store_district, store_region):
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()

        store_key = generate_unique_key()

        insert_query = """
        INSERT INTO store_dimension (store_key, store_number, store_name, store_district, store_region)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (store_key, store_number, store_name, store_district, store_region)

        mycursor.execute(insert_query, data)
        mydb.commit()
        print("Data toko telah berhasil disisipkan.")

        mycursor.close()
        mydb.close()

def insert_date_data():
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()

        start_date = date(2023, 1, 1)
        holiday_dates = get_holiday_dates()

        for i in range(365):
            current_date = start_date + timedelta(days=i)
            date_key = current_date.strftime('%Y%m%d')
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

            # Periksa apakah data untuk tanggal ini sudah ada dalam tabel
            data_exists_query = f"SELECT COUNT(*) FROM date_dimension WHERE date = '{date_str}';"
            mycursor.execute(data_exists_query)
            data_exists = mycursor.fetchone()

            if data_exists[0] == 0:
                # Jika data belum ada, sisipkan data baru
                insert_query = """
                INSERT INTO date_dimension (date_key, date, full_date_desc, day_of_week, calendar_month, calendar_quarter, calendar_year, fiscal_year_month, holiday_indicator, weekday_indicator)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                data = (date_key, date_str, full_date_desc, day_of_week, calendar_month, calendar_quarter, calendar_year, fiscal_year_month, holiday_indicator, weekday_indicator)

                mycursor.execute(insert_query, data)
            else:
                # Jika data sudah ada, perbarui data tersebut
                update_query = """
                UPDATE date_dimension
                SET date_key = %s, full_date_desc = %s, day_of_week = %s, calendar_month = %s, calendar_quarter = %s, fiscal_year_month = %s, holiday_indicator = %s, weekday_indicator = %s
                WHERE date = %s
                """
                data = (date_key, full_date_desc, day_of_week, calendar_month, calendar_quarter, fiscal_year_month, holiday_indicator, weekday_indicator, date_str)

                mycursor.execute(update_query, data)

        mydb.commit()
        print("Data tanggal telah berhasil disisipkan atau diperbarui.")

        mycursor.close()
        mydb.close()

def insert_store_data(store_key, store_number, store_name, store_district, store_region):
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()

        insert_query = """
        INSERT INTO store_dimension (store_key, store_number, store_name, store_district, store_region)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (store_key, store_number, store_name, store_district, store_region)

        try:
            mycursor.execute(insert_query, data)
            mydb.commit()
            print("Data toko telah berhasil disisipkan.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()

def insert_product_data(product_description, brand_description, category_description):
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()

        # Menghasilkan UUID sebagai product_key
        product_key = int(uuid.uuid4())

        # Menggabungkan SKU dan UUID untuk membuat product_key
        SKU_number = f"SKU-{product_key}"

        insert_query = """
        INSERT INTO Product_Dimension (product_key, SKU_number, product_description, brand_description, category_description)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (product_key, SKU_number, product_description, brand_description, category_description)

        try:
            mycursor.execute(insert_query, data)
            mydb.commit()
            print("Data produk telah berhasil disisipkan.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()

def insert_payment_data(payment_method_description, payment_method_group):
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()
        
        # Menghasilkan UUID sebagai payment_key
        payment_method_key = int(uuid.uuid4())

        insert_query = "INSERT INTO payment_method_dimension (payment_method_key, payment_method_description, payment_method_group) VALUES (%s, %s, %s)"

        data = (payment_method_key, payment_method_description, payment_method_group)
        mycursor.execute(insert_query, data)

        try:
            mycursor.execute(insert_query, data)
            mydb.commit()
            print("Data payment telah berhasil disisipkan.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def insert_promotion_data(promotion_name, promotion_media_type, promotion_begin_date, promotion_end_date):
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()

        # Menghasilkan UUID sebagai promotion_key
        promotion_key = int(uuid.uuid4())

        # Menggabungkan SKU dan UUID untuk membuat promotion_name
        promotion_code = f'P{str(uuid.uuid4())}'

        insert_query = """
        INSERT INTO promotion_dimension (promotion_key, promotion_code, promotion_name, promotion_media_type, promotion_begin_date, promotion_end_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (promotion_key, promotion_code, promotion_name, promotion_media_type, promotion_begin_date, promotion_end_date)

        try:
            mycursor.execute(insert_query, data)
            mydb.commit()
            print("Data produk telah berhasil disisipkan.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

        mycursor.close()
        mydb.close()


def init_main():
    # create_date_dimension_table()
    # create_store_dimension_table()
    # create_cashier_dimension_table()
    # create_payment_method_dimension_table()
    # create_promotion_dimension_table()
    # create_traveller_shopper_dimension_table()
    # insert_date_data()
    # insert_store_data(123, "Indomaret", "Jakarta Pusat", "Jakarta")
    # insert_cashier_data(212100159, "John Doe")
    # insert_product_data("Susu", "Frisian Flag", "Susu Anak")
    # insert_product_data("Susu Cokelat", "Ultramilk", "Susu Anak")
    # insert_payment_data("GoPay", "Digital Wallet")
    insert_promotion_data("Valentine", "Online", '2023-02-13', '2023-07-14')

if __name__ == "__main__":
    init_main()