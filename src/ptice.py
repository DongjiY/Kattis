adrian = ["A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A","B","C","A"]
bruno = ["B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C","B","A","B","C"]
goran = ["C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A","B","B","C","C","A","A"]
adriancount,brunocount,gorancount = 0,0,0
nums = int(input())
seq = input()
seqlist = []
for z in range(len(seq)):
    seqlist.append(seq[z])
for x in range(nums):
    if adrian[x] == seqlist[x]:
        adriancount += 1
    if bruno[x] == seqlist[x]:
        brunocount += 1
    if goran[x] == seqlist[x]:
        gorancount += 1
# print(adriancount,brunocount,gorancount)
maxval = max(adriancount,brunocount,gorancount)
print(maxval)
if adriancount == maxval:
    print("Adrian")
if brunocount == maxval:
    print("Bruno")
if gorancount == maxval:
    print("Goran")
