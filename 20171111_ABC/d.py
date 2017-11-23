# AC
print(lambda n:max(abs(n[2]-n[-1]),abs(n[-2]-n[-1])))(map(int,(raw_input()+" "+raw_input()).split()))
