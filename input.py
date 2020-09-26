sp = list(map(int,input().split())) #split the input and convert to int
x = sp[0]
y = sp[1]
poly = input() 
if eval(poly) == sp[1]: #subsitute x in to the poly and compare with y
    print(True)
else:
    print(False)
