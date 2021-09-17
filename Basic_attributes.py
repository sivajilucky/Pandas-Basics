import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import csv

df=pd.read_csv("E:\\Newdata.csv")
print(df)
print(df.shape)#it is used to give rows and columns
rows,columns=df.shape
print(rows)
print(columns)
print(df.head())#it is used to give some initial rows
print(df.head(3))#it is used to give initial 3 rows
print(df.tail())#it is used to print last five rows
#you can also use indexing and slicing to print rows and columns
print(df[0:2])
#if you want to print columns
print(df.columns)
#if you want to individual column means simply
print(df.name)#it will simply print all names
#if you want to print only some columns means then
print(df[['name','email']])
#you can also find maximum 
print(df['phone_no'].max())
#you can also find statistics of data using describe method
print(df.describe())
#you can also find selected data
print(df[df.phone_no>=703651])
#>>>>>IMP>>> if you want change the index and make index as one of the column name
print(df.set_index('name',inplace=True))
#if you want to reset the index means then simply use reset_index
print(df.reset_index(inplace=True))