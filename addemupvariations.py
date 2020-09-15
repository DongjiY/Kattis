# for i in range(len(valuestocompare)):
#     for h in range(len(valuestocompare)):
#         if h ==i:
#             continue
#         else:    
#             if valuetoget-valuestocompare[i]==valuestocompare[h] or valuetoget-valuestocompare[i]==flip(valuestocompare[h]):
#                 yes += 1
#             elif valuetoget-flip(valuestocompare[i])==valuestocompare[h] or valuetoget-flip(valuestocompare[i])==flip(valuestocompare[h]):
#                 yes += 1
#             else:
#                 no += 1
# if yes >= 1:
#     print("YES")
# else:
#     print("NO")

# for i in range(len(valuestocompare)):
#     for h in range(len(valuestocompare)):
#         if valuetoget-valuestocompare[i]==valuestocompare[h] or valuetoget-valuestocompare[i]==flip(valuestocompare[h]):
#             if h==i:
#                 no += 1
#             else:
#                 yes += 1
#         elif valuetoget-flip(valuestocompare[i])==valuestocompare[h] or valuetoget-flip(valuestocompare[i])==flip(valuestocompare[h]):
#             if h==i:
#                 no += 1
#             else:
#                 yes += 1
#         else:
#             no += 1
# if yes >= 1:
#     print("YES")
# else:
#     print("NO")

# for i in range(len(valuestocompare)):
#     for h in range(len(valuestocompare)):
#         if h==i:
#             continue
#         else:    
#             if valuetoget-valuestocompare[i]==valuestocompare[h] or valuetoget-valuestocompare[i]==flip(valuestocompare[h]):
#                 yes += 1
#             elif valuetoget-flip(valuestocompare[i])==valuestocompare[h] or valuetoget-flip(valuestocompare[i])==flip(valuestocompare[h]):
#                 yes += 1
#             else:
#                 no += 1
# if yes >= 1:
#     print("YES")
# else:
#     print("NO")

# nums,valuetoget = [int(x) for x in input().split()]
# valuestocompare = [int(y) for y in input().split()]
# allvals = valuestocompare
# yes,no = 0,0
# for x in range(nums):
#     allvals.append(valuestocompare[x])
# for x in allvals:
#     if (valuetoget-x) in allvals:
#         yes += 1
# if yes >= 1:
#     print("YES")
# else:
#     print("NO")

# if (valuetoget-allvals[x]) in allvals:
#         if x<=(nums-1):
#             if (valuetoget-allvals[x]) != allvals[x+nums] or allvals[x] == allvals[x+nums]:
#                 if valuetoget-allvals[x] in allvals:
#                     yes += 1
#         if x>(nums-1):
#             if (valuetoget-allvals[x]) != allvals[x-nums] or allvals[x] == allvals[x-nums]:
#                 if valuetoget-allvals[x] in allvals:
#                     yes += 1

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

# fliparray = [0,1,2,-1,-1,5,9,-1,8,6]
# def flip(num):
#     x = ""
#     n = int(num)
#     while(n > 0):
#         digit = n % 10
#         if(fliparray[digit]==-1):
#             return -1
#         else:
#             x+= str(digit)
#             n = n//10
#     return int(x)
    
# nums,valuetoget = [int(x) for x in input().split()]
# valuestocompare = [int(y) for y in input().split()]
# yes = False
# for x in range(len(valuestocompare)):
#     temp = valuestocompare[x]
#     diffnum = valuetoget - valuestocompare[x]
#     diffnumflip = valuetoget - flip(valuestocompare[x])
#     del valuestocompare[x]
#     if diffnum in valuestocompare or flip(diffnum) in valuestocompare or diffnumflip in valuestocompare or flip(diffnumflip) in valuestocompare:
#         print("YES")
#         yes = True
#         break
#     valuestocompare.insert(x,temp)
# if(not yes):
#     print("NO")