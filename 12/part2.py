import argparse
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from copy import deepcopy
from tqdm import tqdm

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	file = file.readlines()
	state = file[0].split()[-1]
	combs = {}
	for l in file[2:]:
		split = l.split()
		combs[split[0]] = split[-1]
	return state, combs
	
def process_file(state, combs):
	extended_state = '.'*3000 + state + '.' * 3000
	state =  np.array(list(extended_state))
	central = np.nonzero(state == '#')[0][0]
	
	num_gens = 2500
	pat_len = 5

	scores = []
	its = []
	
	for i in tqdm(range(num_gens)):
		changes = []
		temp = np.copy(state)

		for j in range(len(state)-pat_len):
			pattern = "".join(state[j:j+pat_len])
			if(pattern in combs):
				changes.append((j+2,combs[pattern]))

		for c in changes:
			state[c[0]] = c[1]

		scores.append(score(state, central))
		its.append(i)

	# There is a stabilization after a few iterations: 110
	stable = 111
	stabilization = scores[stable] - scores[stable - 1]
	return (50000000000-1-stable)* stabilization + scores[stable]
	
def predict_result(iteration, scores, its):
	x_train = np.array(its).reshape(-1,1)
	y_train = np.array(scores).reshape(-1,1)

	print(x_train.shape, y_train.shape)
	regr = linear_model.LinearRegression()
	regr.fit(x_train, y_train)

	print("%.0f" % regr.predict(iteration)) 

def score(state, central):
	result = 0
	for i in range(len(state)):
		if(state[i] == '#'):
			index = i-central
			result += index
	return result

def main():
	args = receive_input()
	state, combs = read_file(args)
	print(process_file(state, combs))

main()