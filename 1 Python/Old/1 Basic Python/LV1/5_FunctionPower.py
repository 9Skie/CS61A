# this should make you have a number to any power, positive or negative regardless, and 0

from fractions import Fraction

def raise_to_power(base_num, power_num):
    result = 1
    if power_num > 0:
        for index in range(power_num):
            result = result * base_num
        return result
    elif power_num == 0:
        return result
    elif power_num < 0:
        for index in range(-power_num):
            result = result * Fraction(1, base_num)
        return result
    else:
        pass


print("This is a program that makes the number you input to any whole power you wish!")

num = int(input("Please enter your number: "))
power = int(input("Please enter your power: "))

answer = raise_to_power(num, power)
print("\nThe answer is " + str(answer))
