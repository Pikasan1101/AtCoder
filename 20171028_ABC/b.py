# AC
n = input()
k = input()
num = 1
b = lambda x, y: x+y if x > y else x*2
for _ in xrange(n):
    num = b(num, k)
print num
