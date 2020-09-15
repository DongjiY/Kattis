def flip(num):
    tostring = str(num)
    if "3" in tostring or "4" in tostring or "7" in tostring:
        return num
    flippednum = tostring[::-1]
    if "6" in flippednum:
        return int(flippednum.replace("6","9"))
    elif "9" in flippednum:
        return int(flippednum.replace("9","6"))
    else:
        return int(flippednum)
    
nums,valuetoget = [int(x) for x in input().split()]
valuestocompare = [int(y) for y in input().split()]
allvals = valuestocompare
yes=False
for x in range(nums):
    allvals.append(flip(valuestocompare[x]))
for x in range(len(allvals)):
    temp = allvals[x]
    if x<=(nums-1):
        tempflip = allvals[x+nums]
        del allvals[x+(nums)]
        del allvals[x]
    else:
        tempflip = allvals[x-nums]
        del allvals[x-(nums)]
        del allvals[x-1]
    if valuetoget-temp in allvals:
        print("YES")
        yes=True
        break
    allvals.insert(x,temp)
    allvals.insert(x+nums,tempflip)
if(not yes):
    print("NO")