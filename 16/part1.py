import argparse
import re

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()[:3260]

def process_file(file):
    total = 0

    for i in range(0, len(file) - 3, 4):
        before = [int(i) for i in re.findall(r'-?\d+', file[i])]
        instr = [int(i) for i in re.findall(r'-?\d+', file[i+1])]
        after = [int(i) for i in re.findall(r'-?\d+', file[i+2])]

        num = run_operations(before, instr, after)
        if(num >= 3):
            total += 1

    return total

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

def run_operations(before, instr, after):
    total = 0
    op, a, b, c = instr
    for op in operations:
        temp = before[:]
        temp[c] = op(a,b,before)
        if(temp == after):
            total += 1
    return total
    
def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
