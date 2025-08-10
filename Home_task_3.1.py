number1 = float(input("Enter number#1  "))
number2 = float(input("Enter number#2  "))
operation = input("Enter arithmetic operation (+, -, *, / ): ")
yes = 'y'
no = 'n'

if operation == '-':
    result = number1 - number2
    print("result: ", number1 - number2)
if operation == '+':
    print ( "result: ", number1 + number2)
if operation == '*':
    print ( "result: ", number1 * number2)
if operation == '/':
    if number2 == 0:
        print ( "ERROR! You cannot divide by 0.")
    else:
        print ( "result: ", number1 / number2)