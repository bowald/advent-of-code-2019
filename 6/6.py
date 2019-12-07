from collections import defaultdict

data = [l.rstrip().split(')') for l in open('input.txt')]
# data = [l.rstrip().split(')') for l in open('test.txt')]
# data = [l.rstrip().split(')') for l in open('test2.txt')]

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance
    self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path


def get_parents(start, orbits):
    if start not in orbits:
        return []
    p = orbits[start]
    return [p] + get_parents(p, orbits)


g = Graph() 
orbits = {}

for parent, child in data:
    g.add_node(parent)
    g.add_node(child)
    g.add_edge(child, parent, 1)
    orbits[child] = parent



#part 1
total = 0
for child in orbits.keys():
    total += len(get_parents(child, orbits))
print(total)

#part 2
visited, path = dijsktra(g, 'YOU')
print(visited['SAN'] - 2)