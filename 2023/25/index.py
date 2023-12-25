import random
import math
import networkx as nx
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

graph = nx.Graph()
for line in lines:
    u, a = line.split(": ")
    for v in a.split():
        graph.add_edge(u, v, capacity=1)

nodes = tuple(graph.nodes)
while True:
    a, b = random.choices(nodes, k=2)
    cutsize, partitions = nx.minimum_cut(graph, a, b)
    if cutsize == 3:
        print(tuple(len(partition) for partition in partitions))
        print(math.prod(len(partition) for partition in partitions))
        break