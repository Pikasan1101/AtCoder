# AC
input()
num = map(int, raw_input().split())
n = int()
while True:
    num = map(lambda x: -1 if x%2 else x/2, num)
    if -1 in num:
        print n
        break
    n += 1
