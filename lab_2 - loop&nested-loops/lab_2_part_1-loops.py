# LAB_2_LOOPS
# Part 1: Mod and Integer Division
number = int(input("insert a number: "))
n = int(input("Inform which position do you want to see: "))
n_print = ()
for i in range(number):
    n_print = (number // (10 ** (n-1)) % 10) # equation user for the "coma walking" from the right to the left.
print(n_print)

# ________________________________________________________________________


