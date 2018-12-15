last_iter = 409551

recipes = [3, 7]
first = 0
second = 1

# part 1
while len(recipes) < last_iter + 10:
    #print recipes, first, second
    new_recipe = recipes[first] + recipes[second]
    if new_recipe < 10:
        recipes.append(new_recipe)
    else:
        recipes.append(new_recipe / 10)
        recipes.append(new_recipe % 10)
    first = (first + 1 + recipes[first]) % len(recipes)
    second = (second + 1 + recipes[second]) % len(recipes)

result = ''
for i in range(last_iter, len(recipes)):
    result += str(recipes[i])

print result

# part 2
recipes = [3, 7]
first = 0
second = 1
sequence = str(last_iter)

seq_len = len(sequence)
#409551
#100000
last_iter_mask = 100000
cur = 37 
while True:
    #print recipes, first, second
    new_recipe = recipes[first] + recipes[second]
    if new_recipe < 10:
        recipes.append(new_recipe)
        cur = cur % last_iter_mask
        cur = cur * 10 + new_recipe
        if cur == last_iter:
            print len(recipes) - seq_len
            exit()
    else:
        recipes.append(new_recipe / 10)
        cur = cur % last_iter_mask
        cur = cur * 10 + new_recipe / 10
        if cur == last_iter:
            print len(recipes) - seq_len
            exit()
        recipes.append(new_recipe % 10)
        cur = cur % last_iter_mask
        cur = cur * 10 + new_recipe % 10
        if cur == last_iter:
            print len(recipes) - seq_len
            exit()
    first = (first + 1 + recipes[first]) % len(recipes)
    second = (second + 1 + recipes[second]) % len(recipes)


