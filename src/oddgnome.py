nums = int(input())
for x in range(nums):
    inputLst = [int(x) for x in input().split()]
    currentVal = inputLst[1]
    for x in range(2,len(inputLst)-1):
        if inputLst[x] != currentVal+1:
            print(x)
            break
        currentVal = inputLst[x]
