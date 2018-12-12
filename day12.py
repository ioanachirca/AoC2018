with open("day12.in") as f:
    content = [x.strip() for x in f.readlines()]

state = [c for c in content[0].split()[2]]
good_rules = set(line[:5] for line in content[2:] if line[-1] == '#')
plants = set(i for i, p in enumerate(state) if p == '#')

def evolve(plants, rules):
    next_plants = set()
    start = min(plants)
    end = max(plants)
    for i in xrange(start - 3, end + 4):
        st = ''.join(['#' if i + k in plants else '.' for k in [-2, -1, 0, 1, 2]])
        if st in rules:
            next_plants.add(i)

    return next_plants

def hash(plants):
    st = ''
    for i in range(max(plants)):
        if i in plants:
            st += '#'
        else:
            st += '.'
    return st


# part 1
for i in range(20):
    plants = evolve(plants, good_rules)

print sum(plants)

# part 2 - doesn't work 
# configs = set()
# configs.add(hash(plants))
# i = 0
# while True:
#     plants = evolve(plants, good_rules)
#     i += 1
#     if hash(plants) in configs:
#         break
#     configs.add(hash(plants))

# print i

last_s = 0
plants = set(i for i, p in enumerate(state) if p == '#')
for i in xrange(500):
    plants = evolve(plants, good_rules)

    s = sum(plants)
    step = s - last_s
    print i, s, step
    last_s = s

# stabilized by now (at iter 168 )
itr = 168
s = 13788
final_s = s + step * (50000000000 - itr - 1)
print final_s


