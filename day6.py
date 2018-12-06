from collections import defaultdict

with open("day6.in") as f:
    lines = [x.strip() for x in f.readlines()]

def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

points = set()
max_x = 0
max_y = 0
for line in lines:
    x, y = [z for z in line.split()]
    x, y = int(x[:-1]), int(y)
    points.add((x, y))
    max_x = max(max_x, x)
    max_y = max(max_y, y)

LIMIT = 10000
areas = defaultdict(int)
infinites = set()
best_safe_area = 0

for i in range(max_x + 1):
    for j in range(max_y + 1):
        # part 1
        distances = sorted([(manhattan_dist((i,j), point), point) for point in points])

        if len(distances) == 1 or distances[0][0] != distances[1][0]:
            closest_point = distances[0][1]
            areas[closest_point] += 1

            if i == 0 or i == max_x or j == 0 or j == max_y: # we are on the border
                infinites.add(closest_point)

        # part 2
        if sum([manhattan_dist((i, j), point) for point in points]) < LIMIT:
            best_safe_area += 1

print max(area for point, area in areas.items() if point not in infinites)
print best_safe_area
