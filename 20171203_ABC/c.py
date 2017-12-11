# AC
n = input()
s = list()
for i in xrange(1, 2**10):
    s.append(i)
time_table = list()
benefit = list()
for _ in xrange(n):
    time_table.append("".join(raw_input().split()))
for _ in xrange(n):
    benefit.append(list(map(int, raw_input().split())))

op = [[None for i in xrange(n)] for j in xrange(2**10-1)]
for i in xrange(n):
    for j in xrange(2**10-1):
        op[j][i] = sum(map(int, list(bin(s[j] & int(time_table[i],2))[2:])))

print max([sum([benefit[i][op[j][i]] for i in xrange(n)]) for j in xrange(2**10-1)])
