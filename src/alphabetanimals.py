def seepossible(lst,letter):
    possiblewords = []
    for x in lst:
        if x[0] == letter:
            possiblewords.append(x)
    lettercount = {}
    for x in lst:
        if x[0] in lettercount:
            lettercount[x[0]] += 1
        else:
            lettercount[x[0]] = 1
    # print(lettercount)
    # print(possiblewords)
    if len(possiblewords) == 0:
        return "?"
    for x in possiblewords:
        if x[-1] in lettercount:
            if x[0] == x[-1] and lettercount[x[-1]]-1 == 0:
                return x + "!"
        else:
            return x + "!"
    for x in possiblewords:
        if x[-1] in lettercount:
            return x

past = input()
lettertoget = past[-1]
avail = int(input())
words = []
for x in range(avail):
    words.append(input())
# print(words)
print(seepossible(words,lettertoget))

