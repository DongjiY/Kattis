trans = {"C":0,"C#":1,"D":2,"D#":3,"E":4,"F":5,"F#":6,"G":7,"G#":8,"A":9,"A#":10,"B":11}
def transposition(lst1,lst2):
    past = abs(lst1[0]-lst2[0])
    for x in range(1,len(lst1)):
        if abs(lst1[x]-lst2[x]) != past:
            return False
    return True
def retrograde(lst1,lst2):
    return lst1[::-1] == lst2
def inversion(lst1,lst2):
    for x in range(len(lst1)):
        dist = lst1[x]-lst1[0]
        # print(dist)
        comp = (lst1[0]-dist)
        if comp < 0:
            comp = 12-abs(comp)
        if comp >= 12:
            comp = comp-12
        # print(comp)
        # print(lst2[x],comp,"ass")
        if lst2[x] != comp:
            return False
            # print(lst2[x],comp,"ass")
    return True
nums = int(input())
temp1 = input().split()
orig = []
for x in temp1:
    orig.append(trans[x])
temp = input().split()
new = []
for x in temp:
    new.append(trans[x])
# print(orig,new)
if transposition(orig,new):
    print("Transposition")
elif retrograde(orig,new):
    print("Retrograde")
elif inversion(orig,new):
    print("Inversion")
else:
    print("Nonsense")