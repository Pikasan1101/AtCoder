# AC
a, b, c, d = map(int, list(raw_input()))

ppp = lambda a,b,c,d: (a+b+c+d == 7, "%d+%d+%d+%d=7" % (a,b,c,d))
pps = lambda a,b,c,d: (a+b+c-d == 7, "%d+%d+%d-%d=7" % (a,b,c,d))
psp = lambda a,b,c,d: (a+b-c+d == 7, "%d+%d-%d+%d=7" % (a,b,c,d))
pss = lambda a,b,c,d: (a+b-c-d == 7, "%d+%d-%d-%d=7" % (a,b,c,d))
spp = lambda a,b,c,d: (a-b+c+d == 7, "%d-%d+%d+%d=7" % (a,b,c,d))
sps = lambda a,b,c,d: (a-b+c-d == 7, "%d-%d+%d-%d=7" % (a,b,c,d))
ssp = lambda a,b,c,d: (a-b-c+d == 7, "%d-%d-%d+%d=7" % (a,b,c,d))
sss = lambda a,b,c,d: (a-b-c-d == 7, "%d-%d-%d-%d=7" % (a,b,c,d))

li = [ppp, pps, psp, pss, spp, sps, ssp, sss]
for l in li:
    if l(a, b, c, d)[0]:
        print l(a,b,c,d)[1]
        break



