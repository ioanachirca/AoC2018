from collections import defaultdict

grid_serial_nr = 4172
grid_size = 300

def cell_power(x, y):
    rack_id = x + 10
    power = rack_id * y
    power += grid_serial_nr
    power *= rack_id
    power %= 1000
    power /= 100
    power -= 5
    return power

def square_power(x, y, size):
    total_power = 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            total_power += cell_power(i, j)
    return total_power

# part 1
max_power = -5 * 9
top_left = [-1, -1]
for x in range(1, grid_size - 2):
    for y in range(1, grid_size - 2):
        power = square_power(x, y, 3)
        if power > max_power:
            max_power = power
            top_left = [x, y]

print top_left

# part 2
p_sums = defaultdict(int)
for x in range(1, grid_size+1):
    for y in range(1, grid_size+1):
        p_sums[(x, y)] = cell_power(x, y) + p_sums[(x, y-1)] + p_sums[(x-1, y)] - p_sums[(x-1, y-1)]

max_power = -5
max_size = 1
top_left = [-1, -1]
for x in range(1, grid_size):
    for y in range(1, grid_size):
        max_pos_size = min(grid_size - x, grid_size - y)
        for size in range(1, max_pos_size):
            power = p_sums[(x + size, y + size)] + p_sums[(x, y)] - p_sums[(x+size, y)] - p_sums[(x, y+size)]
            if power > max_power:
                max_power = power
                top_left = [x, y]
                max_size = size

print top_left, max_size

