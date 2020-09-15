cases = int(input())
for x in range(cases):
    nums = int(input())
    numlist = [int(x) for x in input().split()]
    distance = 2*(max(numlist)-min(numlist))
    print(distance)