
nums = int(input())
drink = input()
while nums >= 1:
    if nums == 1:
        print("1 bottle of "+drink+" on the wall, 1 bottle of "+drink+".")
        print("Take it down, pass it around, no more bottles of "+drink+".")
        print()
    elif nums == 2:
        print(str(nums)+" bottles of "+drink+" on the wall, "+str(nums)+" bottles of "+drink+".")
        print("Take one down, pass it around, "+str(nums-1)+" bottle of "+drink+" on the wall.")
        print()
    else:
        print(str(nums)+" bottles of "+drink+" on the wall, "+str(nums)+" bottles of "+drink+".")
        print("Take one down, pass it around, "+str(nums-1)+" bottles of "+drink+" on the wall.")
        print()
    nums -= 1