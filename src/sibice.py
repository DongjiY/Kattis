import math

matches, width, height = [int(x) for x in input().split()]
canfit = math.sqrt(pow(width,2) + pow(height,2))
for n in range(matches):
    if int(input()) <= canfit:
        print("DA")
    else:
        print("NE")