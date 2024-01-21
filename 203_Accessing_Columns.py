#############################

#Pandas Accessing Columns


#########################################

import pandas as pd

transactions = pd.read_excel("grocery_database.xlsx",sheet_name= "transactions")

"""
select 
   customer_id,
   sales_cost
   
from transactions

"""

##new_df = transactions.customer_id Not to prefer

# Allow only one column at a time
# Column name can be sum count etc 
# dyanmic value cant be assigned

my_var = "customer_id"

new_df = transactions["customer_id"]

transactions[my_var]

new_df = transactions[["customer_id"]]

new_df = transactions[["customer_id","sales_cost"]]