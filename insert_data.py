from app import app, db, insert_cashier_data, insert_store_data
from app import CashierDimension  # Import your model if needed

# This allows you to use the app context in the shell
app.app_context().push()

# Now you can call your function
insert_cashier_data()

if __name__ == '__main__':
    pass