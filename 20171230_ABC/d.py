# AC
import math
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

m = list()
s = 0
for i in xrange(10**5):
    if is_prime(i) and is_prime((i+1)/2):
        s += 1
    m.append(s)

n = input()
for _ in xrange(n):
    s = 0
    a, b = map(int, raw_input().split())
    print m[b] - m[a-1]
