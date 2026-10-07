import math
print("Calculator app!!")
number1 = float(input("Enter a number: "))
MathOperator = input("Enter an operator (+, -, *, /, ^, root): ")
if MathOperator == "root":
    if number1 < 0:
        print("Error")
    else:
     print(math.sqrt(number1))
    exit()
number2 = float(input("Enter another number: "))

match MathOperator:
    case "+":
        print(number1 + number2)
    case "-":
        print(number1 - number2)
    case "*":
        print(number1 * number2)
    case "/":
        print(number1 / number2)
    case "^":
        print(number1 ** number2)
    case "root":
        print(math.sqrt(number1))
    case _:
        print("Invalid operator")