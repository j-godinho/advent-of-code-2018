import argparse
import re
import numpy as np
from copy import deepcopy

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

	def __repr__(self):
		if self.group_type == 0:
			group = "Immune"
		else:
			group = "Infection"
		return "{} group contains {} units".format(group, self.units)


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
	for boost in range(1, 10000):
		temp_group = deepcopy(groups)
		for g in temp_group:
			if(g.group_type == 0):
				g.att_damage += boost
		
		last = None
		stalemate = False
		while len(set([x.group_type for x in temp_group])) > 1 and not stalemate:
			temp_group.sort(key=lambda x: (- x.power(), -x.initiative))
			
			attacks = dict()
			for elem in temp_group:

				enemies = [x for x in temp_group if x.group_type != elem.group_type]

				possibilities = [x for x in enemies if elem.att_type not in x.immunities and x not in attacks.values()]

				if len(possibilities) == 0:
					continue

				possibilities.sort(key=lambda x: (-x.power(), -x.initiative))
				damage = [elem.attack(x) for x in possibilities]
		
				chosen_index = np.argmax(np.array(damage))
				chosen = possibilities[chosen_index]
				attacks[elem] = chosen

			temp_group.sort(key= lambda x: (-x.initiative))
			
			for elem in temp_group:
				if elem.units > 0:
					if elem in attacks.keys():
						attacked = attacks[elem]
						damage = elem.attack(attacked)
						killed = damage // attacked.points
						attacks[elem].units = max(0, attacked.units - killed)
			
			# Check for stalemate				
			temp_group = [x for x in temp_group if x.units > 0]

			units_immune = sum([x.units for x in temp_group if x.group_type == 0])
			units_infect = sum([x.units for x in temp_group if x.group_type == 1])
			temp = (units_immune, units_infect)
			if temp == last:
				stalemate = True
			last = temp[:]

		if(len(set([x.group_type for x in temp_group])) == 1):
			if(0 in set([x.group_type for x in temp_group])):
				return sum([x.units for x in temp_group])

def main():
	args = receive_input()
	file = read_file(args)
	groups = process_file(file)
	print(run_simulation(groups))

main()
