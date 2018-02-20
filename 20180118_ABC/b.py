# AC
a = input()
b = input()
c = input()
x = input()

count = int()
for i in xrange(a+1):
    for j in xrange(b+1):
        for k in xrange(c+1):
            if x-(500*i+100*j+50*k) == 0:
                count += 1
print count
