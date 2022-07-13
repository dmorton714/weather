from ast import Str
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import csv
import numpy as np

filename = 'data.csv'
with open('data.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
#print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

#gets high temps 

highs = [ ]
for row in reader: 
    high = int(row[5])
    highs.append(high)

# plot temps 
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c="red")

#formatting
ax.set_title( "highs", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("temo (F)", fontsize=16)
ax.tick_params(axis= 'both', which='major', labelsize=16)

plt.show()







'''
df = pd.read_csv (r'data.csv')

df.dtypes

#df = pd.DataFrame(columns= ['Date','Avg'])


pd.to_datetime(df['Date'])

df['Date'] = pd.to_datetime(df['Date'])

df['Date'].dt.month  

df['Date'].dt.year % 10
#df.plot(x="Date",y="Avg", kind="scatter")



print(df.head(10))

'''

# x label to be temps 
# y label to be the month 
# plots to be average max by decade so 6 plots different color 


#df['Date].dt.year%10