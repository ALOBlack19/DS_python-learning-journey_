# # LAB 5: Matplotlib
import matplotlib.pyplot as plt

# Exercise 4: Histogram
import numpy as np
data = np.random.normal(0, 1, 500) # 500 data points from a normal distribution

plt.hist(data,bins = 20, edgecolor = 'black') # Bins = number of bars
plt.ylabel("Values")
plt.xlabel("Distribution count")
plt.title("Normal Distribution")

plt.show()