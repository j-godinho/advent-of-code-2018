import numpy as np
import networkx as nx

def generate_region(depth, target):
	region = np.zeros((target[0]+50, target[1]+50), dtype=int)
	erosions = np.zeros((target[0]+50, target[1]+50), dtype=int)
	forbiddens = [(0,0), target]

	for y in range(len(region)):
		for x in range(len(region[0])):
			if((y, x) in forbiddens):
				region[y][x] = 0
			elif(y == 0):
				region[y][x] = x*16807
			elif(x == 0):
				region[y][x] = y*48271
			else:
				region[y][x] = erosions[y][x-1] * erosions[y-1][x]

			erosions[y][x] = (region[y][x] + depth) % 20183

	region = erosions%3
	
	return region

def find_path(region, target):
	G=nx.Graph()
	# 0 - climbing, 1-torch, 2-neither
	objects = [(0, 1), (0, 2), (1, 2)]
	for (y, x), value in np.ndenumerate(region):
		availables = objects[region[y][x]]
		G.add_edge((y, x, availables[0]), (y, x, availables[1]), weight=7)
		for elem in ((0,1), (1,0), (0, -1), (-1, 0)):
			t_y, t_x = y + elem[0], x + elem[1]
			if(0 <= t_y < len(region) and 0 <= t_x < len(region[0])):
				new_items = objects[region[t_y][t_x]]
				for it in set(availables).intersection(set(new_items)):
					G.add_edge((y, x, it), (t_y, t_x, it), weight=1)

	# From 0,0 with torch to target_y, target_x with torch
	return nx.dijkstra_path_length(G, (0,0,1), (target[0], target[1], 1))
				

def main():
	depth = 9465
	target = (704, 13)
	region = generate_region(depth, target)
	print(find_path(region, target))

main()