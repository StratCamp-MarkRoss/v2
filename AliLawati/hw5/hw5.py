# 1: Numpy
# 1- Create a NumPy array containing the numbers from 1 to 10. Multiply every element of this array by 5, 
# and then subtract 2 from each element of the resulting array. Print the final array.
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print((arr*5)-2)

# 2- Given the array [8, 20, 22, 20, 10, 20, 22, 8], calculate and print the mean, median, and mode of the array. 
# For simplicity, assume that there's only one mode.

x_array=np.array([8, 20, 22, 20, 10, 20, 22, 8])
print(x_array.mean())

# 3- Create a 3x3 NumPy array representing the following matrix:
# 1 2 3
# 4 5 6
# 7 8 9
# Extract and print the second row, and then extract and print the middle column

import numpy as np
matrix=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
second_matrix=matrix[1]
print(second_matrix)

middle_column=matrix[:,1]
print(middle_column)

#################################################################################
# 2: Pandas

# The DataFrame class in Pandas is used to create DataFrame objects, 
# which are two-dimensional labeled data structures with columns of potentially different types.
# its not a function or varibale.


#1- Enhance You have been provided with data regarding the assets of a portfolio. 
#Create a Pandas DataFrame called df_assets with the following data and then extract only the 'Market Value' column to review the values of the assets.

#data = {

 #'Asset': ['Bonds', 'Stocks', 'Real Estate', 'Commodities'],

 #'Quantity': [120, 80, 50, 70],

#'Market Value': [1200.00, 2400.50, 3000.00, 950.00]  }# Values in USD
import pandas as pd
data = {
    'Asset': ['Bonds', 'Stocks', 'Real Estate', 'Commodities'],
    'Quantity': [120, 80, 50, 70],
    'Market Value': [1200.00, 2400.50, 3000.00, 950.00]  # Values in USD
}

#Create DataFrame from the provided data
df_assets = pd.DataFrame(data)

# Extract and print the 'Market Value' column
market_value_column = df_assets['Market Value']
print("Market Value Column:")
print(market_value_column)
# Convert the Series to a list
marketvalue_row = market_value_column.tolist()  
print(marketvalue_row)


# 2. Using the df_assets DataFrame, write a command to create a new Series that holds the product of 
# 'Quantity' and 'Market Value' for each asset, representing the total market value of each asset type.

total_mv=df_assets['Market Value'] *df_assets['Quantity']
print(total_mv)


#Hint: A series is not a dataframe


 # 3. From the df_assets DataFrame, write a Pandas command to select only those assets whose 'Market Value' is greater than 1000 USD.
selected_assets=df_assets[df_assets['Market Value']>1000]
print(selected_assets)

 # 4. Assume that the market value of 'Commodities' in df_assets has changed to 1025.00 USD. Write the command to update this in the DataFrame and then display the updated DataFrame.
df_assets.loc[df_assets['Asset']=='Commodities','Market Value']=1025
print(df_assets)
 # 5. The investment manager wants to review the assets ordered by the total market value 
# (from the highest to the lowest). 
# Write a Pandas command to sort the df_assets DataFrame by the total market value, 
# which is a product of 'Quantity' and 'Market Value'.
# create a column & calxualte the market value
df_assets['Total_MV']=df_assets['Market Value'] *df_assets['Quantity']
# sort the new column on descending basis
sorted_df=df_assets.sort_values(by='Total_MV', ascending=False)
# pop it up
print(sorted_df)

###########################################################################################

# 3: Time Series Analysis
# 1. Load the ts_data.csv file into a DataFrame called df_stocks. Parse the 'DATE' column as a DateTime object and 
# set it as the index of the DataFrame. Display the first 5 rows of the DataFrame to 
# confirm that the dates are correctly parsed and indexed.

# Load the CSV file into a DataFrame
df_stocks= pd.read_csv('C:\\Users\\user\\Desktop\\Career\\Programming\\StratCamp\\Python\\Applied Python in Finance Part 1\\ts_data.csv')
# Parse the 'DATE' column as a DateTime object
df_stocks['Date']=pd.to_datetime(df_stocks['Date'])
# Set the 'DATE' column as the index of the DataFrame
df_stocks.set_index('Date',inplace=True)
print(df_stocks.head())


# 2. Calculate the 7-day simple moving average (SMA) for the 'AAPL' stock prices. 
# Add this as a new column named 'AAPL_7day_SMA' to the df_stocks DataFrame. 
# Display the DataFrame to verify that the new column has been added correctly.

df_stocks['AAPL_7_AVG']=df_stocks['AAPL'].rolling(window=7).mean()
print(df_stocks.head())

# 3. The maximum drawdown is a measure of the largest single drop from peak to bottom in the value of a portfolio or stock, 
# without considering the time frame. 
# For the 'TSLA' stock, calculate and print the maximum drawdown in the given date range.

import pandas as pd

df_stocks= pd.read_csv('C:\\Users\\user\\Desktop\\Career\\Programming\\StratCamp\\Python\\Applied Python in Finance Part 1\\ts_data.csv')
# Filter the DataFrame for the desired date range and 'TSLA' stock
tsla_data = df_stocks.loc['start_date':'end_date', 'TSLA']


# Check for missing values
if tsla_data.isna().any():
    print("Missing values detected in the 'TSLA' stock data.")
else:
    # Find the peak and trough prices
    peak_price = tsla_data.max()
    trough_price = tsla_data.min()

    # Calculate the drop
    drop = peak_price - trough_price

    # Calculate the maximum drawdown as a percentage
    max_drawdown_percentage = (drop / peak_price) * 100

    # Print the maximum drawdown
    print("Maximum Drawdown for TSLA stock:", max_drawdown_percentage, "%")

