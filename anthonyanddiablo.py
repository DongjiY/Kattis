import math
a,n = [float(x) for x in input().split()]
if n**2/(4*math.pi) >= a:
    print("Diablo is happy!")
else:
    print("Need more materials!")
