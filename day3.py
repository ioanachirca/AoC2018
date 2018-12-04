from collections import defaultdict
 # claim looks like this: #1373 @ 130,274: 15x26
with open("day3.in") as f:
    lines = f.readlines()

def add_rect(x, y, width, height, D):
    global overlaps
    for dx in range(width):
         for dy in range(height):
             D[(x + dx, y + dy)] += 1
             if D[(x + dx, y + dy)] == 2:
                 overlaps += 1

D = defaultdict(int)
overlaps = 0
for line in lines:
    words = line.split()
    x, y = words[2].split(',')
    x, y = int(x), int(y[:-1])
    width, height = [int(tmp) for tmp in words[3].split('x')]
    add_rect(x, y, width, height, D)

print overlaps

for line in lines:
    words = line.split()
    x, y = words[2].split(',')
    x, y = int(x), int(y[:-1])
    width, height = [int(tmp) for tmp in words[3].split('x')]
    ok = True
    for dx in range(width):
        for dy in range(height):
            if D[(x + dx, y + dy)] > 1:
                ok = False
    if ok:
        print words[0]
