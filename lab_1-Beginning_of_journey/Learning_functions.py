#                                                        LEARNING FUNCTIONS


# 1. Function Basics: Write a function called greet that takes a name as an argument and prints a greeting message with that name.

def greet ():
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
    :param x:
    :param y:
    :return:
    """
    return x + y
print(f"The sum of the number is",add(5,8))

# 4. Default Parameters: Write a function greet_user that greets the user with a default name if no name is provided. The default name should be "Guest".

def greet_user(name= "Guest"):
    """
    :param name:
    :return:
    """
    return  f"Welcome {name}"

print(greet_user())

# 5. Keyword Arguments: Write a function format_address that takes street, city, and country as keyword arguments and returns a formatted address string.

def format_address(house_number, street, city, country, code):
    """
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
    :param num:
    :return:
    """
    fac = 1
    for i in range(2,num+1):
        fac *= i
    return fac
print(f"The factorial is: ",factorial(4))

# 7. Calculate BMI: Write a function calc_bmi that takes 2 numbers (height and weight) and returns the bmi.

# 8. Simple Arithmetic: Write a function multiply that takes two numbers as parameters and returns their product.

# 9. String Manipulation: Write a function reverse_string that takes a string as an argument and returns the reversed string.

# 10. Boolean Functions: Write a function is_even that takes an integer and returns True if the number is even and False otherwise.

# 11. List Operations: Write a function sum_list that takes a list of numbers and returns the sum of the list.

# 12. Count Occurrences: Write a function count_vowels that takes a string and returns the number of vowels in the string.

# 13. Find Maximum: Write a function find_max that takes three numbers and returns the maximum of the three.

# 14. Palindrome Check: Write a function is_palindrome that takes a string and returns True if the string is a palindrome and False otherwise.

# 15. Temperature Conversion: Write a function celsius_to_fahrenheit that takes a temperature in Celsius and returns the temperature in Fahrenheit.