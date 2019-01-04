import argparse
import numpy as np
import re
import random
from datetime import datetime, timedelta
from collections import defaultdict

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.read()

def process_file(file):
	index = contains(file)
	while(index != -1):
		file = file[:index] + file[index+2:]
		index = contains(file)
	return len(file)
	
def contains(text):
	for i in range(len(text)-1):
		if(abs(ord(text[i]) - ord(text[i+1])) == 32):
			return i
	return -1

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()