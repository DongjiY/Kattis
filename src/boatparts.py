# should use sets

def boat(p,n):
    uniqueParts = []
    for x in range(n):
        thisInput = input()
        if thisInput not in uniqueParts:
            uniqueParts.append(thisInput)
            if len(uniqueParts) == p:
                return x+1
    return "paradox avoided"

p,n = [int(x) for x in input().split()]
print(boat(p,n))
