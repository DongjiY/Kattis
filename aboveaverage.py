
nums = int(input())
for x in range(nums):
    dataset = [int(y) for y in input().split()]
    denominator = float(dataset[0])
    del dataset[0]
    avg = sum(dataset)//denominator
    aboveavg = 0
    for i in range(len(dataset)):
        if dataset[i] > avg:
            aboveavg += 1
    answer = (aboveavg/denominator)*100
    print('{:.3f}'.format(answer)+"%")