import itertools

# def getsmall(lst, val):
#     absvals = {}
#     for z in lst:
#         absvals[z] = abs(val-z)
#     return min(absvals.keys(), key=lambda k: absvals[k])
def closest(lst,K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

count = 1
while True:
  try:
    nums = int(input())
    print("Case "+str(count)+":")
    allnums = []
    for x in range(nums):
        allnums.append(int(input()))
    # print(allnums)
    sums = []
    for numbers in itertools.combinations(allnums,2):
        sums.append(sum(numbers))
    # for i in range(0, len(allnums)-1):
    #     for y in range(i+1, len(allnums)):
    #         sums.append(allnums[i]+allnums[y])
    # print(sums)
    comp = int(input())
    for x in range(comp):
        value = int(input())
        print("Closest sum to "+str(value)+" is "+str(closest(sums, value))+".")
    count += 1
  except:
    break

    