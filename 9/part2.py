import argparse

import collections
from collections import defaultdict, deque

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def process_file(file):
	debug = False
	if(debug):
		for l in file:
			splited = l.split()
			num_players, last, highscore = int(splited[0]), int(splited[6]), int(splited[-1])
			score = start_game(num_players, last)
			assert (score == highscore)
	else:
		splited = file[0].split()
		num_players, last = int(splited[0]), int(splited[6])*100
		score = start_game(num_players, last)
		return score

def start_game(num_players, last):
	game = deque([0])
	players = defaultdict(int)

	for marble in range(1, last + 1):
		p = marble % num_players

		if(marble % 23 == 0):
			game.rotate(7)
			players[p] += marble + game.pop()
			game.rotate(-1)
		else:
			game.rotate(-1)
			game.append(marble)

	return max_player(players)

def max_player(players):
	maximum = 0
	mvp = None
	for k, v in players.items():
		if(v > maximum):
			maximum = v
			mvp = k
	return maximum

def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
