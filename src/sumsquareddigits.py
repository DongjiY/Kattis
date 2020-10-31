import math

def toNewBase(base, num):
    newvalue = []
    for x in range(int(math.log(num,base)+1)):
        newvalue.append(num%base)
        num = num//base
    return newvalue

trials = int(input())
for x in range(trials):
    total = 0
    a,b,n = [int(x) for x in input().split()]
    array = toNewBase(b,n)
    for i in array:
        total += int(i)**2
    print(a, total)




    

