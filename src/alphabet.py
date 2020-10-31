alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
phraselst = []
counts = []
for x in input():
    phraselst.append(x)
print(phraselst)
count = 0
alphai = 0
for x in range(len(phraselst)):
    if phraselst[x] == alpha[alphai]:
        count += 1
        # print(count)
        alphai += 1
    else:
        alphai = 0
        counts.append(count)
        count = 0
counts.append(count)
print(counts)
print(26-max(counts))