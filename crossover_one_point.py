import random

from crossover import Crossover


class OnePointCrossover(Crossover):

    def crossover(self, parent1, parent2):
        """Performs one-point crossover."""
        point = random.randint(0, len(parent1) - 1)
        child = parent1[:point] + [op for op in parent2 if op not in parent1[:point]]
        return child