import argparse
import re
import numpy as np
import collections

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def process_file(file):
    file = np.array([[int(i) for i in re.findall(r'-?\d+', line)] for line in file])
    
    index = np.argmax(file[:,3])
    max_elem = file[index]
    
    total = 0
    for i, elem in enumerate(file):
    	total += inside_radius(elem, max_elem)
    return total

def inside_radius(elem, max_elem):
	maximum = max_elem[3]
	return (abs(elem[0]-max_elem[0]) + abs(elem[1]-max_elem[1]) + abs(elem[2]-max_elem[2]) <= maximum)

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
