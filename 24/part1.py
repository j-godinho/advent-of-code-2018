import argparse
import re
import numpy as np

class Group:
	def __init__(self, units, points, weaknesses, immunities, att_damage, att_type, initiative, group_type):
		self.units = int(units)
		self.points = int(points)
		self.weaknesses = weaknesses
		self.immunities = immunities
		self.att_damage = int(att_damage)
		self.att_type = att_type
		self.initiative = int(initiative)
		self.group_type = group_type

	def attack(self, enemy):
		if self.att_type in enemy.immunities:
			return 0
		elif self.att_type in enemy.weaknesses:
			return self.power() * 2
		else:
			return self.power()

	def power(self):
		return self.units * self.att_damage


def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args


def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()


def process_file(file):
	rx = re.compile(r"(\d+) units each with (\d+) hit points( \((.+)\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)")
	immune = 0
	groups = []
	for l in file:
		if l == '\n':
			immune = 1
		else:
			match = rx.match(l)
			weaknesses_immunities = [[], []]
			if match:
				units, points, temp, att_damage, att_type, initiative = match.group(1, 2, 4, 5, 6, 7)
				if temp:
					temp = temp.replace('to ', ',')
					temp = temp.replace(';', ',')
					temp = temp.replace(',', '')
					index = 0
					for w in temp.split():
						if w == "weak":
							index = 0
						elif w == 'immune':
							index = 1
						else:
							weaknesses_immunities[index].append(w)
				elem = Group(units, points, weaknesses_immunities[0], weaknesses_immunities[1], att_damage, att_type, initiative, immune)

				groups.append(elem)
	return groups


def run_simulation(groups):
	while len(set([x.group_type for x in groups])) > 1:
		groups.sort(key=lambda x: (- x.power(), -x.initiative))
		
		attacks = dict()
		for elem in groups:

			enemies = [x for x in groups if x.group_type != elem.group_type]

			possibilities = [x for x in enemies if elem.att_type not in x.immunities and x not in attacks.values()]

			if len(possibilities) == 0:
				continue

			possibilities.sort(key=lambda x: (-x.power(), -x.initiative))
			damage = [elem.attack(x) for x in possibilities]
	
			chosen_index = np.argmax(np.array(damage))
			chosen = possibilities[chosen_index]
			attacks[elem] = chosen

		groups.sort(key= lambda x: (-x.initiative))

		for elem in groups:
			if elem.units > 0:
				if elem in attacks.keys():
					attacked = attacks[elem]
					damage = elem.attack(attacked)
					killed = damage // attacked.points
					attacks[elem].units = max(0, attacked.units - killed)

		groups = [x for x in groups if x.units > 0]
	return sum([x.units for x in groups])

def main():
	args = receive_input()
	file = read_file(args)
	groups = process_file(file)
	print(run_simulation(groups))

main()
