from itertools import permutations

def getPrimes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if prime[p] == True:
            for i in range(p*2,n+1,p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime

nums = int(input())
primes = getPrimes(9999999)
for x in range(nums):
    letters = []
    lettercombos = []
    currentnum = input()
    for y in currentnum:
        letters.append(y)
    # print(letters)
    for i in range(1,len(letters)+1):
        lettercombos += list(permutations(letters,i))
    # print(lettercombos)
    letternums = set([int("".join(x)) for x in lettercombos])
    # print(letternums)
    count = 0
    for x in letternums:
        if primes[x]:
            count += 1
    print(count)
