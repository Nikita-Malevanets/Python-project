import string
import keyword
new_lyst_punctuation = string.punctuation.replace('_','')

checking = str(input("Enter checking word "))
if checking [0].isdigit():
    print(False)
elif any(letter.isupper() for letter in checking):
    print(False)
elif any(letter in new_lyst_punctuation or letter == ' ' for letter in checking):
    print(False)
elif keyword.iskeyword(checking):
    print(False)
elif checking.count('_') > 1:
    print(False)
else:
    print(True)