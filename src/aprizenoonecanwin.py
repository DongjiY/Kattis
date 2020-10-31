def prize(lst,phub):
    if len(lst) < 2:
        return 1
    for x in range(0,len(lst)-1):
        if lst[x] + lst[x+1] > phub:
            return x+1
            break
    return len(lst)

nums,price = [int(x) for x in input().split()]
items = [int(y) for y in input().split()]
items.sort()
# print(items)
print(prize(items,price))

