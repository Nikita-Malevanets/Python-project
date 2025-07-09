def is_palindrome(text):
    text = text.lower()
    compare_text = ''.join(element for element in text if element.isalnum())
    reversed_text = compare_text[::-1]
    return reversed_text == compare_text

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")