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
	def __str__(self):
		return ("Rect:{} {} {} {} | ".format(self.left, self.top, self.wide, self.tall))
def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def process_file(file):
	rectangles = []
	prog = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")	

	for line in file:
		match = prog.match(line)
		index, left, top, wide, tall = match.group(1,2,3,4,5)
		rect = Rectangle(index, left, top, wide, tall)
		rectangles.append(rect)
	
	for i in range(len(rectangles)):
		if(overlap_any(rectangles, i) == False):
			print(rectangles[i].index)

		
def overlap_any(rectangles, i):
	for j in range(len(rectangles)):
		if(i!=j):
			if(overlap(rectangles[i], rectangles[j])):
				return True
	return False

def overlap(rect1, rect2):
	h_over = (rect1.left < (rect2.left + rect2.wide)) and ((rect1.left + rect1.wide) > rect2.left)
	v_over = ((rect1.top + rect1.tall) > rect2.top) and (rect1.top < (rect2.top + rect2.tall))
	return h_over and v_over

def main():
	args = receive_input()
	file = read_file(args)
	process_file(file)
main()