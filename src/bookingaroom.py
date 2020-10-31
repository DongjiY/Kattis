r,n = [int(x) for x in input().split()]
bookedlst = []
if r == n:
    print("too late")
else:
    for y in range(n):
        bookedlst.append(int(input()))
    z = 1
    while z in bookedlst:
        if z == r:
            break
        z += 1
    print(z)

