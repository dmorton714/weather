import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import csv
import numpy as np

'''
df = pd.read_csv (r'jan.csv')

filename = 'jan.csv'
with open('jan.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)



#df.dtypes
#pd.to_datetime(df['Date'])
#df['Date'] = pd.to_datetime(df['Date'])

#col_list = ["fifties", "sixties"]
#print(df["fifties"])
#print(df["sixties"])
#avg works!!!!
#date works!!


df2 = df['fifties'].mean()
print(df2)

df2 = df['sixties'].mean()
print(df2)

df2 = df['seventies'].mean()
print(df2)

df2 = df['eighties'].mean()
print(df2)

df2 = df['nineties'].mean()
print(df2)

df2 = df['twok'].mean()
print(df2)

df2 = df['twenty ten'].mean()
print(df2)


jan = {
    "years": ["50's","60's", "70's", "80's", "90's", "00's", "10's"] 
    "temps": [35.85, 34.45, 30.40, 32.20, 35.90, 35.60, 34.45]
}


df = pd.read_csv (r'feb.csv')


filename = 'feb.csv'
with open('feb.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)

feb = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [38.90, 34.31, 35.35, 36.29, 40.27, 38.52, 38.98]
}



df = pd.read_csv (r'March.csv')


filename = 'March.csv'
with open('March.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)


March = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [44.57, 43.83, 46.96, 46.24, 46.88, 48.38, 48.49]
}



df = pd.read_csv (r'april.csv')


filename = 'april.csv'
with open('april.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)


april = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [56.72, 56.62, 56.69, 56.16, 56.81, 58.92, 60.20]
}


df = pd.read_csv (r'may.csv')


filename = 'may.csv'
with open('may.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)


may = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [66.60, 64.86, 65.15, 65.92, 66.43, 67.16, 69.99]
}


df = pd.read_csv (r'june.csv')


filename = 'june.csv'
with open('june.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)


june = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [75.04, 72.87, 73.58, 74.29, 75.02, 75.57, 77.44]
}



df = pd.read_csv (r'july.csv')


filename = 'july.csv'
with open('july.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)


july = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [78.68, 76.62, 77.03, 78.94, 79.24, 78.15, 80.58]
}



df = pd.read_csv (r'aug.csv')


filename = 'aug.csv'
with open('aug.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)


aug = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [77.02, 75.35, 76.20, 77.18, 77.18, 78.89, 79.05]
}


df = pd.read_csv (r'sept.csv')


filename = 'sept.csv'
with open('sept.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)


sept = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [70.17, 68.44, 70.30, 69.91, 69.99, 71.37, 73.21]
}



df = pd.read_csv (r'oct.csv')


filename = 'oct.csv'
with open('oct.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)


oct = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [58.46, 57.36, 57.58, 57.82, 59.19, 59.50, 60.96]
}



df = pd.read_csv (r'nov.csv')


filename = 'nov.csv'
with open('nov.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)


nov = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [44.39, 45.91, 46.97, 47.89, 47.49, 49.13, 47.56]
}

'''

df = pd.read_csv (r'dec.csv')


filename = 'dec.csv'
with open('dec.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)
print(header_row)

df4 = df['fifties'].mean()
print(df4)

df4 = df['sixties'].mean()
print(df4)

df4 = df['seventies'].mean()
print(df4)

df4 = df['eighties'].mean()
print(df4)

df4 = df['nineties'].mean()
print(df4)

df4 = df['twok'].mean()
print(df4)

df4 = df['twenty ten'].mean()
print(df4)

'''
dec = {
    "years": ["50's" "60's" "70's" "80's" "90's" "00's" "10's"] 
    "temps": [37.39, 34.76, 38.57, 36.17, 39.39, 37.58, 40.97]
}
'''


#_______________________________________________________________


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import csv
import numpy as np
#________________________________________________________________


# x axis values 
x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec", ]

# corresponding y axis values 
ys = {
  "50s": [35.85,  38.90, 44.57, 56.72, 66.60, 75.04, 78.68, 77.02, 70.17, 58.46, 44.39, 37.39],
  "60s": [34.45, 34.31, 43.83, 56.62, 64.86, 72.87, 76.62, 75.35, 68.44, 57.36, 45.91, 34.76],
  "70s": [30.4, 35.35, 46.96, 56.69, 65.15, 73.58, 77.03, 76.20, 70.30, 57.58, 46.97, 38.57],
  "80s": [32.2, 36.29, 46.24, 56.16, 65.92, 74.29, 78.94, 77.18, 69.91, 57.82, 47.89, 36.17],
  "90s": [35.9, 40.27, 46.88, 56.81, 66.43, 75.02, 79.24, 77.18, 69.99, 59.19, 47.49, 39.39],
  "00s": [35.6, 38.52, 48.38, 58.92, 67.16, 75.57, 78.15, 78.89, 71.37, 59.50, 49.13, 37.58],
  "10s": [34.45, 38.98, 48.49, 60.2, 69.99, 77.44, 80.58, 79.05, 73.21, 60.96, 47.56, 40.97],
} 
 
# plotting the points  
# plt.plot(x, y["five"], y["six"], y["seven"], y["eight"], y["nine"], y["twok"], y["ten"])
for y in ys:
  plt.plot(x, ys[y], label=y)
  print('For Key: ', y, "   Value: ", ys[y])

# plt.plot(x, y["five"], "", label="50s")
# plt.plot(x, y["six"], "", label="60s")
# plt.plot(x, y["seven"], "", label="70s",)
# plt.plot(x, y["eight"], "", label="80s",)
# plt.plot(x, y["nine"], "", label="90s",)
# plt.plot(x, y["twok"], "", label="00s",)
# plt.plot(x, y["ten"], "", label="10s",)


plt.legend()

    
# naming the x axis 
plt.xlabel('Months')

# naming the y axis 
plt.ylabel('Temperature') 
   
# giving a title to my graph 
plt.title('Average Temputures by Decade') 
    
# function to show the plot 
plt.show() 

