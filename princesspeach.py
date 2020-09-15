obs,nums = [int(x) for x in input().split()]
miss = set()
for x in range(nums):
    miss.add(int(input()))
misslst = list(miss)
misslst.sort()
# print(misslst)
for x in range(obs):
    if x not in misslst:
        print(x)
print("Mario got "+str(len(misslst))+" of the dangerous obstacles.")