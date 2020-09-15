import math

nums = int(input())
total = 0
for i in range(nums):
    string = input()
    power = string[-1]
    base = string[0:-1]
    total += math.pow(int(base),int(power))
print(int(total))