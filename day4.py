from collections import defaultdict

with open("day4.in") as f:
    lines = sorted([x.strip() for x in f.readlines()])

def get_minute(line):
    hour_minute = line.split()[1][:-1]
    return int(hour_minute.split(":")[1])

def get_guard(line):
    return int(line.split()[3][1:])

def get_key_with_max_value(D):
    best = None
    for k in D.keys():
        if best is None or D[k] > D[best]:
            best = k   
    return best


guard_minutes = defaultdict(int)
total_sleep = defaultdict(int)
current_guard = None
asleep = None

for line in lines:
    if "Guard" in line:
        current_guard = get_guard(line)
        asleep = None
    elif "falls asleep" in line:
        asleep = get_minute(line)
    elif "wakes up" in line:
        if asleep is None:
            continue
        awake = get_minute(line)
        for i in range(asleep, awake):
            guard_minutes[(current_guard, i)] += 1
        total_sleep[current_guard] += awake - asleep

# find guard that sleeps the most
guard = get_key_with_max_value(total_sleep)

# get minute slept the most by him
best = None
minute = None
for k, v in guard_minutes.items():
    if k[0] == guard:
        if best is None or v > best:
            best = v 
            minute = k[1]

print guard, minute

# get max guard-minute combination
guard, minute = get_key_with_max_value(guard_minutes)

print guard, minute
