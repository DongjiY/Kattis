problems,cases = [int(x) for x in input().split()]
cando = 0
for x in range(problems):
    testcase = 0
    for i in range(cases):
        tempstr = input()
        lowertemp = tempstr.lower()
        firsttemp = tempstr[0].lower() + tempstr[1:]
        # print(tempstr,lowertemp,firsttemp)
        if lowertemp == tempstr or lowertemp == firsttemp:
            testcase += 1
    if testcase == cases:
        cando += 1
print(cando)
