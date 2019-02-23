import argparse
import numpy as np
 
def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def process_file(file):
	intersections = {}
	carts = find_carts(file)

	while(True):
		v = is_intersecting(carts)
		if(v != False):
			return v[::-1]
		move_carts(file, carts)

def is_intersecting(carts):
	for i in range(len(carts)):
		for j in range(i+1, len(carts)):
			pos1 = carts[i][0:2]
			pos2 = carts[j][0:2]
			if(pos1 == pos2):
				return pos1
	return False

def find_carts(field):
	# y,x,orientation,rotate
	carts = []
	symbols = {'>': 1, '<': -1, '^': 1j, 'v': -1j}
	for y in range(len(field)):
		for x in range(len(field[0])):
			elem = field[y][x]
			if(elem in symbols.keys()):
				carts.append([y, x, symbols[elem], 0])
	return carts

def move_carts(field, carts):
	for c in carts:

		orient = c[2]
		if(orient == -1):
			c[1] -= 1
		elif(orient == 1):
			c[1] += 1
		elif(orient == 1j):
			c[0] -= 1
		elif(orient == -1j):
			c[0] += 1

		pos = field[c[0]][c[1]]
		if(pos == '\\'):
			if(c[2].real == 0):
				c[2] *= 1j
			else:
				c[2] *= -1j
			
		elif(pos == '/'):
			if(c[2].real == 0):
				c[2] *= -1j
			else:
				c[2] *= 1j
		elif(pos == '+'):
			c[2] = c[2] * ((1j) * (-1j) ** c[3])
			c[3] = (c[3] + 1) % 3
		
		
def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()