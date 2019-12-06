tree = {}

# data = [l.rstrip().split(')') for l in open('input.txt')]
data = [l.rstrip().split(')') for l in open('test.txt')]

for parent, child in data:
    if parent in tree:
        tree[parent].extend(child)
    else:
        tree[parent] = [child]

def distance(tree, node, level):
    print(node)
    if node not in tree:
        return 0
    return level + sum([distance(tree, child, level) for child in tree[node]])


print(distance(tree, 'COM', 0))