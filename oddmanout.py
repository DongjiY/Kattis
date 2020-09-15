nums = int(input())
for x in range(nums):
    g = int(input())
    lst = input().split()
    newlst = set(lst)
    finallst = []
    for y in newlst:
        if lst.count(y) != 2:
            finallst.append(y)
    print("Case #"+str(x+1)+": "+"".join(finallst))