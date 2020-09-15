import sys
sys.setrecursionlimit(10**4)

def calcinterest(a,b,c):
    bee = b
    global count
    interest = b * a
    interest = round(interest*100) / 100
    bee += interest
    bee = round(bee*100) / 100
    bee -= c
    # print(addon)
    # print(temp)
    # print(count)
    if count >= 1200:
        return 
    elif bee > 0.0001:
        count += 1
        calcinterest(a,bee,c)
    else:
        count += 1

nums = int(input())
for x in range(nums):
    count = 0
    a,b,c = [float(y) for y in input().split()]
    a /= 100
    calcinterest(a,b,c)
    if count >= 1200:
        print("impossible")
    else:
        print(count)