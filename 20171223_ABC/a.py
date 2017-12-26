# AC
print (lambda a,b,c,d: "Left" if a+b>c+d else "Right" if a+b<c+d else "Balanced")(*map(int, raw_input().split()))
