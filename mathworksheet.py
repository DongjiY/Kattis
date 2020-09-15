def setStr(largest,numstr):
    output = ""
    spaces = largest - len(numstr)
    for x in range(spaces):
        output += " "
    output += numstr
    return output

nums = int(input())
while nums != 0:
    numslst = []
    for x in range(nums):
        numslst.append(str(eval(input())))
    lenlargest = len(max(numslst, key=len))
    newoutput = ""
    for x in range(len(numslst)):
        if len(newoutput)+lenlargest+1 > 50:
            newoutput = newoutput.rstrip()
            print(newoutput)
            newoutput = setStr(lenlargest,numslst[x]) + " "
        else:
            newoutput += setStr(lenlargest,numslst[x]) + " "
    print(newoutput.rstrip())
    nums = int(input())
    if nums != 0:
        print()


