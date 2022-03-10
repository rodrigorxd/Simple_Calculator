#Simple_Calculator_Rodrigo
#02/24/2022
#Introduction

print("-----Simple Calculator-----")
print("Ex:Type 0.xx (decimal) instead of 1/x (fraction).")
print("First number (a), Second number (b).")

#Input

print("\n 1 - +\n 2 - -\n 3 - *\n 4 - /\n 5 - ^\n 6 - % (a/100 * b = x)\n 7 - Root (a ^ 1/b)\n 8 - Bhaskara's\n \n Choose an operation:")
sign = int(input())
print("Example: First Number(a), Second Number(b) = a(radicand), b(index)")
num1 = float(input("Type the first number:"))
num2 = float(input("Type the second number:"))

#Operation choice should be between 1 and 8

choice = sign <= 8 and sign >= 1

#Decision taking structure (bhaskara) + calculating delta, first number typed (a), can't be 0

#Delta < 0 - No real roots

#Root - when index is even, radicand can't be negative and index can't be 0

#Decision taking structure

if choice == True :
    if sign == 1:
        print("The result is:", num1 + num2)
    if sign == 2:
        print("The result is:", num1 - num2)
    if sign == 3:
        print("The result is:", num1 * num2)
    if sign == 4:
        if num2 == 0:
            print("Invalid.")
        else :
            print("The result is:", num1 / num2)
    if sign == 5:
        print("The result is:", num1 ** num2)
    if sign == 6:
        print("The result is:", ((num1)/(100)) * (num2))
    if sign == 7:
        if num2 == 0:
            print("Index can't be 0.")
        else:
            if num2 % 2 == 0 and num1 < 0:
                print("Invalid.")
            else:
                print("The result is:", num1 ** (1 / num2))
    if sign == 8:
        num3 = float(input("Type the third number:"))
        delta = float(((num2) ** 2) - (4 * (num1 * num3)))
        if num1 == 0:
            print("First number typed = 0. Invalid!")
        else:
            if delta < 0 :
                print("No real roots.")
            else :
                print("The result is: ", ((-num2) + (delta) ** (1/2)) / (2 * num1))
                print("The result is: ", ((-num2) - (delta) ** (1/2)) / (2 * num1))
else :
    print("Invalid operation choice.")

