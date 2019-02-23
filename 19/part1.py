import argparse
import re

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def process_file(file):
    index = int(file[0].split()[-1])
    file = file[1:]

    before = [1, 0 ,0 ,0 ,0 ,0 ]
    p = before[index]
    while(p < len(file)):
        before[index] = p
        instr = file[p].split()
        run_operations(before, instr)
        p = before[index]
        p += 1

    return before[0]

### Operations
def addr(a, b, before): return before[a] + before[b]
def addi(a, b, before): return before[a] + b
def mulr(a, b, before): return before[a] * before[b]
def muli(a, b, before): return before[a]*b
def banr(a, b, before): return before[a] & before[b]
def bani(a, b, before): return before[a] & b
def borr(a, b, before): return before[a] | before[b]
def bori(a, b, before): return before[a] | b
def setr(a, b, before): return before[a]
def seti(a, b, before): return a
def gtir(a, b, before): return 1 if (a > before[b]) else 0
def gtri(a, b, before): return 1 if (before[a] > b) else 0
def gtrr(a, b, before): return 1 if (before[a] > before[b]) else 0
def eqir(a, b, before): return 1 if (a == before[b]) else 0
def eqri(a, b, before): return 1 if (before[a] == b) else 0
def eqrr(a, b, before): return 1 if (before[a] == before[b]) else 0

operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def run_operations(before, instr):
    op, a, b, c = instr[0], int(instr[1]), int(instr[2]), int(instr[3])
    before[c] = globals()[op](a,b,before)
    
def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
