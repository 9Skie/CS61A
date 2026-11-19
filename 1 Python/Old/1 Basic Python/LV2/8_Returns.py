def caculation(num):
    times_five = num * 5
    return times_five


print("This is a program that multiplies your number by 5 ")
number = int(input("Insert a number: "))

result = caculation(number)
print("The result is " + str(result))
