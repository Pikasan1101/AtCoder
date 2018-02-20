# AC
n = input()
a = map(int, raw_input().split())
b = map(int, raw_input().split())
print max([sum(a[:i+1])+sum(b[i:]) for i in xrange(n)])
