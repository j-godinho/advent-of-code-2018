import argparse
import numpy as np
import re
import random
from tqdm import tqdm

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.read()

def find_units(text):
	units = set()
	for w in text:
		if(w.lower() not in units):
			units.add(w)
	return units

def react_units(text):
	stack = []
	for c in text:
		if(stack):
			first = ord(c)
			temp = ord(stack[-1])
			if(abs(first - temp)==32):
				stack.pop()
				continue
		stack.append(c)
	return len(stack)

def process_file(file):
	units = find_units(file)
	lengths = dict()
	for u in tqdm(units):
		temp_file = file[:]
		temp_file = temp_file.replace(u.upper(), u).replace(u, '')
		lengths[u] = react_units(temp_file)
	return min(lengths.items(), key=lambda x:x[1])		
	
def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()