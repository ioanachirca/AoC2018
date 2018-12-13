with open("day13.in") as f:
    content = [x for x in f.readlines()]

def add(l1, l2):
	return [a+b for a, b in zip(l1,l2)]

grid = [[c for c in line] for line in content]
height = len(grid)
print height
cars = []
# car = [pos, direction, next_turn_idx]
for y in range(height):
    for x in range(len(grid[y])):
        if grid[y][x] in ['<', '>']:
            cars.append([[y, x], grid[y][x], 0])
            grid[y][x] = '-'
        elif grid[y][x] in ['^', 'v']:
            cars.append([[y, x], grid[y][x], 0])
            grid[y][x] = '|'

move_seq = ['l', 's', 'r']
dirs = {'<':[0, -1], '>':[0, 1], '^':[-1, 0], 'v':[1, 0]} # useful for advancing

turns = { # useful for changing direction
    ('\\', '>') : 'v',
    ('\\', '^') : '<',
    ('\\', '<') : '^',
    ('\\', 'v') : '>',
    ('/', '^') : '>',
    ('/', '<') : 'v',
    ('/', '>') : '^',
    ('/', 'v') : '<',
    ('l', '>') : '^',
    ('r', '>') : 'v',
    ('l', '^') : '<',
    ('r', '^') : '>',
    ('l', 'v') : '>',
    ('r', 'v') : '<',
    ('l', '<') : 'v',
    ('r', '<') : '^',
    ('s', '<') : '<',
    ('s', '^') : '^',
    ('s', '>') : '>',
    ('s', 'v') : 'v',
} 

crash = None
while len(cars) > 1:
    cars = sorted(cars)
    crashed_cars = set() # holds indices
    for idx in range(len(cars)):
        if idx in crashed_cars:
            continue
        car = cars[idx]
        y, x = car[0]
        if grid[y][x] not in ['-', '|']:
            # have to turn
            if grid[y][x] == '+':
                new_dir = turns[(move_seq[car[2]], car[1])]
                car[2] = (car[2] + 1) % len(move_seq)
            else:
                new_dir = turns[(grid[y][x], car[1])]
            car[1] = new_dir

        # advance
        new_y, new_x = add([y, x], dirs[car[1]])
        # check for collision
        for i in range(len(cars)):
            if i in crashed_cars:
                continue
            c = cars[i]
            if [new_y, new_x] == c[0]:
                crashed = True
                if crash is None:
                    print "first crash: ", [new_x, new_y]
                crash = [new_y, new_x]
                crashed_cars.add(i)
                crashed_cars.add(idx)
                break       
        car[0] = [new_y, new_x]

    # remove crashed cars
    cars = [cars[i] for i in range(len(cars)) if i not in crashed_cars]


print cars
            

    