# # LAB 5: Matplotlib
import matplotlib.pyplot as plt
# Exercise 6: Subplots

#                    DATA
#                   PLOTTING
fig, axs = plt.subplots(2,2)
# Line plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
axs[0, 0].plot(x, y)
axs[0, 0].set_title("Line chart xy")
# Bar plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
axs[0,1].bar(categories, values)
axs[0,1].set_title("Bar chart cv")

# Histogram
data = np.random.randn(1000)
axs[1,0].hist(data, bins = 20, edgecolor = 'pink')
axs[1,0].set_title("Histogram")

# Scatter Plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
axs[1,1].scatter(x_scatter, y_scatter)
axs[1,1].set_title("Scatter plot")

plt.tight_layout()
plt.show()