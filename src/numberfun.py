
def ispossible(val1,val2,val3):
    if val1+val2==val3 or val1-val2==val3 or val1/val2==val3 or val1*val2==val3 or val2-val1==val3 or val2/val1==val3:
        return "Possible"
    else:
        return "Impossible"

nums = int(input())
for x in range(nums):
    num1,num2,ans = [int(i) for i in input().split()]
    print(ispossible(num1,num2,ans))
        
        
        
        
    # signs = ['+','-','/','*']
    # for i in range(len(signs)):
    #     strmath = val1+signs[i]+val2
    #     strmath2 = val2+signs[i]+val1
    #     if eval(strmath) == int(val3) or eval(strmath2) == int(val3):
    #         return True