import mysql.connector
from datetime import date, timedelta

def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gudang_data"
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

def create_store_dimension_table():
    mydb = connect_to_database()

    if mydb:
        mycursor = mydb.cursor()

        create_table_query = """
        CREATE TABLE store_dimension (
            store_key INT PRIMARY KEY,
            store_number INT,
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

def get_holiday_dates():
    holiday_dates = ['2023-01-01', '2023-12-25', '2023-07-04']
    return holiday_dates

def insert_date_data():
    mydb = connect_to_database()
    
    if mydb:
        mycursor = mydb.cursor()
        
        # Tanggal awal (1 Januari 2023)
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

            # Menentukan kuartal
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

            if current_date.strftime('%Y-%m-%d') in holiday_dates:
                holiday_indicator = 'Holiday'
            else:
                holiday_indicator = 'Non-Holiday'

            insert_query = """
            INSERT INTO date_dimension (date_key, date, full_date_desc, day_of_week, calendar_month, calendar_quarter, calendar_year, fiscal_year_month, holiday_indicator, weekday_indicator)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (date_key, date_str, full_date_desc, day_of_week, calendar_month, calendar_quarter, calendar_year, fiscal_year_month, holiday_indicator, weekday_indicator)

            mycursor.execute(insert_query, data)

        mydb.commit()
        print("Data tanggal telah berhasil disisipkan.")

        mycursor.close()
        mydb.close()

def init_main():
    # create_date_dimension_table()
    create_store_dimension_table()
    # insert_date_data()

if __name__ == "__main__":
    init_main()