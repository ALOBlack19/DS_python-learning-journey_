#                                                        LEARNING FUNCTIONS

# 1. Function Basics: Write a function called greet that takes a name as an argument and prints a greeting message with that name.

def greet ():
    """
    Greet the user by asking for their name and returning a welcome message.
    :return:
    """
    name = input("what is your name? ").capitalize()
    if name == "":
        print("Try again")
        return greet()
    for letters in name:
        if letters.isdigit():
            print("Number not allowed, only letters")
            return greet()
    return f"welcome {name}!"
print(greet())


# # 2. Return Values: Create a function square that takes an integer and returns its square.

def square():
    """
    Square a number and return the result.
    :return:
    """
    num = input("Insert a number to let it square: ")
    if num == "":
        print("Try again")
        return square()

    if not num.isdigit():
        print("letters not allowed, only numbers")
        return square()
    num = float(num)
    return f"The square of {num} is {num**2}"
print(square())


# 3. Multiple Parameters: Write a function add that takes two numbers as parameters and returns their sum.

def add(x, y):
    """
    Add two numbers and return the result.
    :param x:
    :param y:
    :return:
    """
    return x + y
print(f"The sum of the numbers and are: ",add(5,8))

# 4. Default Parameters: Write a function greet_user that greets the user with a default name if no name is provided. The default name should be "Guest".

def greet_user(name= "Guest"):
    """
    Greet the user with a default name if no name is provided.
    :param name:
    :return:
    """
    return  f"Welcome {name}"

print(greet_user())

# 5. Keyword Arguments: Write a function format_address that takes street, city, and country as keyword arguments and returns a formatted address string.

def format_address(house_number, street, city, country, code):
    """
    Format an address string with house number, street, city, country and code.
    :param house_number:
    :param street:
    :param city:
    :param country:
    :param code:
    :return:
    """
    return f" {house_number} {street}, {city}, {country}, {code}"

print("Address: ", format_address(1463, "North 8th Avenue", "Vancouver", "Canada", "V7P 1R8"))

# 6. Docstrings: Create a function factorial that calculates the factorial of a given number and includes a docstring explaining the function.

def factorial(num):
    """
    Calculate the factorial of a number.
    :param num:
    :return:
    """
    if num < 0:
        return "Negative numbers do not have a factorial"
    if num == 0 or num ==1:
        return 1
    fac = 1
    for i in range(2,num + 1):
        fac *= i
        print(i,fac) # Getting the main idea of the core code -> for i in range(2,num + 1) <- This makes the factorial happen.
    return fac
print(f"The factorial is: ",factorial(5))

# 7. Calculate BMI: Write a function calc_bmi that takes 2 numbers (height and weight) and returns the bmi.

def calculate_bmi(weight,height):
    """
    Calculate the BMI based on weight and height, and classify in Underweight, Normal weight and Overweight categories.
    :param weight:
    :param height:
    :return:
    """
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"Your BMI is {bmi:.2f}, evaluated as Underweight"
    if bmi >= 18.5 and bmi < 24.9:
        return f"Your BMI is {bmi:.2f}, evaluated as Normal weight"
    if bmi >= 25 and bmi < 29.9:
        return f"Your BMI is {bmi:.2f}, evaluated as Overweight"

print(calculate_bmi(74.5,1.73))

# 8. Simple Arithmetic: Write a function multiply that takes two numbers as parameters and returns their product.

def mult(x, y):
    """
    Multiply two numbers.
    :param x:
    :param y:
    :return:
    """
    return x * y

# 9. String Manipulation: Write a function reverse_string that takes a string as an argument and returns the reversed string.

def reversed_string(word):
    """
    Reverse a given string.
    :param word:
    :return:
    """
    return word[::-1]

# 10. Boolean Functions: Write a function is_even that takes an integer and returns True if the number is even and False otherwise.

def is_even(num):
    """
    Check if a number is even.
    :param num:
    :return:
    """
    if num % 2 == 0:
        return True
    else:
        return False

# 11. List Operations: Write a function sum_list that takes a list of numbers and returns the sum of the list.

def sum_list(list_numbers):
    """
    Calculate the sum of a list of numbers.
    :param list_numbers:
    :return:
    """
    total = 0
    for i in list_numbers:
        total += i
    return total
print("Total: ",sum_list([9,8,7,6,5]))

# 12. Count Occurrences: Write a function count_vowels that takes a string and returns the number of vowels in the string.

def count_vowels(word):
    """
    Count the number of vowels in a given word.
    :param word:
    :return:
    """
    vowels = "aeiouAEIOU"
    count = 0
    for letters in word:
        if letters in vowels:
            count += 1
    return count

# 13. Find Maximum: Write a function find_max that takes three numbers and returns the maximum of the three.

def find_max(num1, num2, num3):
    """
    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return max_num

# 14. Palindrome Check: Write a function is_palindrome that takes a string and returns True if the string is a palindrome and False otherwise.

def palindrome_checker(word):
    """
    Check if a word is a palindrome.
    :param word:
    :return:
    """
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
print(palindrome_checker("madam"))

# 15. Temperature Conversion: Write a function celsius_to_fahrenheit that takes a temperature in Celsius and returns the temperature in Fahrenheit.

def temperature_conversion(celsius):
    """
    Convert Celsius to Fahrenheit.
    :param celsius:
    :return:
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit