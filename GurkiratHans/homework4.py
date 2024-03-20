#Question 1a
def check_file_size(filepath):
    try:
        # Open the file in read mode
        with open(filepath, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Check if the length of content is greater than 1
            return len(content) > 1
    except FileNotFoundError:
        print("File not found.")
        return False

# Test the function
file_path = input("Enter the filepath: ")
print(check_file_size(file_path))



#Question 1b
def process_file(filepath):
    if not check_file_size(filepath):  # If FALSE is returned
        with open(filepath, 'w') as file:
            file.write("This file is quite possibly empty")
    else:  # If TRUE is returned
        folder_path = '/'.join(filepath.split('/')[:-1])  # Extract folder path
        new_file_path = folder_path + "/new_file.txt"
        with open(new_file_path, 'w') as new_file:
            new_file.write("This is a new file")

# Test the function
file_path = input("Enter the filepath: ")
process_file(file_path)


#Question 2a
def check_file_size(filepath):
    try:
        # Try to open the file in read mode
        with open(filepath, 'r') as file:
            # Read the content of the file
            content = file.read()
            # Check if the length of content is greater than 1
            return len(content) > 1
    except FileNotFoundError:
        print("File not found.")
        return False
    except IsADirectoryError:
        print("The specified path is a directory, not a file.")
        return False
    except PermissionError:
        print("Permission denied to open the file.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Test the function
file_path = input("Enter the filepath: ")
print(check_file_size(file_path))




#Question 3a
import csv

def read_stock_info(file_path):
    stock_info = {}

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                ticker = row['Ticker']
                close_price = row['Close Price']
                stock_info[ticker] = close_price
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return stock_info

# Test the function
file_path = "Stock_Info.csv"
stock_data = read_stock_info(file_path)
print(stock_data)






#Question 3b
def calculate_average_stock_price(stock_info):
    total_price = 0
    num_stocks = 0

    for price in stock_info.values():
        total_price += float(price)
        num_stocks += 1

    if num_stocks > 0:
        average_price = total_price / num_stocks
        print("Average stock price:", average_price)
    else:
        print("No stock data found.")

# Test the function with the stock data dictionary
calculate_average_stock_price(stock_data)