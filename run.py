import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import numpy as np

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

def update_worksheet(data, worksheet):
    """
    Update a worksheet, and new row with the list data provided.
    """
    print(f"Updating sales {worksheet}... \n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"Sales {worksheet} updated succesfully.\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure substracted from the stock:
    - Positive surplus indicates waste.
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]
    print(f"stock row: {stock_row}")
    print(f"sales row: {sales_row}")
    superplus_data = []
    for stock,sale in zip(stock_row,sales_row):
        superplus_data.append(int(stock)-sale)
    return superplus_data

def get_last_5_entries_sales():
    """
    Run all program functions
    """
    sales = SHEET.worksheet("sales")
    # print(sales)
    # column =sales.
    # print(column)
    columns = []
    for index in range(1,7):
        column = sales.col_values(index)
        columns.append(column[-5:])
    return columns

def get_average(data):
    """
    """
    avg = []
    for column in data:
        numbers = [float(number) for number in column]
        avg.append(np.average(numbers))

    print(avg)




def main():
    """
    Run all program functions
    """
    data = get_sales_data()
# transform element in list into integer
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data,'sales')
    new_superplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_superplus_data, 'surplus')
print("Welcome to Love Sandwiches Data Automation")
# main()
sales_columns = get_last_5_entries_sales()
pprint(sales_columns)