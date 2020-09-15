import math

h,v = [float(x) for x in input().split()]
l = h/(math.sin(math.radians(v)))
print(math.ceil(l))