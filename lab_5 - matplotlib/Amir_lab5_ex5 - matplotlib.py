# # LAB 5: Matplotlib
import matplotlib.pyplot as plt
# Exercise 5: Scatter Plot

import numpy as np
x = np.random.rand(50) # 50 random x-values between 0 and 1
y = np.random.rand(50) # 50 random y-values between 0 and 1

plt.scatter(x,y)

plt.xlabel("Random distribution x")
plt.ylabel("Random distribution y")
plt.title("Random values between 0 and 1")

plt.show()