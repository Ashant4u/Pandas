####################################

#Pandas Exporting  Data with Pandas


#####################################

import pandas as pd

import numpy as np

my_df = pd.DataFrame({"A" : [1,2,3],
                      "B" : ["one",np.nan,"three"]})

my_df.to_csv("tester_csv.csv")

my_df.to_csv("tester_csv.csv", index= False) #with no index

my_df.to_csv("tester_csv.csv", index= False, columns= ["B"]) #with column

my_df.to_csv("tester_csv.csv", index= False,header=False) #with no header

my_df.to_csv("tester_csv.csv", index= False,na_rep="missing") #filling NA values

my_df.to_csv("tester_csv.txt", index= False,na_rep="missing") #To txt  

my_df.to_excel("tester_csv.xlsx", sheet_name="sheet1") #To excel 

my_other_df = my_df * 3

with pd.ExcelWriter("tester_csv.xlsx") as excel_writer:
    my_df.to_excel(excel_writer, sheet_name="sheet1", index=False)
    my_other_df.to_excel(excel_writer, sheet_name="sheet12",index=False)
    
    
my_df.to_csv("C:\\Users\prash\\Desktop\\tester_csv.csv", index=False)