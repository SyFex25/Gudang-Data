import mysql.connector
from random import choice,randint,randrange

def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gudang_data_revised",
            autocommit=True
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    

if __name__ == '__main__':
    mydb = connect_to_database()
    mycursor = mydb.cursor()

    query = """
    select * from product_dimension;
    );
    """
    mycursor.execute(query)
    product = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    query = """
    select * from store_dimension;
    );
    """
    mycursor.execute(query)
    store = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    query = """
    select * from cashier_dimension;
    );
    """
    mycursor.execute(query)
    cashier = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    query = """
    select * from payment_method_dimension;
    );
    """
    mycursor.execute(query)
    payment_method = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    query = """
    select * from date_dimension;
    );
    """
    mycursor.execute(query)
    date = mycursor.fetchall()
    mycursor.close()
    mydb.close()




    # Insert Retail Sales Fact 
    for i in range(15):
        bought_product = choice(product)

        # pilih promo
        # promo = [("12719",20230101),("12936",20230214)]
        #         #  ("33121890113396337783002224795346342625",20230814),("38737260967774587366681226162111705657",20231031),
        #         #  ("8014075331218306379158866005218795500",20230501)]
        # promo_chosen = choice(promo)

        date_key = choice(date)[0]
        # date_key = promo_chosen[1]
        product_key = bought_product[0]
        # product_key = "10354"
        store_key = choice(store)[0]
        promotion_key = "28971"
        # promotion_key = promo_chosen[0]
        cashier_key = choice(cashier)[0]
        payment_method_key = choice(payment_method)[0]
        pos_transaction = "offline"
        sales_quantity = randint(1,10)
        regular_unit_price = bought_product[-2]
        # discount_unit_price = randrange(100,0.1*regular_unit_price)
        discount_unit_price = 0 
        net_unit_price = regular_unit_price - discount_unit_price
        extended_discount_dollar_amount = discount_unit_price * sales_quantity
        extended_sales_dollar_amount = sales_quantity * net_unit_price
        extended_cost_dollar_amount = sales_quantity * bought_product[-1]
        extended_gross_profit_dollar_amount = extended_sales_dollar_amount - extended_cost_dollar_amount
            
        mydb = connect_to_database()
        mycursor = mydb.cursor()
        insert_query = """
        INSERT INTO retail_sales_facts (date_key, product_key, store_key, promotion_key, cashier_key, payment_method_key, pos_transaction, sales_quantity, regular_unit_price, discount_unit_price, net_unit_price, extended_discount_dollar_amount, extended_sales_dollar_amount, extended_cost_dollar_amount, extended_gross_profit_dollar_amount)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (date_key, product_key, store_key, promotion_key, cashier_key, payment_method_key, pos_transaction, sales_quantity, regular_unit_price, discount_unit_price, net_unit_price, extended_discount_dollar_amount, extended_sales_dollar_amount, extended_cost_dollar_amount, extended_gross_profit_dollar_amount)
        mycursor.execute(insert_query, values)
        mydb.commit()
        print("Data berhasil diinsert ke tabel retail_sales_facts.")
        mycursor.close()
        mydb.close()