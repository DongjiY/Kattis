nums = int(input())
for x in range(nums):
    phrase1 = input()
    phrase2 = input()
    outphrase = ""
    for x in range(len(phrase1)):
        if phrase1[x] == phrase2[x]:
            outphrase += "."
        else:
            outphrase += "*"
    print(phrase1)
    print(phrase2)
    print(outphrase)
    print()
