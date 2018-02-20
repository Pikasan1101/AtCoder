# AC
n = input()
t = [map(int, raw_input().split()) for _ in xrange(n-1)]

for i in xrange(n-1):
    s = t[i][1]
    for j in xrange(i, n-1):
        if s >= t[j][1]:
            if not ((s - t[j][1]) % t[j][2]) == 0:
                s += t[j][2] - ((s - t[j][1]) % t[j][2])
            s += t[j][0]
        else:
            s = t[j][0] + t[j][1]
    print s
print 0
