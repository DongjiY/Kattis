def backwards(numstring):
    backwardstring = ""
    for x in range(len(numstring)-1,-1,-1):
        backwardstring += numstring[x]
    return backwardstring

num1,num2 = [str(x) for x in input().split()]
num1back = int(backwards(num1))
num2back = int(backwards(num2))
print(max(num1back,num2back))