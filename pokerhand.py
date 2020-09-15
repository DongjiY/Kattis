hand = input().split()
counts = [0]*13
for x in range(len(hand)):
    if hand[x][0] == "A":
        counts[0] += 1
    elif hand[x][0] == "2":
        counts[1] += 1
    elif hand[x][0] == "3":
        counts[2] += 1
    elif hand[x][0] == "4":
        counts[3] += 1
    elif hand[x][0] == "5":
        counts[4] += 1
    elif hand[x][0] == "6":
        counts[5] += 1
    elif hand[x][0] == "7":
        counts[6] += 1
    elif hand[x][0] == "8":
        counts[7] += 1
    elif hand[x][0] == "9":
        counts[8] += 1
    elif hand[x][0] == "T":
        counts[9] += 1
    elif hand[x][0] == "J":
        counts[10] += 1
    elif hand[x][0] == "Q":
        counts[11] += 1
    else:
        counts[12] += 1
print(max(counts))
