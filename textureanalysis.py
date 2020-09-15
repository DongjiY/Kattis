def findPat(readin):
    theInput = readin
    if theInput == "*":
        return True
    pattern = ""
    newInput = theInput[1:]
    Case = True
    # print(newInput)
    for x in newInput:
        if x == "*":
            pattern += x
            break
        pattern += x
    # print(pattern)
    for x in range(1,len(theInput),len(pattern)):
        if theInput[x:x+len(pattern)]!=pattern:
            Case = False
    return Case

count = 1
firstLine = input()
while firstLine != "END":
    if findPat(firstLine):
        print(str(count)+" EVEN")
    else:
        print(str(count)+" NOT EVEN")
    count += 1
    firstLine = input()