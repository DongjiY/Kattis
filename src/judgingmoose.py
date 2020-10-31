a,b = [int(x) for x in input().split()]
if a == 0 and b == 0:
    print("Not a moose")
elif a == b:
    print("Even "+str(a*2))
else:
    print("Odd "+str(max(a,b)*2))