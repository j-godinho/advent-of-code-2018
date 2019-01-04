import numpy as np

def get_digit(number, n):
    return number // 10**n % 10
    
def process_file(serial):
    grid = np.zeros((300,300))

    for y in range(len(grid)):
        for x in range(len(grid[0])):        
            grid[y][x] = calculate_power(x+1, y+1, serial)

    squares = np.zeros((297, 297))
    maximum = 0
    index = None

    for y in range(0, len(grid)-3):
        for x in range(0, len(grid)-3):
            slicing = grid[y:y+3,x:x+3]
            result = np.sum(slicing)
            if(result > maximum):
                maximum = result
                index = (x+1, y+1)

    return index, maximum

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