# # LAB 5: Matplotlib

import matplotlib.pyplot as plt

# Exercise 2: Customizing Plots

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

plt.plot(x,y,"g--", marker = 'd', markersize = 8)

plt.ylabel("Zero to six")
plt.xlabel("Doubles")
plt.title("Natural numbers and theirs squares")
plt.grid(True)
plt.show()