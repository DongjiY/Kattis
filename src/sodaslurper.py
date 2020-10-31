e,f,c = [int(x) for x in input().split()]
remains = e+f
sodas = 0
while remains >= c:
    sodas += remains//c
    remains = remains//c + remains % c
print(sodas)
