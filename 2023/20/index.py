import math
import re
import sys
lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

nodes = {} # (type, outputs)
node_state = {} # incoming[] for &, state for %
for line in lines:
    label, outputs = line.split(' -> ')
    if label == 'broadcaster':
        node_type = 'b'
    else:
        node_type = label[0]
        label = label[1:]
    outputs = outputs.split(', ')
    nodes[label] = (node_type, outputs)
    for output in outputs:
        if output not in node_state:
            node_state[output] = {}
        node_state[output][label] = 0
for k, node in nodes.items():
    if node[0] == '%':
        node_state[k] = 0 # set state

sent = [0, 0]
for T in range(1000):
    q = []
    q.append(('broadcaster', 'broadcaster', 0))
    sent[0] += 1
    while len(q):
        nq = []
        for prev, u, pulse in q:
            # print(f"{prev} -({pulse})-> {u}")
            if u not in nodes:
                continue
            node_type, outgoing = nodes[u]
            if node_type == '%':
                if pulse == 0:
                    node_state[u] ^= 1
                    for v in outgoing:
                        nq.append((u, v, node_state[u]))
                        sent[node_state[u]] += 1
            elif node_type == '&':
                node_state[u][prev] = pulse
                newstate = 1 ^ min(node_state[u].values())
                for v in outgoing:
                    nq.append((u, v, newstate))
                    sent[newstate] += 1
            elif node_type == 'b':
                for v in outgoing:
                    newstate = 0
                    nq.append((u, v, newstate))
                    sent[newstate] += 1
        q = nq

print(sent)
print(sent[0]*sent[1])