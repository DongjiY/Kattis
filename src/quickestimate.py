import math
nums = int(input())
for x in range(nums):
    value = int(input())
    if value ==0:
        print(1)
    else:
        output = int(math.log10(value)+1)
        print(output)
