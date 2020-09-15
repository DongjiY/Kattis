L,x = [int(x) for x in input().split()]
total = 0
count = 0
for i in range(x):
    temp = input().split()
    if temp[0] == "enter":
        if total + int(temp[1]) > L:
            count += 1
        else:
            total += int(temp[1])
    if temp[0] == "leave":
        total -= int(temp[1])
print(count)