import random

selected_list = []
population = int(input("Please input the number of entire population: "))
surveyed_amount = int(input("Please input the amount wished to be surveyed: "))

while surveyed_amount > 0:
    surveyed_amount = surveyed_amount - 1
    selected_number = random.randint(1, population)
    if selected_number in selected_list:
        surveyed_amount = surveyed_amount + 1
    else:
        selected_list.append(selected_number)


# I need to test it somehow so there wont be any repeats

print("The individuals selected have the numbers " + str(selected_list))
