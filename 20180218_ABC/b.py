# AC
n = input()
a = sorted(list(map(int, raw_input().split())), reverse=True)
print sum([a[i] for i in xrange(n) if not i % 2])-sum([a[i] for i in xrange(n) if i % 2])
