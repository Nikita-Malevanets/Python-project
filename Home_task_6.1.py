import string


letters = str(input('Write your letters, use " - " between:  '))
first_letter = letters[0]
second_letter = letters[2]

start_index = string.ascii_letters.index(first_letter)
end_index = string.ascii_letters.index(second_letter)
range_letters = string.ascii_letters[start_index:end_index +1]

print(range_letters)