import operator
amount = [int(x) for x in input().split()]
req= [int(x) for x in input().split()]
ratios = map(operator.truediv, amount, req)
themin = min(ratios)
remain = []
for i in range(len(amount)):
    remain.append(amount[i] - (req[i] * themin))
print("{l[0]:.6f} {l[1]:.6f} {l[2]:.6f}".format(l=remain))