# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:27:03 2016

@author: crow
"""
t = open('text.file', 'r')
text_x = t.read()
abc = (
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L',
    'l',
    'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
    'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', ' ', '-', '!',
    '?',
    '.', ',', ';', ':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)
abc_x = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', ' ', '-', '!', '?', '.', ',', ';', ':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)
key = raw_input('Введіть ключ=')
dlstr = len(text_x)
dlabc = len(abc)
dlkey = len(key)
i = 0
int_key = []
shfr_numb = []
shyfr = []
j = 0
d = 0
print text_x[16:18]
print key
while i < dlkey:
    while key[i] != abc[j] and key[i] != abc[j + 1] and j < 52:
        d += 1
        j += 2
    while key[i] != abc[j] and j > 51 and j <= dlabc:
        d += 1
        j += 1
    int_key.append(d)
    j = 0
    d = 0
    i += 1
print int_key
i = 0
d = 0
g = 0
while i < dlstr:
    while text_x[i] != abc[j] and text_x[i] != abc[j + 1] and j < 52:
        d += 1
        j += 2
    while text_x[i] != abc[j] and j > 51:
        d += 1
        j += 1
        if j == dlabc:
            break
    g = i % dlkey
    x = (int_key[g] + d) % 44
    a = abc_x[x]
    shyfr.append(a)
    j = 0
    d = 0
    i += 1
    g += 1
    print i
print shfr_numb[0:10]
f = open('shyfr', 'w')
f.writelines(shyfr)
f.close()
