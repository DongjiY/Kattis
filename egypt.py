array = [int(x) for x in input().split()]
while array != [0,0,0]:
    array.sort()
    if array[2]**2 == array[0]**2 + array[1]**2:
        print("right")
    else:
        print("wrong")
    array = [int(x) for x in input().split()]

