valueList = [int(x) for x in input().split()]
valC = max(valueList)
valueList.remove(valC)
valA = min(valueList)
valueList.remove(valA)
valB = valueList[0]
allvalues = {"A":str(valA),"B":str(valB),"C":str(valC)}
order = input()
output = ""
for i in order:
    output += allvalues[i]+ " "
print(output)
