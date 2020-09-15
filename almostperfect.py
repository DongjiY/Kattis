import sys

#when finding factors, you only need to go up to sqrt(value). The rest is filled in with the if statement.
def factors(num):
    factorlist = []
    for i in range(1,int(num**.5+1)):
        if num%i==0:
            if i != num/i:
                factorlist.append(i)
                factorlist.append(int(num/i))
            else:
                factorlist.append(i)
    factorlist.sort()
    factorlist.pop()
    return sum(factorlist)

for y in sys.stdin:
    x = int(y)
    # print(factors(x))
    if factors(x) == x:
        print(str(x)+" perfect")
    elif x-2 <= factors(x) and x+2 >= factors(x):
        print(str(x)+" almost perfect")
    else:
        print(str(x)+" not perfect")
