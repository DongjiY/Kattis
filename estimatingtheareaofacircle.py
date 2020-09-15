import math

array = input().split()
while array != ['0','0','0']:
    r = float(array[0])
    m = int(array[1])
    c = int(array[2])
    realarea = math.pi*math.pow(r,2)
    estarea = math.pow(2*r,2)*(c/m)
    print(realarea, estarea)
    array = input().split()

