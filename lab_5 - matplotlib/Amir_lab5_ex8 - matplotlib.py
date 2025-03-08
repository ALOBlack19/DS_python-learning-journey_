# # LAB 5: Matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Exercise 8: Stacked Bar Plot
categories = ['Group 1', 'Group 2', 'Group 3']
value1 = [5, 7, 3]
value2 = [6, 8, 4]
value3 = [4, 3, 5]
array1 = np.array(value1)
array2 = np.array(value2)
array3 = np.array(value3)

fig, ax = plt.subplots(1)
ax.bar(categories, array1, label = value1)
ax.bar(categories, array2, bottom = array1, label = value2)
ax.bar(categories, array3, bottom = array1 + array2, label = value3)

plt.xlabel('Categories')
plt.ylabel('values')
plt.legend(["Value 1", "Value 2", "Value 3"])
plt.title("Stacked bar plot")

plt.tight_layout()

plt.show()