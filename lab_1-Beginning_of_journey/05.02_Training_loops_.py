
# 1. Write a loop to print each character in the string "Python".

word = "python"
for letters in word:
    print("spelling:",letters)

# 2. Write a loop to count the number of vowels in the string "data science".

course = "data science"
vowels = "aeiouy"
ct = ""
for l in course:
    if l in vowels:
        ct += l
print("The number of vowels is:",len(ct))
print("vowels counted:",ct)

# 3. Write a loop to reverse the string "hello world" and print the reversed string.

s_t_reverse = "hello world"

opposite = ""

for le in s_t_reverse[::-1]:
    opposite += le

print("normal: ",s_t_reverse)
print("reverse: ",opposite)

# 4. Write a loop to print the ASCII value of each character (search ord() function)
# in the string "coding".

word_2 = "coding"
word_list = list(word_2)
ASCII_ = []

for ls in word_list:
    ASCII_.append(ord(ls))
print(word_list)
print(ASCII_)

# 5. Write a loop to count the number of times the character "e" appears
# in the string "experience".

word3 = "experience"

let = "e"

number_of_e = list()

for w3 in word3:
    if w3 == let:
        number_of_e.append(w3)
print("the number of the vowel 'e' is: ",len(number_of_e))

# 6. Write a loop to replace each vowel in the string "education" with an asterisk (*).

ed = "education"
vow = "aeiou"
ast = "*"
new_word = ""

for lt in ed:
    print(lt)
    if lt in vow:
        new_word += ast
    else:
        new_word += lt

print(new_word)

# 7. Write a loop to print every second character in the string "looping".
# use range / range only works with integer
lp = "looping"
lp_rule = []
for i in range(1,len(lp),2):
    lp_rule += lp[i]
print(lp_rule)

# 8. Write a loop to find the first repeating character in the string "swiss"

word = "swiss"
new = ""

for w in word:
    new += word[:]
    if new == w:
        break
print(new)
 # this is not working

# 9. Write a loop to capitalize each word in the string "machine learning is fun".

machi = "machine learning is fun"
machi_list = list(machi)
cap_machi = ""
for i in machi_list:
    cap_machi += (i)
print(cap_machi)

# it is possible to add what you want to check in the loop, for i in ->"here"<-

# 10. Write a loop to check if the string "racecar" is the same forwards and backwards (ignore case).


# LIST QUESTIONS

# 1. Write a loop to print each element in the list [10, 20, 30, 40, 50].

# 2. Write a loop to calculate the sum of all elements in the list [1, 2, 3, 4, 5].

# 3. Write a loop to find the largest number in the list [3, 7, 2, 9, 4].

# 4. Write a loop to count how many times the number 4 appears in the list [1, 4, 4, 2, 4, 3].

# 5.Write a loop to create a new list that contains the squares of each number in the list [1, 2, 3, 4, 5].

# 6. Write a loop to concatenate all the words in the list ["Python", "is", "awesome"] into a single string.

# 7.Write a loop to create a new list that contains only the even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# 8. Write a loop to multiply each number in the list [2, 4, 6, 8] by 2 and store the results in a new list.

# 9. Write a loop to remove all occurrences of the number 3 from the list [1, 3, 3, 4, 3, 5, 3].

# 10. Write a loop to find the index of the first occurrence of the number 7 in the list [5, 7, 8, 7, 10].