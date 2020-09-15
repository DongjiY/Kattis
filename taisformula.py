nums = int(input())

totalvals = []
for i in range(nums):
    lineval = input().split()
    totalvals += lineval
total =0
for i in range(0,(2*nums)-3,2):
    sums = (float(totalvals[i+1]) + float(totalvals[i+3]))/2
    mult = (int(totalvals[i+2])-int(totalvals[i]))/1000
    total += sums*mult
print(total)