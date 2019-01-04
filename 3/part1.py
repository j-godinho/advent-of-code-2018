import argparse
import numpy as np
import re

class Rectangle():
	def __init__(self, index, left, top, wide, tall):
		self.index = int(index)
		self.left = int(left)
		self.top = int(top)
		self.wide = int(wide)
		self.tall = int(tall)

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def draw_rectangle(rect, global_matrix):
	for i in range(rect.top, rect.top+rect.tall):
		for j in range(rect.left, rect.left + rect.wide):
			global_matrix[i][j] += 1

def process_file(file):
	global_matrix = np.zeros((1000,1000))
	prog = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")	

	for line in file:
		match = prog.match(line)
		index, left, top, wide, tall = match.group(1,2,3,4,5)
		rect = Rectangle(index, left, top, wide, tall)
		draw_rectangle(rect, global_matrix)
	
	print((global_matrix >= 2).sum())

def main():
	args = receive_input()
	file = read_file(args)
	process_file(file)
main()