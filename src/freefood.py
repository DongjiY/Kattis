totaldays = []
nums = int(input())
for x in range(nums):
    lower,upper = [int(x) for x in input().split()]
    for i in range(lower,upper+1):
        totaldays.append(i)
fooddays = set(totaldays)
print(len(fooddays))