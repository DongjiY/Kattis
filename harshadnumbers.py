def checkHar(val):
    castedval = str(val)
    thisSum = 0
    for x in range(len(castedval)):
        thisSum += int(castedval[x])
    if val%thisSum == 0:
        return False
    else:
        return True

start = int(input())
while checkHar(start):
    start += 1
print(start)