# AC
l = list(raw_input())

s = l[0]
f = False
mx = 0
x = 0
for i, n in enumerate(l):
    if not n == s:
        mx = max(mx, min(i, len(l)-x))
        x = i
        s = n
else:
    mx = max(mx, min(i+1, len(l)-x))
print mx
