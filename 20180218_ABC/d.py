# AC
from Queue import Queue
d = [0, 1, 0, -1]
h, w = map(int, raw_input().split())
m = list()
m.append(["#" for _ in xrange(w+2)])
for _ in xrange(h):
    m.append(["#"]+list(raw_input())+["#"])
m.append(["#" for _ in xrange(w+2)])
dat = len(filter(lambda x:x==".", [i for j in m for i in j]))

q = Queue()
q.put((1,1,1))

while not q.empty():
    xy = q.get()
    if not m[xy[0]][xy[1]] == ".":
        continue
    m[xy[0]][xy[1]] = xy[2]
    for i in xrange(4):
        e = (xy[0]+d[i], xy[1]+d[i+1&3], xy[2]+1)
        if m[xy[0]+d[i]][xy[1]+d[i+1&3]] == ".":
            q.put(e)

try:
    print dat-m[h][w]
except:
    print -1
