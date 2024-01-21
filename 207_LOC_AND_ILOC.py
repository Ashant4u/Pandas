#############################

#Pandas LOC and ILOC 


#############################

import pandas as pd

transaction = pd.read_excel("grocery_database.xlsx",sheet_name="transactions")


#transaction.loc[row_label,colum_label]
#transaction.loc[row_index,colum_index]


#ILOC

transaction.iloc[0]
transaction.iloc[0:4] # Slicing rows
transaction.iloc[[0,30,51]] #Fetching specific index

transaction.iloc[0:4,[0,3,-1]]

transaction.iloc[:,[0,3,-1]]

#LOC

transaction.loc[0]
transaction.set_index("customer_id",inplace =True)
transaction.loc[1]

transaction.reset_index(inplace = True)

list(transaction)

transaction.loc[0:10,"customer_id"]

transaction.loc[0:10,["customer_id","product_area_id","sales_cost"]]

transaction.loc[0:10,["product_area_id","sales_cost","customer_id"]]




#Conditional Logic

transaction["customer_id"] == 642


transaction.loc[transaction["customer_id"] == 642]

transaction.loc[transaction["customer_id"] == 642 ,["customer_id","sales_cost"]]


transaction.loc[(transaction["customer_id"] == 642) & (transaction["num_items"] > 5)]

transaction.loc[(transaction["customer_id"] == 642) | (transaction["num_items"] > 5)]

transaction.loc[transaction["customer_id"].isin([642,700])]

transaction.loc[~transaction["customer_id"].isin([642,700])] #Negative of condition