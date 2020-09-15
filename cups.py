value = []
nums = int(input())
newdict = {}
for x in range(nums):
    array = input().split()
    newarray = array.copy()
    newarray.sort()
    if array != newarray:
        newdict[int(newarray[0])] = newarray[1]
        value.append(int(newarray[0]))
    else:
        newdict[int(newarray[0])//2] = newarray[1]
        value.append(int(newarray[0])//2)
value.sort()
for i in value:
    print(newdict[i])

