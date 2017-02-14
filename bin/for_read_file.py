#for line in open('4lines.file'):
#    print(line.upper(), end='')

# L = (1, 2, 3)
#I = iter(L)
#while True:
#    try:
#        X = next(I)
#    except StopIteration:
#        break
#    print (X ** 2, end=' ')

# R = [ x + 10 for x in L ]
# print (R)



line = [ line.rstrip() for line in open('4lines.file')]
print(line)




