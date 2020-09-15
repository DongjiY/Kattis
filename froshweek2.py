a,b = [int(x) for x in input().split()]
work = [int(x) for x in input().split()]
rest = [int(x) for x in input().split()]
print(len(work),len(rest))
workcarry = 0
fini = 0
for x in range(min(a,b)):
    if workcarry > 0:
        if workcarry <= rest[x]:
            fini += 1
            # print(fini,"carried1")
        if work[x] <= rest[x] - workcarry:
            fini += 1
            # print(fini,"carried2")
        workcarry = 0
    elif work[x] <= rest[x]:
        fini += 1
        # print(fini,"simple")
    else:
        workcarry = work[x] - rest[x]
        # print("carry",workcarry)
print(fini)