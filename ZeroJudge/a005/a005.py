import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    nums = list(map(int, line.split()))
    if len(nums) == 1:
        continue
    a, b, c, d = nums
    if b - a == c - b:
        diff = b - a     
        e = d + diff  
    else:
        ratio = b // a   
        e = d * ratio   
    print(f"{a} {b} {c} {d} {e}")
