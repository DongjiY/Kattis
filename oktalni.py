octal = {"000":"0","001":"1","010":"2","011":"3","100":"4","101":"5","110":"6","111":"7"}
binary = input()
binlist = []
for x in range(len(binary)):
    binlist.append(binary[x])
# print(binlist)
while len(binlist)%3 != 0:
    binlist.insert(0,"0")
# print(binlist)
newbinlist = []
for i in range(2,len(binlist),3):
    newbinlist.append("".join(binlist[i-2:i+1]))
# print(newbinlist)
output = ""
for y in newbinlist:
    output += octal[y]
print(output)