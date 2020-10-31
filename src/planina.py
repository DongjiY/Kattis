import math

iteration = int(input())
numofsquares = 4**iteration
squaresonaside = math.sqrt(numofsquares)
dots = (squaresonaside+1)**2
print(int(dots))