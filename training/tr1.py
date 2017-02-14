raw_file = open('Sat','r')
from_file = raw_file.readlines()
to_file = []
for setnumber in [0, 1, 2]:
    current_line = from_file[setnumber]
    if setnumber == 0:
       current_line = current_line[:-1]
    else:
       current_line = current_line[:-2]
    current_set = current_line.split(' ')
    print (current_set)
    setname = current_set[0]
    to_file.append(setname)
    print (setname)
    for i in [1, 2, 3]:
	if i = 1: current_set = current_set[1:]
        exrersize = current_set[i]
        print (exrersize)
        to_file.append(int(exrersize) + 1)
    to_file.append('\n')
print (to_file)
raw_file.close()
str_to_file = ' '.join((str(e) for e in to_file))
output = open('Sat','w')
print (str_to_file, file=output)
#print (to_file[0], file=output)  
# output.write(str(to_file).format())
# output.close()



