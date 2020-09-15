import math

def maxarea(a,b,c,d):
    semi = (a+b+c+d)/2
    return math.sqrt((semi-a)*(semi-b)*(semi-c)*(semi-d))

s1,s2,s3,s4 = [int(x) for x in input().split()]
print(maxarea(s1,s2,s3,s4))