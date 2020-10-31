nums = input()
expenses = [int(x) for x in input().split()]
totale = 0
for i in expenses:
    if i < 0:
        totale += abs(i)
print(totale)