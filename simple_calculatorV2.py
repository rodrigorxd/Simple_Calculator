#Simple_Calculator_Rodrigo
#02/24/2022
#Introduction

print("-----Simple Calculator-----")

#Input

num1 = int(input("Type a number:"))
print("\n 1 - + \n 2 - - \n 3 - * \n 4 - / \n 5 - ^ \n 6 - % \n \n Choose an operation:")
sign = int(input())
num2 = int(input("Type a number:"))

#Operation choice should be between 1 and 6

choice = sign <= 6 and sign >= 1

#Decision taking structure

if choice == True :
    if sign == 1 :
        print("The result is:", num1 + num2)
    if sign == 2 :
        print("The result is:", num1 - num2)
    if sign == 3 :
        print("The result is:", num1 * num2)
    if sign == 4 :
        if num2 == 0:
            print("Invalid.")
        else :
            print("The result is:", num1 / num2)
    if sign == 5:
        print("The result is:", num1 ** num2)
    if sign == 6:
        print("The result is:", ((num1)/(100)) * (num2))
else :
    print("Invalid.")

