import collections
from collections import defaultdict, deque

def process_file(num):
	p1 = 0
	p2 = 1
	recipes = [3, 7]

	while(len(recipes) < (99999999)):
		elem1, elem2 = recipes[p1], recipes[p2]
		comb = elem1 + elem2
		digits = [int(x) for x in str(comb)]
		recipes.extend(digits)
		
		p1, p2 = (p1 + elem1 + 1) % len(recipes), (p2 + elem2 + 1) % len(recipes)
	
	return contains_input(recipes, num)

def contains_input(recipes, num):
	patt = [int(x) for x in str(num)]
	recipe_len = len(recipes)
	length = len(patt)

	if(length > recipe_len): return False
	for i in range(0, recipe_len-length + 1):
		if(recipes[i:i+length] == patt):
			return i
	return False

def main():
	num = 580741
	print(process_file(num))
main()
