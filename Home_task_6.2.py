
number = input("Enter a number from 0 to 8640000: ")
if  not number.isdigit():
    print(False, 'Print only numbers')
    exit()
if int(number) > 8640000:
    print(False, 'print number from 0 to 8640000')
    exit()

number = int(number)

day = int(number) // 86400
count_leftovers = number % 86400
hours = count_leftovers // 3600
minutes = (count_leftovers % 3600) // 60
seconds = count_leftovers % 60

# formated_days = str(day).zfill(2)
# formated_hours = str(hours).zfill(2)
# formated_minutes = str(minutes).zfill(2)
# formated_seconds = str(seconds).zfill(2)
#

formated_days = f'{day:02}'
formated_hours = f'{hours:02}'
formated_minutes = f'{minutes:02}'
formated_seconds = f'{seconds:02}'

result = f'{formated_days} days {formated_hours}:{formated_minutes}:{formated_seconds}'
print(result)