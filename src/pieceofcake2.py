import math

s,h,v = [int(x) for x in input().split()]
slice1 = v*h
slice2 = (s-v)*h
slice3 = (s-v)*(s-h)
slice4 = (s-h)*v
print(max(slice1,slice2,slice3,slice4)*4)