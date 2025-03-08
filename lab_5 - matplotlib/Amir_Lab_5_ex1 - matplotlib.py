# # LAB 5: Matplotlib
import matplotlib.pyplot as plt
# Exercise 1: Basic Line Plot

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

plt.plot(x,y)

plt.ylabel("Zero to six")
plt.xlabel("Doubles")
plt.title("Natural numbers and theirs squares")
plt.show()

