#############################

#Pandas Joining and Merging Dataframes


#############################


#Joining

import pandas as pd

df_a = pd.DataFrame({"A":[1, 2, 3],"B":[4, 5, 6]})

df_b = pd.DataFrame({"C":[1, 2, 3],"D":[4, 5, 6]})

df_c = pd.concat([df_a,df_b],axis= 1)

df_c = pd.concat([df_a,df_b],axis= 0)

df_a = pd.DataFrame({"A":[1, 2, 3],"B":[4, 5, 6]})

df_b = pd.DataFrame({"A":[1, 2, 3],"B":[4, 5, 6]})

df_c = pd.concat([df_a,df_b],axis= 0)

df_a.append(df_b) #Deprecated

#Merging


df_a = pd.DataFrame({"user_id":[1, 2, 3, 5, 7],"age":[40, 15, 61, 34,50]})

df_b = pd.DataFrame({"user_id":[1, 2, 3, 4, 5],"gender":["m", "f", "f", "m", "f"]})

#Inner Join

df_c = pd.merge(df_a, df_b,how="inner",on ="user_id")


#Left join

df_c = pd.merge(df_a, df_b,how="left",on ="user_id")

#right join
df_c = pd.merge(df_a, df_b,how="right",on ="user_id")

#Outer join

df_c = pd.merge(df_a, df_b,how="outer",on ="user_id")


#Join on multiple columns
df_c = pd.merge(df_a, df_b,how="left",on =["user_id","column2")
                        
df_b.rename(columns = {"user_id":"customer_id"},inplace= True)

df_c = pd.merge(df_a, df_b,how="inner",left_on="user_id",right_on="customer_id")
                                           
                                           
