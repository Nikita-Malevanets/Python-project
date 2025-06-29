
while True:
    number1 = float(input("Enter number#1  "))
    number2 = float(input("Enter number#2  "))
    operation = input("Enter arithmetic operation (+, -, *, / ): ")

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

    choice = input("Would you like to continue (y/n)? ")
    if choice == 'y':
        continue
    elif choice == 'n':
        break
    else:
        print("That is not a valid choice.")
        break