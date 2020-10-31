cards = input()
t = 0
c = 0
g = 0
for x in range(len(cards)):
    if cards[x] == "T":
        t += 1
    elif cards[x] == "C":
        c += 1
    else:
        g += 1
total = t**2 + c**2 + g**2 + (7*min(t,c,g))
print(total)