
def first_word(text: str) -> str:
    words = text.replace(',',' ' ).replace('.',' ').split()
    for word in words:
        clean_word = ''.join(char for char in word if char.isalpha() or char == "'")
        if clean_word:
            return clean_word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')