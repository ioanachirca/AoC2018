import string 

with open("day5.in") as f:
    line = f.readline().strip()

alphabet = string.ascii_lowercase
opposite = dict()
for c in alphabet:
    opposite[c.upper()] = c.lower()
    opposite[c.lower()] = c.upper()

def get_reduced_len(line):
    stack = []
    for c in line:
        if stack and c == opposite[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)

    return len(stack)

print get_reduced_len(line)

min_size = len(line)
for c in alphabet:
    copy_line = [x for x in line if x not in(c.lower(), c.upper())]
    size = get_reduced_len(copy_line)
    min_size = min(size, min_size)

print min_size
