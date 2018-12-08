from collections import defaultdict
import bisect

with open("day7.in") as f:
    lines = [line.strip() for line in f.readlines()]

graph = defaultdict(list)

# line looks like: "Step P must be finished before step R can begin.""
def get_src_dest(line):
    words = line.split()
    src = words[1]
    dest = words[7]
    return src, dest

for line in lines:
    src, dest = get_src_dest(line)
    graph[src].append(dest)

def task1():
    in_degree = defaultdict(int)
    for src in graph.keys():
        if src not in in_degree:
            in_degree[src] = 0
        for node in graph[src]:
            in_degree[node] += 1

    ready = sorted([v for v, count in in_degree.items() if count == 0])
    order = ""
    print ready
    while ready:
        v = ready.pop(0)
        order += v

        for node in graph[v]:
            in_degree[node] -= 1

            if in_degree[node] == 0:
                bisect.insort(ready, node)

    print order

def task_time(task):
    return 61 + ord(task) - ord('A')

# task: [job, remaining_time]
WORKERS = 5
def task2():
    in_degree = defaultdict(int)
    for src in graph.keys():
        if src not in in_degree:
            in_degree[src] = 0
        for node in graph[src]:
            in_degree[node] += 1

    pending = sorted([[v, task_time(v)] for v, count in in_degree.items() if count == 0])
    running = []
    timestamp = 0

    running = pending[:WORKERS]
    pending = pending[WORKERS:]

    while running:
        for task in running:
            task[1] -= 1
            if task[1] == 0:
                # done with this task, look for others that were freed by it
                running = [x for x in running if x != task]
                for node in graph[task[0]]:
                    in_degree[node] -= 1
                    if in_degree[node] == 0:
                        bisect.insort(pending, [node, task_time(node)])
        
        while len(running) < WORKERS and pending:
            running.append(pending.pop(0))
        timestamp += 1

    print timestamp

task1()
task2()


