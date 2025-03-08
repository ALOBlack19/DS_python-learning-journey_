# Lab 4 - Python Data Structures (List, Dictionary, Tuple)

# Exercise 1: Student Grades Analysis
import numpy as np

students = {
"Alice": [85, 78, 92],
"Bob": [79, 74, 81],
"Charlie": [91, 82, 85],
"David": [76, 85, 83],
"Eve": [88, 79, 92]
}
avg = 0
for k,v in students.items():
    avg = np.average(v)
    print(f"EX:1 TASK 1: the average grade of {k} is {(avg)}")
print()

avg_list = []
n_list = []
for k,v in students.items():
    avg_list.append(np.average(v))
    n_list.append(k)

pairs = sorted(zip(avg_list, n_list)) # Sorting both lists together to guarantee the name order be according to average order.
avg_list, n_list = zip(*pairs) # unpacking the lists

avg_list = list(avg_list) # bringing back to list
n_list = list(n_list) # bringing back to list

print("sorted avg->", avg_list)
print("sorted names ->",n_list)
print()

print(f"EX:1 TASK 2: The highest grade {avg_list[4]} is from {n_list[4]} ")
print(f"EX:1 TASK 3: The lowest grade {avg_list[0]} is from {n_list[0]}")
print()
# print(n_list)
# print(avg_list)

students["Frank"] = [80,90,85]
for k,v in students.items():
    avg = np.average(v)
    print(f"EX:1 TASK 4: Student:{k}, grades:{v}")
print()

# Exercise 2: Product Inventory Management

inventory = {
"apple": (50, 0.5),
"banana": (100, 0.2),
"orange": (75, 0.3),
"pear": (20, 0.4)
}
for (k,v) in inventory.items():
    print(f"EX:2 TASK 1: key: {k}, value: {v}")
print()

# price per product:
# a_t = inventory["apple"]
# a_t = a_t[0] * a_t[1]
# print(a_t)

# list with each product price:
total = []
for t in inventory.values():
    total.append(t[0] * t [1])
print(f"EX:2 TASK 2: total per product:{total}")
print()

total = 0
for t in inventory.values():
    total += t[0] * t [1]
print("EX:2 TASK 2: Total: ",total)
print()

inventory["mango"] = (30,0.6)
inventory["banana"] = (120,0.2)
del inventory["pear"]

print("EX:2 TASKS 3, 4 AND 5: the new inventory dictionary is: ")
for k,v in inventory.items():
    print(f"key:{k}, value:{v}")
print()
# Exercise 3: Employee Records

employees = [
("John Doe", "Accounting", "john.doe@example.com"),
("Jane Smith", "Marketing", "jane.smith@example.com"),
("Emily Davis", "HR", "emily.davis@example.com"),
("Michael Brown", "IT", "michael.brown@example.com")
]
for e in employees:
    print(f"EX:3 TASK 1: employee name:{e[0]}, department:{e[1]}")
print()

email = []
name = []
first_name = []
l_name = []
for m in employees:
    email.append(m[2])
    name = m[0].split()
    first_name.append(name[0])
    l_name.append(name[1])

l_name_sort_mail = sorted(zip(l_name, email)) # Sorting both lists together to guarantee the name order be according to average order.
l_name, email = zip(*l_name_sort_mail) # unpacking the lists

l_name = list(l_name) # bringing back to list
email = list(email) # bringing back to list

for l,e in l_name_sort_mail:
    print(f"EX:3 TASK 2:{e} sorted by last name {l}")
print()

new_employee = ("David Wilson","Sales","david.wilson@example.com")
employees.append(new_employee)
for n_e in employees:
    print(f"EX:3 TASK 3: updated list {n_e}")
print()

for e in employees:
    if e[0] == "Jane Smith":
        print(f"EX:3 TASK 4:  Jane Smith's department is {e[1]}")
print()

# Exercise 4: Book Library System

