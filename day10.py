import re

with open("day10.in") as f:
    lines = [x.strip() for x in f.readlines()]

lines = [[int(i) for i in re.findall('-?\d+', l)] for l in lines]

pts = [[x[0], x[1]] for x in lines]
vs = [[x[2], x[3]] for x in lines]


def lim(l):
    return min(l), max(l)

def print_message(points):
	(min_x, min_y), (max_x, max_y) = lim(zip(*points))
	for y in xrange(min_y, max_y + 1):
		line = ""
		for x in xrange(min_x, max_x + 1):
			if [x,y] in points:
				line += "#"
			else:
				line += " "
		print line

def add(l1, l2):
	return [a+b for a, b in zip(l1,l2)]


max_height = 20 
time = 0

while True:
    hh = lim(zip(*pts))
    print hh
    (min_x, min_y), (max_x, max_y) = hh
    if abs(max_y - min_y) < max_height:
        # means we reached text dimension = min size
		break

    pts = [add(p, v) for p, v in zip(pts, vs)]
    time += 1

print_message(pts)
print time
