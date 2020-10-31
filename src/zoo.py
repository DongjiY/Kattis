nums = int(input())
count = 1
while nums != 0:
    zooDict = {}
    zooAnimals = []
    for x in range(nums):
        thisInput = input().split()
        animal = thisInput[-1].lower()
        if animal not in zooAnimals:
            zooAnimals.append(animal)
            zooDict[animal] = 1
        else:
            zooDict[animal] += 1
    zooAnimals.sort()
    # print(zooAnimals)
    print("List "+str(count)+":")
    count += 1
    for x in range(len(zooAnimals)):
        print(zooAnimals[x]+" | "+str(zooDict[zooAnimals[x]]))
    nums = int(input())