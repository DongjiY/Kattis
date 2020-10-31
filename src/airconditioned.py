from collections import Counter

def maketemp(l,h):
    templist = []
    for i in range(l,h+1):
        templist.append(i)
    return templist

def themode(lst):
    n = len(lst)
    data = Counter(lst)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        return -1
    else: 
        return mode[0]
    
minions = int(input())
listoflist = []
listoftemps = []
rooms = 0
for x in range(minions):
    x,y = [int(x) for x in input().split()]
    listoflist.append(maketemp(x,y))
    listoftemps += maketemp(x,y)
listoftemps.sort()
print(listoflist)
print(listoftemps)
while themode(listoftemps) != -1:
    mode = themode(listoftemps)
    print(mode)
    for x in range(len(listoflist)-1,-1,-1):
        if mode in listoflist[x]:
            for y in listoflist[x]:
                listoftemps.remove(y)
            del listoflist[x]
    print(listoflist)
    print(listoftemps)
    rooms += 1
rooms += len(listoflist)
print(rooms)

