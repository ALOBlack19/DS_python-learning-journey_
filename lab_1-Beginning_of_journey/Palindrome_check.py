
#Bonus Exercises_________________________________________________________________________________
#   Palindrome Check
#   Write a function that checks whether a given string is a palindrome (reads the same forwards and backwards). Test it with the strings "madam" and "hello".

palindrome1 = "madam"
palindrome2 = "hello"

def palindorme_checker(palindrome):

    return palindrome == palindrome[::-1]

print(palindorme_checker(palindrome1))
print(palindorme_checker(palindrome2))

# Using the user input
# # user_word = input("insert here a word to check if it is a palindrome or not: ")
# #
# # straight = ""
# # reverse = ""
# #
# # def palin_checker (user_word):
# #     return user_word == user_word[::-1]
# #
# # if palin_checker(user_word):
# #     straight += user_word
# #     print(straight, "is a palindrome!")
# # else:
# #     reverse += user_word
# #     print(reverse, "is not a palindrome!")

#  Bonus Exercise 2 - List to String Conversion
# Convert the list ['P', 'y', 't', 'h', 'o', 'n'] to a single string "Python". Print the result.

list_python = ['P', 'y', 't', 'h', 'o', 'n']

python_str = "".join(list_python)

print(python_str)



