import argparse
import numpy as np

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return np.array(file.readlines(), dtype=int)

def main():
	args = receive_input()
	file = read_file(args)
	print(np.sum(file))
	
main()