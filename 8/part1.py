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

	for i in range(childs):
		total, file = recursive_read(file)
		value += total

	value += sum(file[:metadata])

	return value, file[metadata:]

def process_file(file):
	file = [int(x) for x in file]
	return recursive_read(file)[0]

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()