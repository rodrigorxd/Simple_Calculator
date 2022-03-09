#Simple_Calculator_Rodrigo
#02/24/2022
#Introduction

print("-----Simple Calculator-----")

#Input

print("\n 1 - + \n 2 - - \n 3 - * \n 4 - / \n 5 - ^ \n 6 - % \n 7 - Root \n 8 - Bhaskara's \n \n Choose an operation:")
sign = int(input())
print("Example: First Number(a), Second Number(b) = a(radicand), b(index)")
num1 = float(input("Type the first number:"))
num2 = float(input("Type the second number:"))

#Decision taking structure (bhaskara) + calculating delta

if sign == 8:
    if num1 == 0:
        print("Invalid.")
    else :
        num3 = float(input("Type the third number:"))
        delta = float(((num2) ** 2) - (4 * (num1 * num3)))

#Delta < 0 - No real roots

#Root - when index is even, radicand can't be negative

#Operation choice should be between 1 and 8

choice = sign <= 8 and sign >= 1

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
        if num2 % 2 == 0 and num1 < 0:
            print("Invalid.")
        else:
            print("The result is:", num1 ** (1 / num2))
    if sign == 8:
        if delta < 0 and delta != 0:
            print("No real roots.")
        else :
            print("The result is: ", ((-num2) + (delta) ** (1/2)) / (2 * num1))
            print("The result is: ", ((-num2) - (delta) ** (1/2)) / (2 * num1))
else :
    print("Invalid operation choice.")

