#                                  LAB_2 - PART_2 -> Star Drawings with Nested Loops
# ______________________________________________________________________________________________________________________
# PATTERN - 1
# with googles help
n = 7                              # number of rows
o = 2 * n - 2                      # variable to calculate the white spaces, it makes the triangle move.

for m in range(1,n+1):             # positioning the number of rows / determine the number of * for each line.

    for opp_tri in range(o):       # create the white spaces to move the top of the triangle, it reduces each row spaces.
        print(end=" ")             # displays the space to align the *.
    o = o - 2                      # calculate the variable to reduce the white spaces for each line in every loop round.
    for opp_tri in range (0, m-1): # creates the first half of the triangle, from zero until the end of the loop
        print("*", end=" ")        # prints a * and a space for each loop round.
    for tri in range(0, m):        # create the second half of the triangle based on each element of the first for loop.
        print("*", end=" ")        # displays the * with spaces.
    print()                        # this print makes sure that all loops will be in the right position.

print()

'''
    Wasn't possible to do this one without look on google some parts, I had no idea how to create white spaces, but now 
    I have a little knowledge about how to do it. To really understand and dominate the technique, I'll need to do it 
    repeatedly.
'''
# ______________________________________________________________________________________________________________________
# PATTERN - 2

n = 7

for l1 in range(0,n): # Range that determine how many rows the draw is going to have
    print()           # I realize that wasn't necessary to insert any space or *.
    for l2 in range(l1, n): #
        print("*",end=" ")


'''
 My process to figure it out how to do it was initializing the construction of a simple 
 list of numbers made by a for loop, then visualizing the draw as a sequence of a list of numbers
 was possible to start changing the ranges for each loop and its respective prints.
'''
# ______________________________________________________________________________________________________________________
# PATTERN - 3
# Method 02 - with googles help
print()
print()
n = 7

for s in range(0,n - 3):
    for t1 in range (0,s + 1):
        print("*", end=" ")
    print("")

for i_t in range(n - 4, 0, -1):
    for t2 in range (0, i_t):
        print("*",end=" ")
    print()
# ______________________________________________________________________________________________________________________
# Method 01 - by myself
n = 7
for i in range(0, n - 3):
    for j in range(0, i):
        print("*", end=" ")
    print()

for i in range(3, n):
    for j in range(i, n):
        print("*", end=" ")
    print()

'''
     My process to figure it out how to do it was thinking about 2 different triangles. Doing this I was able to
     visualize the example of nested loop in the "starry.py" file and replicate the first one. The second triangle
     wasn't as simple as I imagine, even though I used the second pattern, to combine them I needed to spend some hours.
     
     Before it, I needed to look on google how to do it.
     https://www.geeksforgeeks.org/python-nested-loops/
     In this site, no success, I understand a more about nested loop, what was actually good, but didn't helped me to
     solve the problem.
     https://pynative.com/python-nested-loops/
     I looked this other page, and I helped even more than the other one, and during the reading I found:
     https://pynative.com/print-pattern-python-examples/
     Which was the one that make me realize that without seeing it, I would possibly just understand how to complete all
     patterns in much more days.
     
     I take care to don't just copy, but to understand what each part of the code is responsible for.
      
'''


