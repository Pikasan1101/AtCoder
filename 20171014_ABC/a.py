# AC
print (lambda a,b,c: a if b == c else b if a == c else c)(*map(int, raw_input().split()))
