nums = int(input())
for x in range(nums):
    rep,val = [int(i) for i in input().split()]
    s1 = 0
    s2 = 0
    s3 = 0
    for y in range(val+1):
        s1 += y
    for i in range(1,val*2,2):
        s2 += i
    for z in range(2,val*2+1,2):
        s3 += z
    print(rep,s1,s2,s3)