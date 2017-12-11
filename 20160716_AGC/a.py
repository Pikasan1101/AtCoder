n = input()*2
l = sorted(map(int, raw_input().split()))
print sum([l[i] for i in xrange(0, n, 2)])
