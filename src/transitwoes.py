elapsedtime = 0
start, total, num = [int(x) for x in input().split()]
secondline = input().split()
thirdline = input().split()
fourthline = input().split()
for x in range(0,num):
    count = int(secondline[x])
    if count>int(fourthline[x]):
        while count % int(fourthline[x]) != 0:
            count+=1
    else:
        count = int(fourthline[x])
    elapsedtime += count
for y in thirdline:
    elapsedtime += int(y)
elapsedtime += int(secondline[-1])+start
if elapsedtime > total:
    print("no")
else:
    print("yes") 