library = {
"978-3-16-148410-0": {"title": "The Catcher in the Rye","author": "J.D. Salinger", "year": 1951},
"978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
"978-0-7432-7356-5": {"title": "To Kill a Mockingbird","author": "Harper Lee", "year": 1960},
"978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}
g_o = ""
for tt,a in library.items():
    print(f"EX 4: TASK 1:ISBN {tt}\n{a}")
    if tt == "978-0-14-028329-7":
        g_o = a
print()

print(f"EX 4: TASK 2: Book ISBN 978-0-14-028329-7:\n{g_o}")
print()

library["978-1-4028-9462-6"] = {"title": "The Great Gatsby","author": "F.Scott Fitzgerald", "year": 1925}

for tt, a in library.items():
    print(f"EX 4: TASK 3:ISBN {tt}\n{a}")
print()

library["978-0-7432-7356-5"] = {"title": "To Kill a Mockingbird","author": "Harper Lee", "year": 1961}

for tt,a in library.items():
    print(f"EX 4: TASK 4:ISBN {tt}\n{a}")
print()

del library["978-0-452-28423-4"]

for tt,a in library.items():
    print(f"EX 4: TASK 5:ISBN {tt}\n{a}")
print()

# Exercise 5: City Population Data

cities = {
"New York": 8419000,
"Los Angeles": 3980000,
"Chicago": 2716000,
"Houston": 2328000,
"Phoenix": 1690000
}

for c,p in cities.items():
    print(f"EX 5: TASK 1:The population of {c} is {p}")
print()

max_pop = 0
min_pop = 0
c_l = []
p_l = []
for c,p in cities.items():
    max_pop = np.max(p)
    min_pop = np.min(p)
    c_l.append(c)
    p_l.append(p)

pairs = sorted(zip(p_l, c_l)) # Sorting both lists together to guarantee the name order be according to average order.
p_l, c_l = zip(*pairs) # unpacking the lists

p_l = list(p_l) # bringing back to list
c_l = list(c_l) # bringing back to list

print(f"EX:5 TASK 2: The highest population {p_l[4]} is from {c_l[4]} ")
print(f"EX:5 TASK 3: The lowest population {p_l[0]} is from {c_l[0]}")
print()

cities["Phoenix"] = (1700000)

for c,p in cities.items():
    print(f"EX 5: TASK 4:The population of {c} is {p}")
print()

cities["San Francisco"] = (884000)

for c,p in cities.items():
    print(f"EX 5: TASK 5:The population of {c} is {p}")
print()
# Exercise 6: Movie Database

movies = {

"Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
"The Godfather": {"year": 1972, "rating": 9.2, "genre":"Crime"},
"The Dark Knight": {"year": 2008, "rating": 9.0, "genre":"Action"},
"Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
"Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}

for t,d in movies.items():
    print(f"EX 6: TASK 1: {t}:\n{d}")
print()


movie_name = []
rate = []
for m,d in movies.items():
    movie_name.append(m)
    rate.append(d["rating"])

print("movies names:",movie_name)
print("movies rate",rate)
print()

movie_name_sort_rate = sorted(zip(movie_name,rate)) # Sorting both lists together to guarantee the name order be according to average order.
rate, movie_name = zip(*movie_name_sort_rate) # unpacking the lists

rate = list(rate) # bringing back to list
movie_name = list(movie_name) # bringing back to list

# for r,mn in movie_name_sort_rate:
print(f"EX:6 TASK 2:{rate[4]} is the movie with the highest rate of {movie_name[4]}")
print(f"EX:6 TASK 2:{rate[0]} is the movie with the lowest rate of {movie_name[0]}")
print()

movies["The Matrix"] = {"year":1999,"rating":8.7,"genre":"Sci-Fi"}

for t,d in movies.items():
    print(f"EX 6: TASK 3: {t}:\n{d}")
print()

movies["Inception"] = {"year": 2010, "rating": 9.0, "genre": "Sci-Fi"}
del movies["Pulp Fiction"]

for t,d in movies.items():
    print(f"EX 6: TASK 3,4 & 5: {t}:\n{d}")
print()
# Exercise 7: Country Capitals

countries = {
"USA": "Washington, D.C.",
"Canada": "Ottawa",
"France": "Paris",
"Germany": "Berlin",
"Japan": "Tokyo"
}

for co,cap in countries.items():
    print(f"EX 7: TASK 1:\n Country:{co}\n Capital:{cap}")
print()

for co,cap in countries.items():
    if co == "Germany":
        print(f"EX 7: TASK 2: The capital of Germany is: {cap}")
print()

countries["Australia"] = ("Caberra")

for co,cap in countries.items():
    print(f"EX 7: TASK 3:\n Country:{co}\n Capital:{cap}")
print()

countries["USA"] = ("New Washington")
for co,cap in countries.items():
    print(f"EX 7: TASK 4:\n Country:{co}\n Capital:{cap}")
print()

del countries["France"]

for co,cap in countries.items():
    print(f"EX 7: TASK 5:\n Country:{co}\n Capital:{cap}")
print()
# Exercise 8: Shopping Cart

cart = [
{"item": "apple", "quantity": 3, "price_per_unit": 0.5},
{"item": "banana", "quantity": 6, "price_per_unit": 0.2},
{"item": "orange", "quantity": 4, "price_per_unit": 0.3},
{"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]

q = []
p_u = []
for it in cart:
    q.append(it["quantity"])
    p_u.append(it["price_per_unit"])
    print(f"EX 8: TASK 1:\n{it}")
print()

q_array = np.array(q)
p_u_array = np.array(p_u)
ppp = q_array * p_u_array
print("mult", ppp)
print()

total_cost = sum(ppp)

print(f"EX 8: TASK 2:The total cost of the cart is {total_cost}$")
print()

new_item = {"item": "grape", "quantity": 5 ,"Price_per_unit":0.6}
cart.append(new_item)

q = []
p_u = []
for it in cart:
    print(f"EX 8: TASK 3:\n{it}")
print()

cart[1] = {"item": "banana", "quantity": 10, "price_per_unit": 0.2}

for i in cart:
    print(f"EX 8: TASK 4:The updated list is:\n{i}")
print()
del cart[3]

for i in cart:
    print(f"EX 8: TASK 5:The updated list is:\n{i}")
print()

# Exercise 9: Weather Data

weather = {
"Monday": {"temperature": 20, "humidity": 60},
"Tuesday": {"temperature": 22, "humidity": 55},
"Wednesday": {"temperature": 19, "humidity": 65},
"Thursday": {"temperature": 23, "humidity": 50},
"Friday": {"temperature": 21, "humidity": 70}
}

for wd,d in weather.items():
    print(f"EX 9: TASK 1: {wd} {d}")
print()

week_day = []
temp = []
for wd,d in weather.items():
    week_day.append(wd)
    temp.append(d["temperature"])

day_based_temp = sorted(zip(temp,week_day))
temp, week_day = zip(*day_based_temp)

temp = list(temp)
week_day = list(week_day)

print(f"EX 9: TASK 2: The highest temperature of {temp[4]}C was on {week_day[4]}")
print(f"EX 9: TASK 3: The lowest temperature of {temp[0]}C was on {week_day[0]}")
print()

weather["Wednesday"] = {"temperature": 25, "humidity": 65}
for wd,d in weather.items():
    print(f"EX 9: TASK 4: {wd} {d}")
print()

weather["saturday"] = {"temperature": 24, "humidity": 60}
for wd,d in weather.items():
    print(f"EX 9: TASK 5: {wd} {d}")
print()

# Exercise 10: Library Members

members = [
{"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
{"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
{"name": "Charlie", "age": 22, "books_borrowed": ["BraveNew World", "1984"]},
{"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
]

for m in members:
    print(f"EX 10: TASK 1: Member name:{m["name"]}, member age:{m["age"]}")
print()

for b in members:
    if b["name"] == "Charlie":
        print("EX 10: TASK 2: The books borrowed by Charlie:\n",b["books_borrowed"])
print()

new_member = {"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]}
members.append(new_member)

members[1] = {"name": "Bob", "age": 31, "books_borrowed": ["BraveNew World", "1984"]}

for m in members:
    print(f"EX 10: TASK 3 & 4: Member name:{m["name"]}, member age:{m["age"]}")
print()

del members[3]

for m in members:
    print(f"EX 10: TASK 5: Member name:{m["name"]}, member age:{m["age"]}")
print()

# REFERENCES -
# https://blog.finxter.com/5-best-ways-to-perform-calculations-with-dictionaries-in-python/
# https://www.w3schools.com/python/ref_func_sorted.asp
