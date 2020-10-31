import math

def tute(m,n,t):
    if t==1:
        if n>=13:
            return "TLE"
        elif m>= math.factorial(n):
            return "AC"
    elif t==2:
        if m>= 2**n:
            return "AC"
    elif t==3:
        if m>= n**4:
            return "AC"
    elif t==4:
        if m>= n**3:
            return "AC"
    elif t==5:
        if m>= n**2:
            return "AC"
    elif t==6:
        if m>= n*math.log(n,2):
            return "AC"
    else:
        if m>= n:
            return "AC"
    return "TLE"
m1,n1,t1 = [int(x) for x in input().split()]
print(tute(m1,n1,t1))


    