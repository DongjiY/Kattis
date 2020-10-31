import sys

demo = 1
consumed = 0
megpermonth = 0
numofmonths = 0

for line in sys.stdin.readlines():
    if demo ==1:
        megpermonth = int(line)
        demo+=1
        continue
    if demo ==2:
        numofmonths = int(line)
        demo+=1
        continue

    consumed += int(line)

print(megpermonth*(numofmonths+1)-consumed)


