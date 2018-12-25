from collections import deque
import re

def dist(p1, p2):
    return sum([abs(a-b) for a, b in zip(p1, p2)])

with open("day25.in") as f:
    content = [line.strip() for line in f.readlines()]

points = [tuple(map(int, re.findall('-?\d+', line))) for line in content]

neighs = [set() for _ in range(len(points))]
for i in range(len(points)):
    for j in range(len(points)):
        if dist(points[i], points[j]) <= 3:
            neighs[i].add(j)

result = 0
visited = set() # holds indexes
for i in range(len(points)):
    if i in visited:
        continue
    # bfs to find all neighbors
    Q = deque([i]) # holds indexes
    while Q:
        idx = Q.popleft()
        if idx in visited:
            continue
        visited.add(idx)
        for neigh in neighs[idx]:
            Q.append(neigh)
    result += 1

print result


# import sys
# import re
# from collections import deque

# fname = sys.argv[1]
# P = []
# for line in open(fname).read().strip().split('\n'):
#     w,x,y,z = map(int, re.findall('-?\d+', line))
#     P.append((w,x,y,z))
# E = [set() for _ in range(len(P))]
# for i,(w1,x1,y1,z1) in enumerate(P):
#     for j,(w2,x2,y2,z2) in enumerate(P):
#         d = abs(w1-w2)+abs(x1-x2)+abs(y1-y2)+abs(z1-z2)
#         if d <= 3:
#             E[i].add(j)

# S = set()
# ans = 0
# for i in range(len(P)):
#     if i in S:
#         continue
#     ans += 1
#     Q = deque()
#     Q.append(i)
#     while Q:
#         x = Q.popleft()
#         if x in S:
#             continue
#         S.add(x)
#         for y in E[x]:
#             Q.append(y)
# print ans