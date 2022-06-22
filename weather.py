import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import csv
import numpy as np

df = pd.read_csv (r'data.csv')

#df.dtypes
#pd.to_datetime(df['Date'])
#df['Date'] = pd.to_datetime(df['Date'])
#df.plot(x="Date",y="Avg", kind="scatter")

Names = []
Values = []
  
with open('data.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        Names.append(row[2])
        Values.append(row[3])
  
plt.scatter(Names, Values, color = 'g',s = 1)
plt.xticks(rotation = 30)

plt.title('Average Temps 2022', fontsize = 20)
  
plt.show()