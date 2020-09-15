nums = int(input())
numslist = []
tally = 0
avgtotal = 0
for z in range(nums):
    numslist.append(int(input()))
for y in range(len(numslist)):
    tally += numslist[y]*((4/5)**y)
tally /= 5
for x in range(nums):
    temp = numslist[x]
    del numslist[x]
    for i in range(len(numslist)):
        avgtotal += (numslist[i]*((4/5)**i))
    numslist.insert(x,temp)
avgtotal /= ((nums)*5)
print(tally)
print(avgtotal)