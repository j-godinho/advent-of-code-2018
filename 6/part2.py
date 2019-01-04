import argparse
import numpy as np
import re
import random
import pandas as pd

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

	matrix = np.zeros((max_y, max_x))

	positions = parse_positions(file)

	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			d = distance((y, x), positions)
			if(d<10000):
				matrix[y][x] = 1

	return np.count_nonzero(matrix == 1)

def distance(pos, positions):
	result = 0
	for point in positions:
		result += (abs(pos[0]-point[0])+abs(pos[1]-point[1]))
	return result

def parse_positions(file):
	positions = []
	for index, row in file.iterrows():
		positions.append((row[1], row[0]))
	return positions

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()