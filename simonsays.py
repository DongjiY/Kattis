nums = int(input())
for x in range(nums):
    line = input()
    if "Simon says" in line:
        print(line[10:])