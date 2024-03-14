# 1: Working with Files
# 1. Create a function that accepts a filepath/filename as a string and 
# returns TRUE if the file has more than 1 written characters in it, 
# and FALSE if the file has 1 or less characters written in it

# os module, which provides a way to interact with the operating system.
import os
def has_more_character(file_path):
    try:
        file_size= os.path.getsize(file_path)
        if file_size>1:
            return True
        else:
            return False
    #Handling Exception:
    except FileNotFoundError:
        print(f"file '{file_path}'not found.")
        return False
    #Handling other exceptions
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    

file_path = 'C:\\Users\\user\\Desktop\\Career\\Programming\\StratCamp\\Python\\sample.txt'
result = has_more_character(file_path)
print(f"The file has more than one character: {result}")

# 2. Write a Python script that engages the above function as follows:
#If FALSE is returned, write to that file the words: “This file is quite possibly empty”
#If TRUE is returned, create a new file, in the same folder, and write the following text to the new file: 
#“ This is a new file”.

import os

def is_file_empty(filename):
    return os.path.getsize(filename) == 0

def main():
    filename = input("Enter the filename: ")

    if os.path.exists(filename):
        if is_file_empty(filename):
            with open(filename, 'w') as file:
                file.write("This file is quite possibly empty\n")
            print("Text written to the existing file.")
        else:
            new_filename = os.path.splitext(filename)[0] + "_new.txt"
            with open(new_filename, 'w') as new_file:
                new_file.write("This is a new file\n")
            print("New file created with text.")
    else:
        print("File not found.")

if __name__ == "__main__":
    main()


# 2: Exception Handling

# Enhance the function from 1.1 with exception handling to ensure that the file exists within that filepath, 
# and throw an appropriate error if it does not 
import os

def has_more_character(file_path):
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        file_size = os.path.getsize(file_path)
        if file_size > 1:
            return True
        else:
            return False
    
    except FileNotFoundError as e:
        print(e)
        return False
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    

file_path = 'C:\\Users\\user\\Desktop\\Career\\Programming\\StratCamp\\Python\\sample.txt'
result = has_more_character(file_path)
print(f"The file has more character: {result}")

# 3: Finance Application
# 1. Create a new file in Microsoft Excel. This file should have two columns: 
# Ticker and Close Price. Ticker is the symbol of the stock, and 
#Close Price is the last traded price before the market closed yesterday. 
#Name this file “Stock_Info.CSV”. Note, when you save in Excel click SAVE AS and save it as a CSV file.
# 2.Create a Python function that consumes the file from 3.1, 
#reading line by line and RETURNS the results in a dictionary.
# 3.Loop through the dictionary and print the average stock price to the screen.

# step 1: Step 1: Create a CSV file with stock information:
import csv

def create_csv_file(stock_data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Ticker', 'Close Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for ticker, close_price in stock_data.items():
            writer.writerow({'Ticker': ticker, 'Close Price': close_price})

# Example data (you need to replace this with your actual data)
stock_data = {'AAPL': 150.25, 'MSFT': 290.75, 'GOOGL': 2750.30}

# Create the CSV file
create_csv_file(stock_data, 'Stock_Info.csv')

# Step 2: Create a Python function to read the CSV file and store the data in a dictionary:

def read_csv_file(filename):
    data = {}
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ticker = row['Ticker']
            close_price = float(row['Close Price'])  # Convert to float
            data[ticker] = close_price
    return data

# Read the CSV file and store data in a dictionary
stock_info = read_csv_file('Stock_Info.csv')
print(stock_info)

# Step 3: Calculate the average stock price and print it to the screen:


def calculate_average_stock_price(stock_data):
    total_price = sum(stock_data.values())
    average_price = total_price / len(stock_data)
    return average_price

# Calculate the average stock price
average_price = calculate_average_stock_price(stock_info)
print(f"Average stock price: {average_price}")
