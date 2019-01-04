import numpy as np

def calculate_risk(depth, target):
	region = np.zeros((target[0]+1, target[1]+1), dtype=int)
	erosions = np.zeros((target[0]+1, target[1]+1), dtype=int)
	forbiddens = [(0,0), target]

	for y in range(len(region)):
		for x in range(len(region[0])):
			if((y, x) in forbiddens):
				region[y][x] = 0
			elif(y == 0):
				region[y][x] = x*16807
			elif(x == 0):
				region[y][x] = y*48271
			else:
				region[y][x] = erosions[y][x-1] * erosions[y-1][x]

			erosions[y][x] = (region[y][x] + depth) % 20183

	region = erosions%3
	
	return np.sum(region[:target[0]+1, :target[1]+1])

def main():
	depth = 9465
	target = (704, 13)
	print(calculate_risk(depth, target))

main()
