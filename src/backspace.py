phrase = []
for x in input():
    phrase.append(x)
# print(phrase)
count = 0
newphrase = []
for x in range(len(phrase)-1,-1,-1):
    # print(count)
    if phrase[x] != "<":
        if count > 0:
            count -= 1
            continue
        newphrase.append(phrase[x])
    elif phrase[x] == "<":
        count += 1
newphrase.reverse()
prt = "".join(newphrase)
print(prt)
    