# WA
import sys
chars = [chr(65+i) for i in xrange(26)]
def func(l):
    if len(l) == 1:
        return l
    l1 = func(l[:len(l)/2])
    l2 = func(l[len(l)/2:])
    retval = list()
    while len(l1) and len(l2):
        print "? %s %s" % (l1[0], l2[0])
        sys.stdout.flush()
        if raw_input() == "<":
            retval.append(l1.pop(0))
        else:
            retval.append(l2.pop(0))
    return retval+l1 if len(l1) > 0 else retval+l2

n, q = map(int, raw_input().split())
l = chars[:n]
print "! %s" % "".join(func(l))
sys.stdout.flush()
