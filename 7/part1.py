import argparse
import numpy as np
import re
import random
import pandas as pd
from collections import defaultdict


def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def process_file(file):
	dependencies = defaultdict(list)
	preds = defaultdict(list)

	values = set()
	for line in file:
		splited = line.split()
		f, b = splited[1], splited[-3]
		
		values.add(f)
		preds[b].append(f)
		dependencies[f].append(b)
	
	queue = []
	keys = preds.keys()
	for v in values:
		if(v not in keys):
			queue.append(v)
	queue.sort()
	
	print(queue)
	order = []
	while(queue):
		elem = queue.pop(0)
		if(elem in order): continue
		order.append(elem)

		for dep in dependencies[elem]:
			if(can_execute(order, dep, dependencies)):
				queue.append(dep)
		queue.sort()

	return ("".join(order))

def can_execute(order, dep, dependencies):
	for k, v in dependencies.items():
		if((k not in order) and (dep in v)):
			return False
	return True


def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
