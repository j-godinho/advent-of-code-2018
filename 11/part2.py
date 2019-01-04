import numpy as np
from tqdm import tqdm

def get_digit(number, n):
    return number // 10**n % 10
    
def process_file(serial):
    grid = np.zeros((300,300))
    for y in range(len(grid)):
        for x in range(len(grid[0])):        
            grid[y][x] = calculate_power(x+1, y+1, serial)

    maximum = 0
    square = None
    for s in tqdm(range(300)):
        for y in range(0, len(grid)-s):
            for x in range(0, len(grid)-s):
                slicing = grid[y:y+s,x:x+s]
                result = np.sum(slicing)
                if(result > maximum):
                    maximum = result
                    square = (x+1, y+1, s)

    return square, maximum

def calculate_power(x, y, serial):
    index = x + 10
    power = index * y
    power += serial
    power *= index
    power = get_digit(power, 2) - 5
    return power

def main():
    serial = 7672
    print(process_file(serial))
main()