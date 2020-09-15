newNum = input()
while len(newNum) != 1:
    intNums = []
    for x in newNum:
        intNums.append(int(x))
    mult = 1
    for y in intNums:
        if y == 0:
            continue
        else:
            mult = mult*y
    newNum = str(mult)    
print(newNum)