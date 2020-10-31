people = int(input())
lineupInput = [int(x) for x in input().split()]
lineup = [""]*people
lineup[0] = '1'
for y in range(people-1):
    lineup[lineupInput[y]+1] = str(y+2)
print(" ".join(lineup))