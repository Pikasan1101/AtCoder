# AC
x, y = map(int, raw_input().split())

n = 1
while True:
    x *= 2
    if x > y:
        break
    n += 1
print n
