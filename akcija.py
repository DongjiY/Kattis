
nums = int(input())
numarray = []
for x in range(nums):
    numarray.append(int(input()))
numarray.sort(reverse=True)
freebook = 0
for i in range(2,len(numarray),3):
    freebook += numarray[i]
print(sum(numarray)-freebook)