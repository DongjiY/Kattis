nums = int(input())
actualtime = []
esttime = []
for x in range(nums):
    x,y = input().split()
    actualtime.append(int(y))
    esttime.append(60*int(x))
minute = sum(actualtime)/sum(esttime)
if minute <= 1:
    print("measurement error")
else:
    print(minute)
