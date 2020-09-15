word = set(input())
perm = input()
gotem = len(set(word))
# print(gotem)
wrongcount = 0
counter = 0
while wrongcount < 10:
    # print(perm[counter])
    if perm[counter] in word:
        counter += 1
        gotem -= 1
    else:
        counter += 1
        wrongcount += 1
# print(gotem)
if gotem == 0:
    print("WIN")
else:
    print("LOSE")