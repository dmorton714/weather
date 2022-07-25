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

