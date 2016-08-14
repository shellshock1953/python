import time

day = time.strftime("%a")
print day
from_file = open('Sat', 'r')

agenda = {}
to_file = []
for line in from_file.readlines():
    key, value_str = line.split(None, 1)
    value = str(value_str)
    agenda[key] = value.split()
    print line
print agenda

newitems = []
for set_turple in agenda.items():
    current_set = list(set_turple)
    for todo in current_set[1]:
        print todo
        newitems.append(int(todo) + 1)
    print newitems
    current_set[1] = newitems
    newitems = []
    to_file.append(current_set)

