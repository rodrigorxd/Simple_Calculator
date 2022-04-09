#simple_calculator_V4
#03/24/2022

print("-----Simple Calculator-----")
print("Ex:Type 0.xx (decimal) instead of 1/x (fraction).")
print("First number (a), Second number (b), Third number (c)")
print("\n 1 - +\n 2 - -\n 3 - *\n 4 - /\n 5 - ^\n 6 - % (a/100 * b = x)\n 7 - Root (a ^ 1/b)\n 8 - Bhaskara's\n 9 - Area\n \n Choose an operation:")

operation = int(input())

#input if else structure- calculate if else structure - print

if operation < 1 or operation > 9:
print("Invalid choice.")
else:
if operation <= 7:
    number1 = float(input("Type the first number:"))
    number2 = float(input("Type the second number:"))
else:
    if operation == 8:
        print("axˆ2 + bx + c = 0")
        number1 = float(input("Type the first number:"))
        number2 = float(input("Type the second number:"))
        number3 = float(input("Type the third number:"))
    else:
        if operation == 9:
            print("\n 1 - Square/Rectangle\n 2 - Parallelogram\n 3 - Triangle\n 4 - Circle\n 5 - Trapezium:")
            geometric = int(input("Choose a geometric shape:"))
            if geometric < 1 or geometric > 5:
                print("Invalid choice.")
            else:
                if geometric <= 2:
                    side1 = float(input("Type the first side:"))
                    side2 = float(input("Type the other side:"))
                else:
                    if geometric == 3:
                        base = float(input("Type the base:"))
                        height = float(input("Type the height:"))
                    else:
                        if geometric == 4:
                            radius = float(input("Type the radius:"))
                        else:
                            minor_base = float(input("Type the minor base:"))
                            major_base = float(input("Type the major base:"))
                            height = float(input("Type the height:"))
if operation == 1:
    total = number1 + number2
else:
    if operation == 2:
        total = number1 - number2
    else:
        if operation == 3:
            total = number1 * number2
        else:
            if operation == 4:
                if number2 == 0:
                    print("Invalid, divison by zero.")
                else:
                    total = number1 / number2
                    print(f"Result:{total}")
            else:
                if operation == 5:
                    total = number1 ** number2
                else:
                    if operation == 6:
                        total = (number1/100) * number2
                    else:
                        if operation == 7:
                            if number2 == 0:
                                print("Invalid.")
                            else:
                                if number2 % 2 == 0 and number1 < 0:
                                    print("Invalid.")
                                else:
                                    total = number1 ** (1/number2)
                                    print(f"Result: {total}")
                        else:
                            if operation == 8:
                                if number1 == 0:
                                    print("Invalid, (a) can't be zero.")
                                else:
                                    delta = (number2 ** 2) - (4 * number1 * number3)
                                    if delta < 0:
                                        print("No real roots.")
                                    else:
                                        total1 = (-number2 + (delta ** (1 / 2))) / (2 * number1)
                                        total2 = (-number2 - (delta ** (1 / 2))) / (2 * number1)
                                        print(f"Results :\n {total1}\n {total2}")
                            else:
                                if geometric < 1 or geometric > 5:
                                    print("!")
                                else:
                                    if geometric <= 2:
                                        total = side1 * side2
                                    else:
                                        if geometric == 3:
                                            total = (base * height) / 2
                                        else:
                                            if geometric == 4:
                                                total = (radius ** 2) * 3.14
                                            else:
                                                total = ((minor_base + major_base) * height) / 2
                                print(f"Result: {total}")
if operation <= 3:
    print(f"Result: {total}")
else:
    if operation > 4 and operation <= 6:
        print(f"Result: {total}")
