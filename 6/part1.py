import argparse
import numpy as np
import re
import random
import pandas as pd

class Cell(object):
	def __init__(self):
		self.value = -1
		self.processed = False
		self.main = False

	def process(self):
		self.processed = True

	def set_value(self, value):
		self.value = value
		self.processed = False

	def is_main(self):
		self.main = True

	def other(self):
		letters = "abcdefg"
		if(self.value>=0):
			if(self.main):
				return str(letters[self.value]).upper()
			return str(letters[self.value])
		elif(self.value==-2):
			return "."
		else:
			return "x"
		#return "({}-{})".format(self.value, self.processed)
		#return "({})".format(self.value)

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	df = pd.read_csv(args.input, header=None)
	return df

def process_file(file):
	max_x, max_y = max(file[0]), max(file[1])
	num_points = len(file[0])
	print("Maximums: {}, {} | Num_points: {}".format(max_y, max_x, num_points))

	matrix = np.array([[Cell() for row in range(max_x + 2)] for column in range(max_y + 2)])

	positions = parse_positions(file)
	populate_matrix(matrix, positions)

	iterate2(matrix)

	finites = find_finites(matrix, num_points)

	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			matrix[y][x] = matrix[y][x].value

	maximum = None
	max_value = 0
	for f in finites:
		count = np.count_nonzero(matrix == f)
		if(count > max_value):
			max_value = count
			maximum = f
	return max_value

def parse_positions(file):
	positions = []
	for index, row in file.iterrows():
		positions.append((row[1], row[0]))
	return positions

def is_finish(matrix):
	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			if(matrix[y][x].value == -1):
				return False
	return True

def valid_position(matrix, pos):
	i, j = (pos[0], pos[1])
	if(i>=0 and i<len(matrix)):
		if(j>=0 and j<len(matrix[0])):
			return True
	return False

def lock_positions(matrix):
	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			cell = matrix[y][x]
			if(cell.value == -2 or cell.value >= 0):
				cell.process()

def iterate2(matrix):
	while(not is_finish(matrix)):
		for y in range(len(matrix)):
			for x in range(len(matrix[0])):
				cur = matrix[y][x]
				if(cur.value >= 0 and cur.processed):
					update_neighbors(matrix, (y, x), cur.value)
		lock_positions(matrix)
	print(matrix)


def update_cell(matrix, pos, value):
	y, x = (pos[0], pos[1])
	if(valid_position(matrix, pos)):
		cell = matrix[y][x]
		if(not cell.processed):
			if(cell.value == -1):
				cell.set_value(value)
			elif(cell.value>=0 and cell.value!=value):
				cell.set_value(-2)

def update_neighbors(matrix, pos, value):
	top = (pos[0]-1, pos[1])
	bottom = (pos[0]+1, pos[1])
	left = (pos[0], pos[1]-1)
	right = (pos[0], pos[1]+1) 

	update_cell(matrix, top, value)
	update_cell(matrix, bottom, value)
	update_cell(matrix, left, value)
	update_cell(matrix, right, value)
	
def find_finites(matrix, num_points):
	finites = set([x for x in range(num_points)])
	uniques(matrix[0], finites)
	uniques(matrix[len(matrix)-1], finites)
	uniques(matrix[:,0], finites)
	uniques(matrix[:,len(matrix[0])-1], finites)
	return finites

def uniques(array, finites):
	for elem in array:
		if(elem.value in finites):
			finites.remove(elem.value)

def populate_matrix(matrix, positions):
	for index, pos in enumerate(positions):
		cell = matrix[pos[0]][pos[1]]  
		cell.set_value(index)
		cell.is_main()
		cell.process()

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()