with open("day1.in") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
# first
value = sum(content)
print value

# second
value = 0
seen = set()
repeated = False
repeated_value = -1
while True:
    for num in content:
        value += num
        if value in seen:
            repeated_value = value
            repeated = True
            break
        seen.add(value)
    if repeated:
        break

print repeated_value
