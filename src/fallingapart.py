nums = int(input())
numslst = [int(x) for x in input().split()]
numslst.sort(reverse = True)
# print(numslst)
alice = 0
bob = 0
for x in range(len(numslst)):
    if x % 2 != 0:
        bob += numslst[x]
    else:
        alice += numslst[x]
print(alice, bob)