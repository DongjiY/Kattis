nums = int(input())
rep = 1
while nums != 0:
    compilelist = []
    for x in range(nums):
        compilelist.append(input())
    print("SET "+str(rep))
    for x in range(0,len(compilelist),2):
        print(compilelist[x])
    if nums % 2 ==0:
        for x in range(len(compilelist)-1,0,-2):
            print(compilelist[x])
    else:
        for x in range(len(compilelist)-2,0,-2):
            print(compilelist[x])
    nums = int(input())
    rep += 1