nums = int(input())
inputs = []
missing = []
for x in range(nums):
    inputs.append(int(input()))
for x in range(1,inputs[-1]):
    if x not in inputs:
        missing.append(x)
if len(missing) == 0:
    print("good job")
else:
    for i in missing:
        print(i)
