import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import csv
import numpy as np

df = pd.read_csv (r'data.csv')

df.dtypes

pd.to_datetime(df['Date'])

df['Date'] = pd.to_datetime(df['Date'])

df['Date'].dt.month  

df['Date'].dt.year % 10
#df.plot(x="Date",y="Avg", kind="scatter")

print(df.head(20))



# x label to be temps 
# y label to be the month 
# plots to be average max by decade so 6 plots different color 


#df['Date].dt.year%10