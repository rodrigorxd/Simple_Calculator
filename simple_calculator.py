#Simple_Calculator_Rodrigo
#02/24/2022
#Introduction

print("-----Simple Calculator-----")

#Input

num1 = int(input("Type a number:"))
sign = input("Type the operation sign:")
num2 = int(input("Type a number:"))

#Decision taking structure

if sign == '+':
    print("The result is: ", num1 + num2)
if sign == '-':
    print("The result is:", num1 - num2)
if sign == '*':
    print("The result is:", num1 * num2)
if sign == "/":
    print("The result is", num1 / num2)
