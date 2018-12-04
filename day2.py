with open("day2.in") as f:
    lines = [line.strip() for line in f]

count_2 = 0
count_3 = 0

def count(s, nr):
    freqs = [0] * 26
    for c in s:
        freqs[ord(c)-ord('a')] += 1

    return nr in freqs

def close(s1, s2):
    dist = 0
    idx = -1
    for i in range (len(s1)):
        if s1[i] != s2[i]:
            dist += 1
            idx = i
        if dist == 2:
            return -1
    return idx

for s in lines:
    if count(s, 2):
        count_2 += 1
    if count(s, 3):
        count_3 += 1

print count_2 * count_3

result = ""
for i in range (len(lines) - 1):
    for j in range(i, len(lines)):
        idx = close(lines[i], lines[j])
        if idx >= 0:
            result = lines[i][0:idx] + lines[i][idx+1:]

print result
