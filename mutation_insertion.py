import random

from mutation import Mutation


class InsertionMutation(Mutation):

    def mutation(self, schedule):
        if random.random() < self.mutation_rate:
            i, j = sorted(random.sample(range(len(schedule)), 2))
            gene = schedule.pop(i)
            schedule.insert(j, gene)