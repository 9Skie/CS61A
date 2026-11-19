num1 = float(input("Enter a number: "))
sign = input("Enter a sign: ")
num2 = float(input("Enter a second number: "))

if sign == "+":
    operation = num1 + num2
elif sign == "-":
    operation = num1 - num2
elif sign == "*":
    operation = num1 * num2
elif sign == "/":
    operation = num1 / num2
else:
    print("The sign is invald, please redo the operation") + exit()

print("The answer is: " + str(operation))
