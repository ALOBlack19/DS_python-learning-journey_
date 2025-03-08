# # LAB 5: Matplotlib
import matplotlib.pyplot as plt

# Exercise 3: Bar Plot

categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
values = [10, 15, 7, 12, 5]

plt.bar(categories,values)

plt.xlabel("Fruits")
plt.ylabel("Values")
plt.title("Products prices")

plt.show()