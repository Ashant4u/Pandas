#############################

#Understanding our Data


#########################################


import pandas as pd


transactions = pd.read_excel("grocery_database.xlsx",sheet_name= "transactions")

transactions.shape

transactions.head() #By default 5 

transactions.tail(10) #Last 10 transactions

transactions.sample() # 1 randomly selected Sample by default else give count

sample = transactions.sample(frac = 0.1) # Selecting fraction from overall data set



transactions.describe()

transactions.nlargest(25,"sales_cost") # Give largest 25 entries from sales_cost column

transactions.nsmallest(25,"sales_cost") # Give smallest 25 entries from sales_cost column

transactions.nunique() #Get unique values from data 

customer_details = pd.read_excel("grocery_database.xlsx",sheet_name= "customer_details")

customer_details.isna() #Get null vaules
customer_details.isnull()

customer_details.isna().sum()
