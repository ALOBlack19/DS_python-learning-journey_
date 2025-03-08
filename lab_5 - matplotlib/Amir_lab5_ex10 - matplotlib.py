# # LAB 5: Matplotlib
import matplotlib.pyplot as plt

# Exercise 10: Line Plot with Annotations

x = range(0, 20)
y = [value ** 2 for value in x]

plt.plot(x,y)
plt.annotate('minimum', xy = (min(x), min(y)), xycoords='data')
plt.annotate('maximum', xy = (max(x), max(y)), xycoords='data')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Line plot with annotations")
plt.show()