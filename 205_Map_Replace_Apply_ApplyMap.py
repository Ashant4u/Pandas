#############################

#Pandas Adding and Dropping Columns


#########################################

import pandas as pd

customer_details = pd.read_excel("grocery_database.xlsx",sheet_name="customer_details")
product_areas = pd.read_excel("grocery_database.xlsx",sheet_name ="product_areas")

#Map

customer_details["gender_numeric"] = customer_details["gender"].map({"M": 0,
                                                                     "F" : 1})

customer_details["gender_numeric"] = customer_details["gender"].map({"F" : 1}) #If no values pass NAN


customer_details.drop("gender_numberic",axis =1)


#Replace

customer_details["gender_numeric"] = customer_details["gender"].replace({"M": 0,
                                                                     "F" : 1})

customer_details["gender_numeric"] = customer_details["gender"].replace({"M": 0}) #if no values present keep the values
                                                                

#Apply

product_areas["product_area_name"].apply(len)

def update_profit_margin(profit_margin):
    if profit_margin > 0.2:
        return profit_margin * 1.2
    else:
        return profit_margin * 0.8


product_areas["profit_margin_updated"] = product_areas["profit_margin"].apply(update_profit_margin)





x = pd.DataFrame({"A":[1,2],"B":[3,4],"C":[5,6],})

x.apply(max) #Column Wise
x.apply(max, axis =1) #Row Wise

#ApplyMap

def square(n):
    return n **2

x.applymap(square)
