def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

nums = int(input())
for x in range(nums):
    value = int(input())
    response = fact(value)
    tostring = str(response)
    print(tostring[-1])