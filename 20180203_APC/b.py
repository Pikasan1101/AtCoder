# AC
import math
n = input()
a = map(int, raw_input().split())
b = map(int, raw_input().split())
c = 0
for i, j in zip(a, b):
    if i < j:
        c += math.ceil(1.0*(j-i)/2)
if c > sum(b)-sum(a):
    print "No"
else:
    print "Yes"
