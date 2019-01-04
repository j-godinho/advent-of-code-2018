import argparse
import numpy as np
from collections import defaultdict

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.read().split('\n')

def process_file(file):

	ocurrences = [0, 0]
	for line in file:
		word_dict = defaultdict(lambda:0, {})
		temp = [0, 0]
		for word in line:
			word_dict[word] += 1
		
		for k, v in word_dict.items():
			if(word_dict[k] == 2):
				temp[0] = 1
			if(word_dict[k] == 3):
				temp[1] = 1
		ocurrences[0] += temp[0]
		ocurrences[1] += temp[1]
		
	return ocurrences[0] * ocurrences[1]



def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()