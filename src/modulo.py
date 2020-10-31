newset = set(())
for x in range(10):
    number = int(input())
    toadd = number % 42
    newset.add(toadd)
print(len(newset))