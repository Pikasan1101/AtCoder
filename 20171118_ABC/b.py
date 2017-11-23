# AC
luca = list()
luca.append(2)
luca.append(1)
for i in xrange(2, input()+1):
    luca.append(luca[i-1]+luca[i-2])
print luca[-1]

