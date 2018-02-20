# AC
a = [map(int, raw_input().split()) for _ in xrange(3)]
h0 = sum(a[0])
h1 = sum(a[1])
h2 = sum(a[2])
w0 = sum([a[i][0] for i in xrange(3)])
w1 = sum([a[i][1] for i in xrange(3)])
w2 = sum([a[i][2] for i in xrange(3)])

if (h0-h1)%3 or (h1-h2)%3 or (h2-h0)%3 or (w0-w1)%3 or (w1-w2)%3 or (w2-w0)%3:
    print "No"
else:
    print "Yes"
