def toOct(num):
    try:
        octa = int(str(num),8)
    except ValueError:
        return 0
    else:
        return octa
def toHex(num):
    try:
        hexa = int(str(num),16)
    except ValueError:
        return 0
    else:
        return hexa

nums = int(input())
for x in range(nums):
    casenum, deca = [int(x) for x in input().split()]
    octal = toOct(deca)
    hexadecimal = toHex(deca)
    print(casenum, octal, deca, hexadecimal)
