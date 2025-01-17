import random

from mutation import Mutation


class Mutation1(Mutation):

    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate

    def mutation(self, schedule):
        """Performs swap mutation."""
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(schedule)), 2)
            schedule[i], schedule[j] = schedule[j], schedule[i]