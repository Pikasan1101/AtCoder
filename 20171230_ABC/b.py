# AC
import sys
a, b = map(int, raw_input().split())
s = raw_input()
num = [str(i) for i in xrange(10)]
for i in xrange(a):
    if not s[i] in num:
        print "No"
        sys.exit()

if not s[i+1] == "-":
    print "No"
    sys.exit()

for i in xrange(b):
    if not s[i+a+1] in num:
        print "No"
        sys.exit()

print "Yes"

