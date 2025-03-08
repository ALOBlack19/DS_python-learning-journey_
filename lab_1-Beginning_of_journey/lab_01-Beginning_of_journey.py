# lab_01-Beginning_of_journey.py

# Exercise 1 - Write a Python program that prints ‘My first program in Python!’
print("My first exercise in Python!")

# Exercise 2 - Determine the data type of the following variables using the type() function
a = 10
b = 3.14
c = "Python"
d = True
e = [1, 2, 3]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Exercise 3 - Convert the data types
b = int(b)
a = float(a)
d = int(d)

print(type(b))
print(type(a))
print(type(d))

# Exercise 4 - Given the string: “Python is Amazing!”
ex4 = "Python is Amazing!"

# Convert the string to all lowercase
ex4_2 = ex4.lower()
print(ex4_2)

# Convert the string to all uppercase
ex4_3 = ex4_2.upper()
print(ex4_3)

# Find the index of the word "Amazing"
print(ex4.index("Amazing"))

# Replace "Amazing" with "Fun"
print(ex4.replace("Amazing", "Fun"))
ex4 = ex4.replace("Amazing", "Fun")
print(ex4)

# Slice the string
print(ex4[:6])
print(ex4[:-3])

# Exercise 5 - Check if an integer is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print(f"The value typed {num} is positive")
elif num < 0:
    print(f"The value typed {num} is negative")
else:
    print(f"The value typed is {num}")

# Exercise 6 - Check if the number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"The value typed {num} is even")
else:
    print(f"The value typed {num} is odd")

# Exercise 7 - Count the number of vowels in a string
cl = str(input("Enter a string: "))

vowels = "aeiouAEIOU"
total_vowels = 0
for letters in cl:
    if letters in vowels:
        total_vowels += 1

print(f"The total of vowels is: {total_vowels}")

# Exercise 8 - Reverse the order of words in a sentence
inp_sent = str(input("Enter a sentence: "))

frag = inp_sent.split()
print(frag)
print(type(frag))

reversed_frag = frag[::-1]
print(reversed_frag)
print(type(reversed_frag))

reversed_sentence = " ".join(reversed_frag)
print("Original sentence:", inp_sent)
print("Reversed sentence:", reversed_sentence)

# Exercise 9 - Remove duplicate characters from a string
input_string = str(input("Enter a string: "))

def rem_dupli(input_string):
    result = ""
    basket = []
    for char in input_string:
        if char not in result:
            result += char
            basket.append(char)
    return result

print(rem_dupli(input_string))

# Exercise 10 - Rock, Paper, Scissors game
import random

print("Let's play Rock x Paper x Scissors!")

user_choice = input("Enter your choice (rock, paper, or scissors): ")

if user_choice not in ["rock", "paper", "scissors"]:
    print("Try again! If you don't want to play, go away :), please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")