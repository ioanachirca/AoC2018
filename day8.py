with open("day8.in") as f:
    license = [int(x) for x in f.readline().strip().split()]
index = 0
metadata_sum = 0

class Node:
    def __init__(self, nr_kids, nr_metadata):
        self.nr_kids = nr_kids
        self.nr_metadata = nr_metadata
        self.kids = []
        self.metadata = []
        self.value = 0


# returns node, new_index
def create_node(idx):
    global license
    global metadata_sum
    node = Node(license[idx], license[idx+1])
    new_idx = idx + 2
    # process children
    for i in range (node.nr_kids):
        new_node, new_idx = create_node(new_idx)
        node.kids.append(new_node)

    # process metadata
    node.metadata = license[new_idx: new_idx + node.nr_metadata]
    metadata_sum += sum(node.metadata)

    if node.nr_kids == 0:
        node.value = sum(node.metadata)
    else:
        node.value = sum([node.kids[i - 1].value for i in node.metadata if i > 0 and i <= len(node.kids)])

    return node, new_idx + node.nr_metadata


root, _ = create_node(index)
print metadata_sum
print root.value
        