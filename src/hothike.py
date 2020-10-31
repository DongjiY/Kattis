nums = int(input())
options = []
correspondingdays = []
temps = [int(x) for x in input().split()]
for x in range(nums-2):
    options.append(max(temps[x],temps[x+2]))
    correspondingdays.append(x)
print(correspondingdays[options.index(min(options))]+1,min(options))
