x, y = [int(i) for i in input().split()]
if y == 1:
    if x == 0:
        print("ALL GOOD")
    elif x != 0:
        print("IMPOSSIBLE")
else:
    intersection = (-1*x)/(y-1)
    print(intersection)