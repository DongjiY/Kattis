dominant = {"A":11, "K":4, "Q":3, "J":20, "T":10, "9":14, "8":0, "7":0}
notdominant = {"A":11, "K":4, "Q":3, "J":2, "T":10, "9":0, "8":0, "7":0}
array = input().split()
nums = int(array[0])*4
dom = array[-1]
total = 0
for x in range(nums):
    value = input()
    if value[-1] == dom:
        total += dominant[value[0]]
    else:
        total += notdominant[value[0]]
print(total)