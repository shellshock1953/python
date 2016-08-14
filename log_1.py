import sys

for raw_line in open(sys.argv[1],'r'):
    line = raw_line.split()
    date, time, level, message = line[:1], line[2], line[3], line[3:]
    print(date)
