import time
day = time.strftime("%a")
today = open(day).read().split(' ')
output = open(day, 'w')
for current in range(12):
    if current % 4 == 0:
        input()
        print('SET:', today[current])
        print(today[current], end =' ', file=output)
        continue
    print(' current', today[current])
    input()
    for sec in range(5):
        print('     ', sec)
        time.sleep(1)
    print(int(today[current]) + 1, end=' ', file=output)
    if current % 4 == 0:
        print('Set complete')
print('Well done!')
