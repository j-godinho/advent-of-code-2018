import argparse
import re

def receive_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="path for input file", type=str, required=True)
	args = parser.parse_args()
	return args

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

### End operations

def read_file(args):
	file = open(args.input, 'r')
	return file.readlines()

def contains_more_than_one(mapping):
    for k,v in mapping.items():
        if(len(v)>1):
            return True
    return False

def process_file(file):
    first_part = file[:3260]
    second_part = file[3262:]

    mapping = {}
    after = None

    # Opcode possibilities
    for i in range(0, len(first_part) - 3, 4):
        before = [int(i) for i in re.findall(r'-?\d+', first_part[i])]
        instr = [int(i) for i in re.findall(r'-?\d+', first_part[i+1])]
        after = [int(i) for i in re.findall(r'-?\d+', first_part[i+2])]
        
        run_operations(before, instr, after, mapping)

    # Remove ambiguities
    while(contains_more_than_one(mapping)):
        for i in range(16):
            op_list = mapping[i]
            if(len(op_list) == 1):
                for j in range(16):
                    if(i!=j):
                        mapping[j] = list(set(mapping[j]) - set(op_list))

    # Run last input
    for i in range(len(second_part)):
        op, a, b, c = [int(i) for i in re.findall(r'-?\d+', second_part[i])]
        instr = mapping[op][0]
        after[c] = instr(a,b,after)

    return after, after[0]

def run_operations(before, instr, after, mapping):
    code, a, b, c = instr
    available = []
    for op in operations:
        temp = before[:]
        temp[c] = op(a,b,before)
        if(temp == after):
            available.append(op)

    if(code in mapping.keys()):
        mapping[code] = list(set(available).intersection(mapping[code]))
    else:
        mapping[code] = available
    
def main():
	args = receive_input()
	file = read_file(args)
	print(process_file(file))
main()
