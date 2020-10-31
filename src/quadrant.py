import sys

cords = sys.stdin.readlines()
x = int(cords[0])
y = int(cords[1])
if x>0 and y>0:
    print(1)
elif x>0 and y<0:
    print(4)
elif x<0 and y>0:
    print(2)
else:
    print(3)