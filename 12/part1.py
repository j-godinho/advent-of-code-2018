import argparse

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
	extended_state = '.'*20 + state + '.' * 20
	state =  list(extended_state)
	central = state.index('#')
	num_gens = 20
	pat_len = 5
	print("Initial state:\t", ''.join(state))
	for i in range(num_gens):
		changes = []
		for j in range(len(state)-pat_len):
			pattern = "".join(state[j:j+pat_len])
			if(pattern in combs):
				changes.append((j+2,combs[pattern]))

		for c in changes:
			state[c[0]] = c[1]
	
	print("State after:\t", "".join(state))

	final = 0
	for i, elem in enumerate(state):
		if(elem == '#'):
			index = i-central
			final+=index
	return final

def main():
	args = receive_input()
	state, combs = read_file(args)
	print(process_file(state, combs))

main()