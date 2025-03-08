# Exercise 1 -  List Creation and Access:--------------------------------------------------------------
# Create a list with the following elements: 1, 2, 3, 4, 5. Print the third element in the list.


list_ = [1,2,3,4,5]
print("The third element of the list is:",list_[2])

# Exercise 2 - List Manipulation:----------------------------------------------------------------------
# Append the number 6 to the list created in the previous exercise. Print the updated list.
# Remove the second element from the list. Print the updated list.

list_.append(6)
print(list_)

removed_item = list_[1]
list_.pop(1)
print(list_)
print("The element removed is:",removed_item)


# Exercise 3 - List slicing:----------------------------------------------------------------------
# Given the list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], print the first five elements.
# Print the last three elements of the list.
# Print every second element of the list.

list_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list_num[:5])
print(list_num[-3:])
print(list_num[1::2]) # [min:max:interval]

# Exercise 4 - List Operations:----------------------------------------------------------------------
# Create a list of numbers from 1 to 10. Calculate and print the sum of all elements in the list.
# Find and print the maximum and minimum values in the list.


numbers = [i for i in range(1,11)] # numbers = list(range(1,11))
print(numbers)

soma = 0
for i in numbers:
    soma += i
print(f"The sum of the elements of the list is:",soma)

mini = 0
maxi = 0
for i in numbers[:]:
    if i < numbers[1]:
        mini = i
    elif i > numbers[-2]:
        maxi = i
print(f"The smallest number of the list is:",min)
print(f"The greatest number of the list is:",max)


# Exercise 5 - List Comprehension----------------------------------------------------------------------
# Create a list of squares for numbers from 1 to 10 using list comprehension. Print the list.

l_squares = [i * i for i in range(1,11)] # l_squares = [x ** 2 for in range(1,11)]

print("the list of squares looks like:",l_squares)

# Exercise 6 - Nested Lists----------------------------------------------------------------------
# Create a list that contains three lists: [1, 2, 3], [4, 5, 6], and [7, 8, 9].
# Access and print the element 5 from the nested list.

num1 = [i for i in range(1,4)]
num2 = [i for i in range(4,7)]
num3 = [i for i in range(7,10)]

print(num1)
print(num2)
print(num3)

num_total = num1 + num2 + num3
print(num_total)
print("The element 5 is:",num_total[4])

#Another way to do------------------------------------------------------------------
element_5 = 0

for i in num_total:
    if i < num_total[5]:
        element_5 = i
print("The element 5 is:",element_5)
#------------------------------------------------------------------------------------

## String Exercises

#  Exercise 1 - String Creation and Access
#  Create a string with the value "Hello, World!". Print the first and last character of the string.

sentence = str("hello, world!")

print(f"The first character is:", {sentence[0]})
print(f"The last character is:", {sentence[-1]})

# String Slicing____________________________________________________________________

# Exercise - Given the string "Python Programming", print the substring "Python".
# Print the substring "Programming".

sent = str("Python Programming")
print(f"the first substring is: {sent[:7]}")

print(f"the second substring is: {sent[-11:]}")
#__________________________________________________________________________________
# String Methods

#  Exercise 3 - Convert the string "hello, world!" to uppercase and print it.
#  Replace "World" with "Python" in the string "Hello, World!" and print the updated string.

phrase = "hello, world!"
phrase_upper = phrase.upper()
print(phrase_upper)

new_phrase = (phrase.replace("world","python"))

print(new_phrase)

# Exercise 4 - String Concatenation ----------------------------------------------------------------------
#  Concatenate the strings "Hello" and "World" with a space in between. Print the result.

h = "hello"
w = "world"

hw = h + w

print(h + "" + w), print(h,w)

# Exercise 5 - String Splitting ----------------------------------------------------------------------
# Given the string "apple,banana,cherry", split it by commas and print the resulting list.

fruits = str("apple,banana,cherry")

ft_list = fruits.split(",")

print("the list of fruits is:",ft_list )
print("the first fruits of the list is:",ft_list[0])
print("the second fruits of the list is:",ft_list[1])
print("the third fruits of the list is:",ft_list[2])
print(type(ft_list))

# Exercise 6 - String Formatting ----------------------------------------------------------------------
# Use string formatting to create a string that says "My name is [name] and I am [age] years old",
# where [name] and [age] are variables. Print the result.

#n = input("insert your name:" )
#a = input("Now, your age:", )

n = "Amir"
a = 26

print(f"My name is {n} and I am {a} years old")

# Exercise 7 - String Reversal ----------------------------------------------------------------------
# Write a program that takes a string input from the user and prints the string in reverse order.

rev = input("insert a message:", )

rev_spt = rev.split()
#print(rev_spt)
#print(type(rev_spt))

reverse = rev[::-1] # total reverse order, for each letter and each word.
print("total reverse order:", reverse)

reverse_words = rev_spt[::-1] # reverse order for each word
print("reverse order for each word:", reverse_words)

























