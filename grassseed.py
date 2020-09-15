cost = float(input())
lawns = int(input())
totalarea = 0
for x in range(lawns):
    w,l = [float(y) for y in input().split()]
    totalarea += w*l
output = cost*totalarea
print('{:.7f}'.format(output))