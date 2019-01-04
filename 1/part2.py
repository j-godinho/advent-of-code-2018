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

def process_file(file):
	frequencies = set()
	cur = 0
	
	# First element
	frequencies.add(cur)
	
	while(1):
		for freq in file:
			cur += freq
			if(cur in frequencies):
				return cur
			frequencies.add(cur)
	return -1

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()