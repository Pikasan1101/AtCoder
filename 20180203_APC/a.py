# AC
import sys
x, y = map(int, raw_input().split())
if x == y:
    print -1
    sys.exit()
for i in xrange(x, x*y, x):
    if not i % y == 0:
        print i
        break
else:
    print -1
