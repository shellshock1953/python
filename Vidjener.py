import string

alphabet = []
crypt = []
text_file = open('text.file').read().lower()
key_int = []
# key = raw_input('Enter KEY:')
key = 'c'
for letter in string.printable.lower():  # making alphabet
    alphabet.append(letter)

for char in key:  # convert char key into int key
    if char in alphabet:
        key_int.append(alphabet.index(char))
# print 'int key is %s' % key_int
i = 0
for letter in text_file:  # input_text[char + key]
    if letter not in alphabet:
        continue
    crypt.append(alphabet[(alphabet.index(letter) + key_int[i % len(key)]) % len(alphabet)])
    i += 1
# crypted_file = open('crypt_file.txt', 'w')
# crypted_file.writelines(map(str, crypt))
# crypted_file.close()
print map(list, crypt)