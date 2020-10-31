periods = int(input())
total = 0.0
for i in range(periods):
    num, time = [float(x) for x in input().split()]
    total = total + (num*time)
print(total)