nums = int(input())
for x in range(nums):
    temp = int(input())
    if temp % 400 == 0:
        print(temp//400)
    else:
        print(temp//400+1)
