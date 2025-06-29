import string

enter = str(input("Wright yours text (max 140 characters)     "))
enter = enter.title()
delete = string.punctuation + " "
result = ""
for character in enter:
    if character not in delete:
        result += character
if len(result) > 140:
    result = result[:140]
print('#' + result)
