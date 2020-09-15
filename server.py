numtasks,totaltime = map(int,input().split())
tasktime = input().split()
sums = 0
counter = 0
for x in range(len(tasktime)):
    sums += int(tasktime[x])
    if sums <= totaltime:
        counter += 1
    if sums >= totaltime:
        break
print(counter)