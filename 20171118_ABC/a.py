import sys
num = list(raw_input())
p  = num[0]
c = 1
for i in xrange(1, len(num)):
    if p == num[i]:
        c += 1
        if c == 3:
            print "Yes"
            sys.exit()
    else:
        p = num[i]
        c = 1
print "No"
