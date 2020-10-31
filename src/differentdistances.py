vals = [float(x) for x in input().split()]
while vals != [0]: 
    pnorm = (((abs(vals[0]-vals[2]))**vals[4])+((abs(vals[1]-vals[3]))**vals[4]))**(1/vals[4])
    print(pnorm)
    vals = [float(x) for x in input().split()]
