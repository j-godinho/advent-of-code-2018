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
	return file.read().split('\n')

def process_input(regex):
    

def example_inputs():
    inputs = ["^WNE$", "^ENWWW(NEEE|SSE(EE|N))$", "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$", "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$", "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"]
    outputs = [3, 10, 18, 23, 31]

    for i in range(len(inputs)):
        r = process_input(inputs[i])
        assert (r == outputs[i])

def process_file(file):

    
def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
