nums = int(input())
for x in range(nums):
    case, days = [int(y) for y in input().split()]
    daySum = 0
    for z in range(days+1):
        daySum += z
    print(case, daySum+days)
