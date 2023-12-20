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

cycleN = {}
firstN = {}
sent = [0, 0]
for T in range(1, 1024*32+1):
    q = []
    q.append(('broadcaster', 'broadcaster', 0))
    # q.append(('a', 'sx', 0))
    # q.append(('a', 'fx', 0))
    # q.append(('a', 'gj', 0))
    # q.append(('a', 'tj', 0))
    sent[0] += 1
    while len(q):
        nq = []
        for prev, u, pulse in q:
            if pulse == 0: 
                if u == 'rx':
                    print('RX FOUND', T)
                    nq = []
                    break
            if pulse == 0:
                if u not in firstN: firstN[u] = T
                elif u not in cycleN: cycleN[u] = T - firstN[u]
            # print(f"{prev} -({pulse})-> {u}")
            if u not in nodes:
                continue
            node_type, outgoing = nodes[u]
            if node_type == '%':
                if pulse == 0:
                    node_state[u] ^= 1
                    for v in outgoing:
                        nq.append((u, v, node_state[u]))
                        # sent[node_state[u]] += 1
            elif node_type == '&':
                node_state[u][prev] = pulse
                newstate = 1 ^ min(node_state[u].values())
                for v in outgoing:
                    nq.append((u, v, newstate))
                    # sent[newstate] += 1
            elif node_type == 'b':
                for v in outgoing:
                    newstate = 0
                    nq.append((u, v, newstate))
                    # sent[newstate] += 1
        q = nq

for u in nodes.keys():
    if u not in firstN: firstN[u] = None
    for v in nodes[u][1]:
        if v not in firstN:
            firstN[v] = None
print(firstN)
print(cycleN)

# ahh i did not realize the input was 'nice'
ans2 = math.lcm(*[cycleN[r] for r in node_state['kz'].keys()])
print(ans2)