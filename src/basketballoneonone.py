scorebreakdown = input()
aScore = 0
bScore = 0
newGoal = False
for x in range(len(scorebreakdown)):
    if scorebreakdown[x] == 'A':
        aScore += int(scorebreakdown[x+1])
    if scorebreakdown[x] == 'B':
        bScore += int(scorebreakdown[x+1])

    if aScore == 10 and bScore == 10:
            newGoal = True

    if newGoal:
        if aScore >= bScore+2:
            print("A")
            break
        elif bScore >= aScore+2:
            print("B")
            break
    else:
        if aScore >= 11:
            print("A")
            break
        elif bScore >= 11:
            print("B")
            break
