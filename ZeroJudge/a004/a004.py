import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    year = int(line)
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("閏年")
    else:
        print("平年")
