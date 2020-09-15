import math

r,c = [int(x) for x in input().split()]
areaWithCheese = ((r-c)**2)*math.pi
totalArea = math.pi*(r**2)
print((areaWithCheese/totalArea)*100)