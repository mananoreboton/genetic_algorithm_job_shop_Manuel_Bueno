import random

from mutation import Mutation


class SwapMutation(Mutation):

    def mutation(self, schedule):
        """Performs swap mutation."""
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(schedule)), 2)
            op_i = schedule[i]
            op_j = schedule[j]
            if op_i[0] == op_j[0]:
                # If they belong to the same job, ensure no precedence is violated
                if (op_i[1] > op_j[1] and i < j) or (op_i[1] < op_j[1] and i > j):
                    return
            schedule[i], schedule[j] = schedule[j], schedule[i]