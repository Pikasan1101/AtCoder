# AC
import sys
s = list(raw_input()[::-1])
t = list(raw_input()[::-1])
for i in xrange(0, len(s)-len(t)+1):
    for j in xrange(len(t)):
        if ("?" == s[i+j]) or (t[j] == s[i+j]):
            continue
        break
    else:
        for j in xrange(len(t)):
            s[i+j] = t[j]
        break
else:
    print "UNRESTORABLE"
    sys.exit()
print "".join([(lambda x: "a" if x == "?" else x)(s[i]) for i in xrange(len(s))])[::-1]

