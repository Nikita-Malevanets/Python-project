def popular_words (text, words):
    text = text.lower().split()
    count_words = {}
    for word in words:
        count_words[word] = text.count(word)
    return count_words

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
