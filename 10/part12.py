import argparse
import re
import matplotlib.pyplot as plt

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def process_file(file):
    file = [[int(i) for i in re.findall(r'-?\d+', line)] for line in file] 


    minimum = float('+inf')    
    index = None
    for i in range(30000):
        xx = [x + i*vx for (x,y,vx,vy) in file]
        yy = [y + i*vy for (x,y,vx,vy) in file]

        minx, maxx = min(xx), max(xx)
        miny, maxy = min(yy), max(yy)

        result = maxx-minx + maxy - miny 

        if(result<minimum):
            minimum = result
            index = i

    new_xx = [x + index*vx for (x,y,vx,vy) in file]
    new_yy = [y + index*vy for (x,y,vx,vy) in file]

    draw_letters(new_xx, new_yy)

    return index

def draw_letters(xx, yy):
    plt.scatter(yy, xx)
    plt.show()
    
def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()