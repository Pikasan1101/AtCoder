n, c = map(int, raw_input().split())
time_table = [list(map(int, raw_input().split())) for _ in xrange(n)]
time_table.sort()

recoders = [[True for i in xrange(10**5+1)]]
for tt in time_table:
    for recoder in recoders:
        if recoder[0] == tt[2]:
            for i in xrange(tt[0], tt[1]+1):
                recoder[i] = False
            break
        else:
            if recoder[tt[0]]:
                for i in xrange(tt[0], tt[1]+1):
                    recoder[i] = False
                recoder[0] = tt[2]
                break
    else:
        recoders.append([True for i in xrange(10**5+1)])
        recoders[-1][0] = tt[2]
        for i in xrange(tt[0], tt[1]+1):
            recoders[-1][i] = False
print len(recoders)

