#                                       LOOPS EXERCISES
from snowballstemmer.tamil_stemmer import lab16

# 1. Write a loop to print each character in the string "Python".

word = "python"
for letters in word:
    print("\nspelling:",letters)

# 2. Write a loop to count the number of vowels in the string "data science".

course = "data science"
vowels = "aeiouy"
ct = ""
for l in course:
    if l in vowels:
        ct += l
print("\nThe number of vowels is:",len(ct))
print("\nvowels counted:",ct)

# 3. Write a loop to reverse the string "hello world" and print the reversed string.

s_t_reverse = "hello world"

opposite = ""

for le in s_t_reverse[::-1]:
    opposite += le

print("\nnormal: ",s_t_reverse)
print("\nreverse: ",opposite)

# 4. Write a loop to print the ASCII value of each character (search ord() function)
# in the string "coding".

word_2 = "coding"
word_list = list(word_2)
ASCII_ = []

for ls in word_list:
    ASCII_.append(ord(ls))
print("\n",word_list)
print("\n",ASCII_)

# 5. Write a loop to count the number of times the character "e" appears
# in the string "experience".

word3 = "experience"

let = "e"

number_of_e = list()

for w3 in word3:
    if w3 == let:
        number_of_e.append(w3)
print("\n","the number of the vowel 'e' is: ",len(number_of_e))

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

print("\n",new_word)

# 7. Write a loop to print every second character in the string "looping".
# use range / range only works with integer
lp = "looping"
lp_rule = []
for i in range(1,len(lp),2):
    lp_rule += lp[i]
print("\n",lp_rule)

# 8. Write a loop to find the first repeating character in the string "swiss"

word = "swiss"
new = ""

for w in word:
    new += word[:]
    if new == w:
        break
print("\n",new)
 # this is not working

# 9. Write a loop to capitalize each word in the string "machine learning is fun".

machi = "machine learning is fun"
machi_list = list(machi)
cap_machi = ""
for i in machi_list:
    cap_machi += (i)
print("\n",cap_machi)

# it is possible to add what you want to check in the loop, for i in ->"here"<-

# 10. Write a loop to check if the string "racecar" is the same forwards and backwards (ignore case).

s1 = "racecar"
str_forward = []
str_backwards = []
for i in s1:
    str_forward.append(i)
for i in s1[::-1]:
    str_backwards.append(i)
if str_forward == str_backwards:
    print("\nracecar is palindrome")
else:
    print("not a palindrom")

# LIST QUESTIONS

# 1. Write a loop to print each element in the list [10, 20, 30, 40, 50].

l1 = [10, 20, 30, 40, 50]
for i in l1:
    print("\n",i)

# 2. Write a loop to calculate the sum of all elements in the list [1, 2, 3, 4, 5].

l2 = [1, 2, 3, 4, 5]
v_list = []
v = 0
for obj in l2:
    v += obj
    v_list.append(v)
print("\nThe result of each sum of the values in the list is:",v_list)
print("\nThe total sum of the list is:", v)

# 3. Write a loop to find the largest number in the list [3, 7, 2, 9, 4].
l3 = [3, 7, 2, 9, 4]
max_v = 0
for obj in l3:
    if  obj > max_v:
        max_v = obj
print("\nlargest number is:",max_v)

# 4. Write a loop to count how many times the number 4 appears in the list [1, 4, 4, 2, 4, 3].

l4 = [1, 4, 4, 2, 4, 3]
c = []
for i in l4:
    if i == 4:
        c.append(i)
print(f"\nThe number 4 appears -> {len(c)} <- times")

# 5.Write a loop to create a new list that contains the squares of each number in the list [1, 2, 3, 4, 5].

l5 = [1, 2, 3, 4, 5]
l_square = []
for i in l5:
    l_square.append(i * i)
print(f"\nOriginal list {l5}\nSquare list {l_square}")

# 6. Write a loop to concatenate all the words in the list ["Python", "is", "awesome"] into a single string.

l6 = ["Python", "is", "awesome"]
c_l6 = " "
for i in l6:
   c_l6 += i + " "
print(c_l6.strip())

# 7.Write a loop to create a new list that contains only the even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# 8. Write a loop to multiply each number in the list [2, 4, 6, 8] by 2 and store the results in a new list.

# 9. Write a loop to remove all occurrences of the number 3 from the list [1, 3, 3, 4, 3, 5, 3].

# 10. Write a loop to find the index of the first occurrence of the number 7 in the list [5, 7, 8, 7, 10].