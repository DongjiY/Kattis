import math
def sorter(a,b,c,A,B,C):
    lst = [a,b,c]
    lst.sort()
    classification = ""
    if a == b or a == c or b == c:
        classification += "isosceles "
    else:
        classification += "scalene "
    if A == 90.0 or B == 90.0 or C == 90.0:
        classification += "right "
    elif A > 90.0 or B > 90.0 or C > 90.0:
        classification += "obtuse "
    else:
        classification += "acute "
    classification += "triangle"
    return classification
nums = int(input())
for x in range(nums):
    x1,y1,x2,y2,x3,y3 = [int(y) for y in input().split()]
    area = abs(.5*((x1*(y2-y3))+(x2*(y3-y1))+(x3*(y1-y2))))
    if area == 0.0:
        print("Case #"+str(x+1)+": not a triangle")
    else:
        a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
        c = math.sqrt((x3-x1)**2 + (y3-y1)**2)
        # print(a,b,c)
        A = round(math.degrees(math.acos((a**2-b**2-c**2)/(-2*b*c))),1)
        B = round(math.degrees(math.acos((b**2-c**2-a**2)/(-2*a*c))),1)
        C = round(math.degrees(math.acos((c**2-b**2-a**2)/(-2*a*b))),1)
        # print(A,B,C)
        print("Case #"+str(x+1)+": "+sorter(a,b,c,A,B,C))