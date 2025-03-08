# 7. Write a loop to print every second character in the string "looping".

pl = "paralelepipedo"
pl_2 = []
pla_lt = []
for l in range(1,len(pl),2):
    pl_2.append(l)
    pla_lt += pl[l]
# range( 1 means -> where in the range of the string do you want to begin
# range( 1, len(pl) means -> Where in the range I would like to stop, in this case it will stop after the full size of the string length
# range(1,len(pl),2 means -> the steps I want to give in the string, but it is optional, (2 means every second element)
print(pla_lt)
print(pl_2)
# I'm printing only the unique elements of the string that is obeying the for loop rule (range(1,len(pl),2)

# _________________________________________________________________________________________________________________________________________
# print every third
aa = "rice chicken and eggs"

for a in range(2,len(aa),3):
    print(aa[a])

# _________________________________________________________________________________________________________________________________________


