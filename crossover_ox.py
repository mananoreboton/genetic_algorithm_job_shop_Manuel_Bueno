import random

from crossover import Crossover


class OXCrossover(Crossover):

    def crossover(self, parent1, parent2):
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child = [None] * len(parent1)
        child[start:end] = parent1[start:end]
        ptr = end
        for gene in parent2:
            if gene not in child:
                if ptr == len(parent1):
                    ptr = 0
                child[ptr] = gene
                ptr += 1
        return child
