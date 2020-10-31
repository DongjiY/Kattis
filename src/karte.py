def getNewVal(lsta,lstb):
    p,k,h,t = 13,13,13,13
    if len(lsta) != len(lstb):
        return "GRESKA"
    else:
        for x in lsta:
            letter = x[0]
            if letter == 'P':
                p -= 1
            elif letter == 'K':
                k -= 1
            elif letter == 'H':
                h -= 1
            else:
                t -= 1
        return str(p)+" "+str(k)+" "+str(h)+" "+str(t)

allcards = input()
newcards = []
for x in range(0,len(allcards),3):
    newcards.append(allcards[x:x+3])
uniquecards = set(newcards)
print(getNewVal(newcards,uniquecards))
