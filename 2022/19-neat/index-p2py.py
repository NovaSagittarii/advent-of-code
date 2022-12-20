"""
2-input XOR example -- this is most likely the simplest possible example.
"""

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

import neat
# import visualize
import pickle
import gzip

# import simulation
import random
import copy
import datetime
import multiprocessing

# print(multiprocessing.cpu_count())
# exit()

# print(datetime.datetime.now().hour)
# exit()


# 2-input XOR inputs and expected outputs.
# xor_inputs = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
# xor_outputs = [(0.0,), (1.0,), (1.0,), (0.0,)]

sample = '''4 2 3 14 2 7
2 3 3 8 3 12'''
real = '''4 4 4 17 4 20
3 3 2 12 2 10
3 3 2 20 3 18
3 3 3 19 3 17
3 4 4 18 3 13
2 4 2 16 2 9
4 3 3 14 4 17
3 4 4 18 3 8
4 4 2 9 3 15
4 4 2 15 3 16
2 4 3 19 4 13
3 3 4 19 4 7
3 4 2 15 3 7
3 4 3 10 2 7
4 4 2 10 3 14
4 4 4 5 3 7
4 4 3 20 2 10
4 3 3 15 2 13
4 4 2 14 4 19
4 4 4 18 4 9
3 4 3 20 3 14
4 3 4 8 3 7
2 4 3 19 4 8
4 4 4 5 2 10
4 3 4 8 2 8
3 4 4 14 4 10
2 4 4 18 2 11
3 3 2 16 3 14
2 3 3 18 2 19
2 4 4 11 3 8'''

ruleset = tuple(map(lambda l: tuple(map(int, l.split(' '))), sample.split('\n')))

def play_game(net, rules, debug=False):
    if debug: print(rules)
    resources = [0, 0, 0, 0]
    bots = [1, 0, 0, 0]
    for t in range(1,32+1):
        res = net.activate((t, *resources, *bots, *rules))
        choice = 0
        oldbots = bots[::]
        for i in range(len(res)):
            if res[i] > res[choice]: choice = i
        if choice == 1 and resources[0] >= rules[0]:
            resources[0] -= rules[0]
            bots[0] += 1
            if debug: print(t, resources, bots, "buy orebot")
        elif choice == 2 and resources[0] >= rules[1]:
            resources[0] -= rules[1]
            bots[1] += 1
            if debug: print(t, resources, bots, "buy claybot")
        elif choice == 3 and resources[0] >= rules[2] and resources[1] >= rules[3]:
            resources[0] -= rules[2]
            resources[1] -= rules[3]
            bots[2] += 1
            if debug: print(t, resources, bots, "buy obibot")
        elif choice == 4 and resources[0] >= rules[4] and resources[2] >= rules[5]:
            resources[0] -= rules[4]
            resources[2] -= rules[5]
            bots[3] += 1
            if debug: print(t, resources, bots, "buy geobot")
        for i in range(len(bots)): resources[i] += oldbots[i] # distribute resources
    return resources[3] # + min(0.99,resources[2]/1000+resources[1]/100000)

def eval_genome(genome, config, rules):
    # genome.fitness = 0.0
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    res = play_game(net, rules)
    # genome.fitness += res
    return res

def eval_genomes(genomes, config, rules):
    for _, genome in genomes: genome.fitness = 0.0
    for i, (genome_id, genome) in enumerate(genomes[:3]):
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        played = 0
        # for rules in ruleset[:2]:
        #     res = play_game(net, rules)
        #     played += 1
        #     genome.fitness += res
        res = play_game(net, rules)
        #played += 1
        genome.fitness += res
        #genome.fitness /= played

    #for genome_id, genome in genomes:
    #    genome.fitness = 4.0
    #    net = neat.nn.FeedForwardNetwork.create(genome, config)
    #    for xi, xo in zip(xor_inputs, xor_outputs):
    #        output = net.activate(xi)
    #        genome.fitness -= (output[0] - xo[0]) ** 2


def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    qual = 0
    a = [] # postprint

    for i, rule in enumerate(ruleset):
        i += 1
        rulestr = '(' + ",".join(map(str,rule)) + ')'
        filename = f"best{rulestr}.pickle"
        os.system("title " + f"solving {i} - {rulestr}")

        if False and os.path.exists(filename): print("exists file", filename)
        # p = neat.Checkpointer.restore_checkpoint(filename if os.path.exists(filename) else 'neat-checkpoint-200')
        p = neat.Population(config)

        # pe = neat.ThreadedEvaluator(8, lambda a,b:eval_genome(a,b,rule))
        # winner = p.run(pe.evaluate, 10)
        # pe.stop()

        # pe = neat.ParallelEvaluator(multiprocessing.cpu_count(), lambda a,b:eval_genome(a,b,rule))
        # winner = p.run(pe.evaluate, 10)

        winner = p.run(lambda a,b:eval_genomes(a,b,rule), 2000)

        winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

        # with gzip.open(filename, 'w', compresslevel=5) as f:
        #     data = (p.generation, p.config, p.population, p.species, random.getstate())
        #     pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

        # with open(filename, "wb") as f:
        #    pickle.dump(p, f)

        res = play_game(winner_net, rule, not True)
        a.append(" ".join(map(str, (i, int(res), res, rulestr))))
        qual += i*int(res)
    print("\n".join(a))
    print(qual)
    with open('output-p2', 'w') as f:
        f.write("\n".join([*a, str(qual)]))

if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward-sim')
    run(config_path)
    # while datetime.datetime.now().hour < 20:
    #     run(config_path)
    #     # break