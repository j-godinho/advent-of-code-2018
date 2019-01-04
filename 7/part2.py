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

def process_file(file, num_workers):
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
	
	return scheduler(num_workers, queue, dependencies)

class Entry(object):
	def __init__(self, job, time):
		self.job = job
		self.time = time

	def reduce_time(self, period):
		self.time = self.time - period

	def __repr__(self):
		return "[{}: {}]".format(self.job, self.time)

def calculate_time(elem):
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	return letters.find(elem) + 60 + 1 

def remove_soonest(pool):
	minimum = float("+inf")
	index = None
	for i, entry in enumerate(pool):
		if(entry.time < minimum):
			minimum = entry.time
			index = i
	return index, minimum

def subtract_scores(pool, time):
	for entry in pool:
		entry.reduce_time(time)

def create_refill_pool(queue, num_workers, pool=[]):
	while(queue and len(pool)<num_workers):
		elem = queue.pop(0)
		pool.append(Entry(elem, calculate_time(elem)))
	return pool

def scheduler(num_workers, queue, dependencies):
	order = []
	t_time = 0

	while(queue or pool):
		pool = create_refill_pool(queue, num_workers)
		index, time = remove_soonest(pool)
		elem = pool[index].job
		order.append(elem)
		subtract_scores(pool, time)
		t_time += time	

		pool.pop(index)

		for dep in dependencies[elem]:
			if(can_execute(order, dep, dependencies)):
				queue.append(dep)
		queue.sort()
	return t_time

def can_execute(order, dep, dependencies):
	for k, v in dependencies.items():
		if((k not in order) and (dep in v)):
			return False
	return True

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file, num_workers=5))
main()
