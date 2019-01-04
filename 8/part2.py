import argparse

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.read().split()
	
def recursive_read(file):
	childs, metadata = file[:2]
	file = file[2:]
	value = 0
	scores = []

	for i in range(childs):
		total, file, score = recursive_read(file)
		value += total
		scores.append(score)

	value += sum(file[:metadata])

	if(childs == 0):
		return value, file[metadata:], sum(file[:metadata])
	else:
		return value, file[metadata:], sum([scores[i-1] for i in file[:metadata] if i>0 and i<=len(scores)])

def process_file(file):
	file = [int(x) for x in file]
	return recursive_read(file)[2]

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()