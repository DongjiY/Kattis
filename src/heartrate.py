nums = int(input())
for x in range(nums):
    b,p = [float(x) for x in input().split()]
    print(60/(p/(b-1)),(60*b)/p,60/(p/(b+1)))
