def binaryToDecimal(binary):     
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def flip(num):
    numString = str(num)
    flipped = ""
    for x in range(len(numString)-1,-1,-1):
        flipped += numString[x]
    return flipped

number = int(input())
decimalarray = bin(number)
decimalnum = str(decimalarray)
binnum = decimalnum[2:]
flippedbin = int(flip(binnum))
print(binaryToDecimal(flippedbin))


