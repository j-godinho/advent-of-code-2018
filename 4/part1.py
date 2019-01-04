import argparse
import numpy as np
import re
import random
from datetime import datetime, timedelta
from collections import defaultdict

class Entry():
	def __init__(self, date, rest):
		self.date = date
		self.rest = rest

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def process_file(file):
	# Order by date
	file.sort(key=lambda x: datetime.strptime(x.replace('[',']').split(']')[1], "%Y-%m-%d %H:%M"))
	
	time_slept = defaultdict(lambda:timedelta(0), {})
	started_sleeping = dict()
	most_recent = None
	ocurrences = defaultdict(lambda:[], {})

	prog = re.compile(r"\[(.+)\]\s(.+)")
	for line in file:
		match = prog.match(line)
		date, rest = match.group(1,2)
		date = datetime.strptime(date, "%Y-%m-%d %H:%M")
		result = parse_line(rest)
		
		if(result == -1):
			started_sleeping[most_recent] = date
			ocurrences[most_recent].append(date.minute)
		elif(result == -2):
			time_slept[most_recent] += (date - started_sleeping[most_recent])
			ocurrences[most_recent].append(date.minute)
		else:
			most_recent = result

	sleeper = find_sleeper(time_slept)
	time = build_matrix(ocurrences[sleeper])

	return sleeper * time

def build_matrix(ocurrences):
	matrix = np.zeros((50,))
	for i in range(0, len(ocurrences)-1, 2):
		matrix[ocurrences[i]:ocurrences[i+1]] += 1
	return np.argmax(matrix)

def find_sleeper(time_slept):
	minimum = timedelta()
	sleeper = None
	for k, v in time_slept.items():
		if(time_slept[k] > minimum):
			sleeper = k
			minimum = time_slept[k]
	return sleeper

def parse_line(line):
	splited = line.split()
	if(len(splited) == 2):
		if(splited[0]=="falls"):
			return -1
		else:
			return -2
	else:	
		return int(splited[1][1:])

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()