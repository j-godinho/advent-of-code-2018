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
	for i, line in enumerate(file):
		for j in range(i, len(file)-1):
			if(dissimilarity(file[i], file[j])==1):
				return and_words(file[i], file[j])

def and_words(word1, word2):
	sim = ""
	for i in range(len(word1)):
		if(word1[i] == word2[i]):
			sim += word1[i]
	return sim

def dissimilarity(word1, word2):
	value = 0
	for i in range(len(word1)):
		if(word1[i] != word2[i]):
			value += 1
	return value

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()