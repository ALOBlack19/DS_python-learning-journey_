# # LAB 5: Matplotlib
import matplotlib.pyplot as plt
# Exercise 7: Pie Chart

categories = ['Marketing', 'Development', 'Sales', 'Support']
values = [20, 35, 25, 20]

plt.pie(values, labels = categories)
plt.title("Departments chart")

plt.show()