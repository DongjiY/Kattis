nums = int(input())
count = 0
for x in range(nums):
    thisInput = input().lower()
    if "rose" in thisInput or "pink" in thisInput:
        count += 1
if count == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(count)
