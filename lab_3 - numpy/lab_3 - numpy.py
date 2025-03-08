#                 LAB 3 - NUMPY ARRAYS - RANDOM
# ________________________________________________________________________
# TASK 1: Creating a 1D NumPy Array
import numpy as np

arr = []
x = 0
for i in range (1,31):
    arr.append(i)
    x = np.array(arr)
print("Task 1: The array is: ", x)
print()
print("Task 1: The type is: ",type(x))
print()
print("Task 1: The number 10 is in the position: ",np.where(x == 10)[0][0])
print()
print("Task 1: The shape is: ",np.shape(x))
print()

# ________________________________________________________________________
# Task 2: Creating a 2D NumPy Array
ns = np.reshape(x,(6,5),'C')
print("Task 2: New shaped array:\n", ns)
print()
print("Task 2: In the position row 3, column 4 is the number: ",ns[2,3])
print()

# ________________________________________________________________________
# Task 3: Subsetting a 2D Array

ns_1 = ns[2,:]
print("Task 3: third row: ",ns_1)
print()
ns_2 = ns[:2,]
print("Task 3: first two rows:\n", ns_2)
print()
ns_3 = ns[:,2:6]
print("Task 3: the last three columns:\n", ns_3)
print()

# ________________________________________________________________________
# Task 4: Generating Random Integer Array
from numpy import random
ns_4 = random.randint(10,100, size = 15)
print("Task 4: The random array between 10 and 100 is: ", ns_4)
print()

ns_4_max = np.max(ns_4)
print("Task 4: the max value of the random array is: ", ns_4_max)
print()

ns_4_min = np.min(ns_4)
print("Task 4: the max value of the random array is: ",ns_4_min)
print()

# ________________________________________________________________________
# Task 5: Generating a 2D Random Array

ns_5 = random.randint(50, size = (4,4))
print("Task 5: the 2D array of shape (4, 4): ", ns_5)
print()

ns_5_sum = np.sum(ns_5)
print("Task 5: The sum of the 2D array of shape (4, 4) is: ", ns_5_sum)
print()
# ________________________________________________________________________
# Task 6: Manipulating Array

ns_6 = random.randint(1,20, size = (5,5))
print("Task 6: The array with (shape 5, 5) between 1 and 20:\n", ns_6)
print()

ns_6[1] = 0
print("Task 6: second row as zero:\n", ns_6)
print()

ns_6[ns_6 > 10] = 99
print("Task 6: Replacing all values greater than 10 with 99:\n", ns_6)
print()

# ________________________________________________________________________
# Task 7: Arithmetic Operations on Array
ns_7 = random.randint(10, size = 5)
ns_7_2 = random.randint(10, size = 5)

ns_7_sum = ns_7 + ns_7_2
print("Task 7: First array 1D", ns_7)
print("Task 7: second array 1D", ns_7_2)
print("Task 7: Element wise sum: ", ns_7_sum)
print()

ns_7_sub = ns_7 - ns_7_2
print("Task 7: First array 1D", ns_7)
print("Task 7: second array 1D", ns_7_2)
print("Task 7: Element wise subtraction: ", ns_7_sub)
print()

ns_7_mult = ns_7 * ns_7_2
print("Task 7: First array 1D", ns_7)
print("Task 7: second array 1D", ns_7_2)
print("Task 7: Element wise multiplication: ", ns_7_mult)
print()

ns_7_div = ns_7 // ns_7_2
print("Task 7: First array 1D", ns_7)
print("Task 7: second array 1D", ns_7_2)
print("Task 7: Element wise division: ", ns_7_div)
print()

# ________________________________________________________________________
# Task 8: Broadcasting in NumPy

ns_8 = np.array([2,4,6,8])
ns_8_2 = random.randint(1,5, size = (3,4))

ns_broad = ns_8 + ns_8_2
print("Task 8: Array 1D: ",ns_8)
print("Task 8: Array 2D:\n", ns_8_2)
print("Task 8: Broadcasting array:\n", ns_broad)
print()


# ________________________________________________________________________
# Task 9: Filtering an Array

ns_9 = random.randint(1,100, size = 20)
print("Task 9: Array 1D: ", ns_9)
print()
print("Task 9: Greater than 50 elements:\n",ns_9[ns_9 > 50])
print()
ns_9[ns_9 < 30] = - 1
print("Task 9: values less than 30 with -1:\n",ns_9)
print()

# ________________________________________________________________________
# Task 10: Reshaping Array

ns_10 = random.randint(1,50, size = 12)
ns_10_2 = np.reshape(ns_10,(3,4),'C')
ns_10_3 = np.reshape(ns_10,(4,3),'F')

print("Task 10: Original 1D array: ", ns_10)
print()
print("Task 10: 2D 3x4 array 'C' order:\n", ns_10_2)
print()
print("Task 10: 2D 3x4 array 'F' order:\n", ns_10_3)

# GLOSSARY -
# ns = new shape

# REFERENCES -
# https://www.statology.org/numpy-replace/
# https://www.w3schools.com/python/numpy/numpy_random.asp
# https://pt.stackoverflow.com/questions/200818/como-quebrar-a-linha
# https://www.geeksforgeeks.org/numpy-array-broadcasting/