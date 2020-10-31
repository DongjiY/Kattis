nums = int(input())
for x in range(nums):
    r,e,c = [int(y) for y in input().split()]
    if (e-c) > r :
        print("advertise")
    elif (e-c) < r :
        print("do not advertise")
    else:
        print("does not matter")