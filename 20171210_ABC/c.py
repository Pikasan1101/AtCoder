import collections
n, k = map(int, raw_input().split())
num = map(int, raw_input().split())
n = int()
num = collections.Counter(num)
for t, v in sorted(num.items(), key=lambda x:x[1])[0:-k]:
    n += v
print n
