# AC
h, w = map(int, raw_input().split())
table = list()
table.append([0]*(w+2))
for _ in xrange(h):
    table.append([0]+list(map(lambda c:0 if c == "." else c, list(raw_input())))+[0])
table.append([0]*(w+2))

xy = [0, 1, 0, -1, 1, 1, -1, -1, 0]
for i in xrange(1, h+1):
    for j in xrange(1, w+1):
        if table[i][j] == "#":
            for k in xrange(8):
                if type(table[i+xy[k]][j+xy[k+1]]) == type(int()):
                    table[i+xy[k]][j+xy[k+1]] += 1


for i in xrange(1, h+1):
    print "".join(map(str, table[i][1:-1]))

