nums = int(input())
inputlst = []
ascendinginputlst = []
descinputlst = []
for x in range(nums):
    inputlst.append(input())
ascendinginputlst = sorted(inputlst)
descinputlst = sorted(inputlst, reverse = True)
if inputlst == ascendinginputlst:
    print("INCREASING")
elif inputlst == descinputlst:
    print("DECREASING")
else:
    print("NEITHER")