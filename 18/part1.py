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

def process_file(file):
    its = 10
    mapping = np.array([[x for x in line] for line in file])

    for i in range(its):
        changes = []
        for y in range(len(mapping)):
            for x in range(len(mapping[0])):
                elem = mapping[y][x]
                xmin = (x-1) if (x-1 >= 0) else 0
                xmax = (x+2) if ((x+2) < len(mapping[0])) else len(mapping[0])
                ymin = (y-1) if (y-1 >= 0) else 0
                ymax = (y+2) if ((y+2)<len(mapping)) else len(mapping)

                slicing = mapping[ymin : ymax, xmin : xmax].reshape((-1,))
                counter = collections.Counter(slicing)
                counter[elem]-=1
                
                if(elem == '.' and counter['|']>=3):
                    changes.append((y,x,'|'))

                elif(elem == '|' and counter['#']>=3):
                    changes.append((y,x,'#'))

                elif(elem == '#'):
                    if(counter['#']>=1 and counter['|']>=1):
                        changes.append((y,x,'#'))
                    else:
                        changes.append((y,x,'.'))

        for c in changes:
            mapping[c[0]][c[1]] = c[2]

    final = collections.Counter(mapping.reshape((-1,)))
    return final['|'] * final['#']    
    
def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
