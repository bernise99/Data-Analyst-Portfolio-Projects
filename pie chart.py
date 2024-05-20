# import matplotlib.pyplot for designing pie chart and give it a name plt


import pandas as pd

from matplotlib import pyplot as plt

x = [1,2,3]
y = [1,4,9]
z = [10,5,0]

plt.plot(x,y)
plt.plot(x,z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["This is y", "This is z"])
plt.show()

sample_data = pd.read_csv('sample_data.csv')

type(sample_data)


type(sample_data.column_c)

plt.plot(sample_data.column_a, sample_data.column_b)
plt.plot(sample_data.column_a, sample_data.column_c)
plt.title("Data Visualization")
plt.xlabel("a")
plt.ylabel("b and c")
plt.legend(["This column b", "This is column c"])
plt.show()

data = pd.read_csv('countries.csv')

#compare the population growth in the US and Egypt

us = data[data.country == "United States"]

eg = data[data.country == "Egypt"]

plt.plot(us.year, us.population / 10**6)
plt.plot(eg.year, eg.population / 10**6)
plt.title("Population Compare")
plt.xlabel("Year")
plt.ylabel("poplation in Million")
plt.legend(["United States" , "Egypt"])
plt.show()

plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(eg.year, eg.population / eg.population.iloc[0] * 100)
plt.title("Population Compare")
plt.legend(["United States" , "Egypt"])
plt.xlabel("Year")
plt.ylabel("poplation gowth (first year = 100 )")
plt.show()
