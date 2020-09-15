import itertools

def closest(lst,K):
    if len(lst) == 0:
        return 0
    return lst[min(range(len(lst)), key = lambda i: abs(int(lst[i])-K))]


num = input()
comboA = []#list(permutations(num,len(num)))
for i in itertools.permutations(num,len(num)): #permutation instead of combination
    comboA.append(i)
comboB = []
for x in range(len(comboA)):
    comboB.append("".join(comboA[x]))
# print(comboB)
for x in range(len(comboB)-1,-1,-1):
    if int(comboB[x]) <= int(num):
        del comboB[x]
# print(comboB)
print(closest(comboB,int(num)))