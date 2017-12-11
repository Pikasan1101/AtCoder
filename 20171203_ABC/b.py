# AC
print (lambda n: "No" if n%sum(map(int, list(str(n)))) else "Yes")(input())
