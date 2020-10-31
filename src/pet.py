totals = []
for x in range(1,6):
    temp = [int(x) for x in input().split()]
    totals.append(sum(temp))
largest = max(totals)
for i in range(len(totals)):
    if totals[i] == largest:
        print(str(i+1)+" "+str(largest))
        break