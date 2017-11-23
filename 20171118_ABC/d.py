# AC
import heapq

def func(start, mp):
    d = [float("inf") for i in xrange(10)]
    d[start] = 0
    q = [(0, start)]
    while len(q):
        c, n = heapq.heappop(q)
        if d[n] < c:
            continue
        for i in xrange(10):
            if d[i] > d[n]+mp[n][i]:
                d[i] = d[n]+mp[n][i]
                heapq.heappush(q, (d[i], i))
    return d[1]

h, w = map(int, raw_input().split())
mp = list()
for i in xrange(10):
    mp.append(map(int, raw_input().split()))

m = [func(i, mp) for i in xrange(10)]
print sum([sum(map(lambda x:m[x] if not x == -1 else 0, map(int, raw_input().split()))) for i in xrange(h)])

