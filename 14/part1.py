import collections
from collections import defaultdict, deque

def process_file(num):
	p1 = 0
	p2 = 1

	recipes = [3, 7]

	while(len(recipes) < (num+10)):
		elem1, elem2 = recipes[p1], recipes[p2]
		comb = elem1 + elem2
		digits = [int(x) for x in str(comb)]
		recipes.extend(digits)
		
		p1, p2 = (p1 + elem1 + 1) % len(recipes), (p2 + elem2 + 1) % len(recipes)
		
	return "".join([str(x) for x in recipes[num:]])

def main():
	num = 580741
	print(process_file(num))
main()