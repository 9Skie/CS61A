Classmates = ["Frank", "Tiffany", "William", "Criss"]

# in this case, the length of the array "Classmates" is 4, there are 4 elements inside of the array
# so in the for loop below, range(len(Classmates)) = range(4), Classmate[0，1，2，3] will be printed out, 4 isn''t included
# right now, we are using the for statement to check all the elements inside of the list

for name in range(len(Classmates)):
    print(name + 1, Classmates[name])
    if name < 2:
        print("cool\n")
    else:
        print("friend, maybe\n")

