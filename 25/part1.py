import argparse
import re
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from matplotlib import pyplot as plt
 
def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def process_file(file):
    file = np.array([[int(i) for i in re.findall(r'-?\d+', line)] for line in file])
    
    z = linkage(file, metric='cityblock')
    clusters = fcluster(z, 3, criterion="distance")
    
    #fig = plt.figure()
    #dn = dendrogram(z)
    #plt.show()

    return len(set(clusters))

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
