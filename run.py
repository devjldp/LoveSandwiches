import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love sandwiches')

'''CHECKING api IS WORKING
sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)

'''

# Defining function to input data

def get_sales_data():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by comma. The loop repeatedly request data, until is valid.    
    """
    while True:
        print("Please enter sales data form alst market")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(',')
        if validate_data(sales_data):
            print("Data is valid!")
            break
    return sales_data


# Defining function to validate data
def validate_data(values):
    """
    Inside the try converts all string values into integers.
    Raise ValueError if strings cannot be converted into int, or if there aren't excatly 6 values
    parameters:
        values: data to be validated.
    """
    try:
        if len(values) != 6:
            [int(value) for value in values]
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False
    
    return True

def update_sales_worksheet(data):
    """
    Update sales worksheet, and new row with the list data provided.
    """
    print("Updating sales worksheet... \n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated succesfully.\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure substracted from the stock:
    - Positive surplus indicates waste.
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet(stock).get_all_values()
    stock_row = stock[-1]


def main():
    """
    Run all program functions
    """
    data = get_sales_data()
# transform element in list into integer
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)

print("Welcome to Love Sandwiches Data Automation")
main()