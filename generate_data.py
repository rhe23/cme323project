import random

# Generates random integers:
#	n - number of integers generated
#	lowerBound - inclusive lower bound 
# 	upperBound - inclusive upper bound

def generateData(n, lowerBound, upperBound):
	return [random.randint(lowerBound, upperBound) for _ in range(n)]