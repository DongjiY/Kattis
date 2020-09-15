nums = int(input())
temps = [int(x) for x in input().split()]
belowzero = 0
for x in temps:
    if x < 0:
        belowzero+=1
print(belowzero)