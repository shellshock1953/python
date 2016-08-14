import string
text = open('text.file').read().lower()
result = {}
for letter in string.printable.lower():
    result[letter] = 0
for letter in text:
    if letter.lower() not in result:
        result[letter] = 1
    else:
        result[letter] += 1
print result

