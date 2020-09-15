nums = int(input())
for x in range(nums):
    thisInput = input()
    if thisInput == "P=NP":
        print("skipped")
    else:
        print(eval(thisInput))