import argparse
import re
import numpy as np
from z3 import *

import sys
sys.setrecursionlimit(1500)

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def z3_abs(x):
  return If(x >= 0, x, -x)

def process_file(file):
	file = np.array([[int(i) for i in re.findall(r'-?\d+', line)] for line in file])
	
	x, y, z = Ints('x y z')
	dist = Int('dist')
	cost = Int('cost')

	cost_expr = ""

	for i,elem in enumerate(file):
		x_t, y_t, z_t, r_t = elem[0], elem[1], elem[2], elem[3]
		cost_expr += If(z3_abs(x - x_t) + z3_abs(y - y_t) + z3_abs(z - z_t) <= r_t, 1, 0)

	opt = Optimize()
	opt.add(cost == cost_expr)
	opt.add(dist == distance((x,y,z)))
	opt.maximize(cost)
	opt.minimize(dist)
	opt.check()
	model = opt.model()
	pos = (model[x].as_long(), model[y].as_long(), model[z].as_long())

	return sum(pos)

def distance(elem):
	return z3_abs(elem[0]) + z3_abs(elem[1]) + z3_abs(elem[2])

def inside_radius(elem, max_elem):
	maximum = max_elem[3]
	return (abs(elem[0]-max_elem[0]) + abs(elem[1]-max_elem[1]) + abs(elem[2]-max_elem[2]) <= maximum)

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
