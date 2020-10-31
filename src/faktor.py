
A,I = [int(x) for x in input().split()]
bribe = 0.0
while bribe/A <= (I-1):
    bribe+=1.0
print(int(bribe))
