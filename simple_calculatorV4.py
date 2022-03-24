#simple_calculator_v4
#03/24/2022
#menu

print("-----Simple Calculator-----")
print("Ex:Type 0.xx (decimal) instead of 1/x (fraction).")
print("First number (a), Second number (b).")
print("\n 1 - +\n 2 - -\n 3 - *\n 4 - /\n 5 - ^\n 6 - % (a/100 * b = x)\n 7 - Root (a ^ 1/b)\n 8 - Bhaskara's\n 9 - Area\n \n Choose an operation:")

operation = int(input())

#geometric shape choice

if operation == 9:
    print("\n 1 - Square/Rectangle\n 2 - Parallelogram\n 3 - Triangle\n 4 - Circle\n 5 - Trapezium:")
    geometric = int(input("Choose a number:"))


#numbers input

if operation < 1 or operation > 9:
    print("Invalid operation!")
else:
    if operation <= 7:
        num1 = float(input("Type the first number:"))
        num2 = float(input("Type the second number:"))
    else:
        if operation == 8:
            num1 = float(input("Type the first number (a):"))
            num2 = float(input("Type the second number (b):"))
            num3 = float(input("Type the third number (c):"))
        else:
            if geometric < 1 or geometric > 5:
                print("Invalid choice.")
            else:
                if geometric >= 1 and geometric <= 3:
                    side1 = float(input("Type the side/base:"))
                    side2 = float(input("Type the side/height:"))
                else:
                    if geometric == 4:
                        radius = float(input("Radius:"))
                    else:
                        minor_base = float(input("Minor base:"))
                        major_base = float(input("Major base:"))
                        height = float(input("Height:"))

#result based on operation choice

if operation == 1:
    total = num1 + num2
else:
    if operation == 2:
        total = num1 - num2
    else:
        if operation == 3:
            total = num1 * num2
        else:
            if operation == 4:
                if num2 != 0:
                    total = num1 / num2
                else:
                    print("Invalid.")
if operation == 5:
    total = num1 ** num2
else:
    if operation == 6:
        total = (num1 / 100) * num2
    else:
        if operation == 7:
            if num2 == 0:
                print("Index can't be 0.")
            else:
                if num2 % 2 == 0 and num1 < 0:
                    print("Invalid.")
                else:
                    total = num1 ** (1 / num2)
                    print(f"Result = {total}")
if operation == 8:
    delta = ((num2) ** 2) - (4 * (num1 * num3))
    if num1 == 0:
        print("First number (a) can't be zero.")
    else:
        if delta < 0:
            print("No real roots.")
        else:
            total1 = ((-num2) + ((delta) ** (1/2))) / (2 * num1)
            total2 = ((-num2) - ((delta) ** (1/2))) / (2 * num1)
            print(f"Result: {total1} , {total2}")

if operation == 9:
    if geometric >= 1 and geometric <= 5:
        if geometric <= 2:
            total = side1 * side2
        else:
            if geometric == 3:
                total = (side1 * side2) / 2
            else:
                if geometric == 4:
                    total = radius * 3.14
                else:
                    total = ((minor_base + major_base) * height) / 2

if operation >= 1 and operation <= 6 or operation == 9:
    if operation == 4:
        if num2 != 0:
            print(f"Result = {total}")
    else:
        print(f"Result = {total}")




























