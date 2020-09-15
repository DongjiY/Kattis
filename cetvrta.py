def least_common(lst):
    return min(lst, key=lambda x: (lst.count(x), lst[::-1].index(x)))
x = []
y = []
while True:
    try:
        a,b = [int(x) for x in input().split()]
        x.append(a)
        y.append(b)
    except:
        break
# print(x,y)
print(least_common(x),least_common(y))
