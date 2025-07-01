
number = input('Enter your number:   ')

while int(number) > 9:
    result = 1
    for element in number:
        result = result * int(element)
    number = str(result)


print(number)

