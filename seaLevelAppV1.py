import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# This is a rough POC of using .csv data from NOAA to plot 
# Regional Sea Level(rsl) change from Charleston, SC based on studies 
# referenced at: https://tidesandcurrents.noaa.gov/sltrends/sltrends_station.shtml?id=8665530

# Needs: -Projections based on Regional Sea Level Trends(2000-2020)
#        -Dataframe to select 2000-2020
#        -Animation of horizontal line over time

rslF = pd.read_csv('linearTrendCharleston.csv')

dataStrm = rslF[['Year','Linear_Trend']]

# had to hard code lines in here need to figure out dataframes
x = dataStrm['Year'][976:1227]
y = dataStrm['Linear_Trend'][976:1227]

plt.scatter(x, y, 1)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.axhline(y=0.07,color = 'b',linestyle = '-')

plt.xlabel("Year")
plt.ylabel("Sea Level(m)")
plt.title("8665530 Charleston, SC")
plt.grid()

plt.show()