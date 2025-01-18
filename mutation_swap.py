import random

from mutation import Mutation


class SwapMutation(Mutation):

    def mutation(self, schedule):
        """Performs swap mutation."""
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(schedule)), 2)
            schedule[i], schedule[j] = schedule[j], schedule[i]