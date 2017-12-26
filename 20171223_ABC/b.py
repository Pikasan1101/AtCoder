# AC
n, a, b = map(int, raw_input().split())
print sum([i for i in xrange(1, n+1) if a <= sum(map(int, list(str(i)))) <= b])
