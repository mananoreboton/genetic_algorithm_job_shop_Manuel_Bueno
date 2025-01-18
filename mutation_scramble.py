import random

from mutation import Mutation


class ScrambleMutation(Mutation):

    def mutation(self, schedule):
        i, j = sorted(random.sample(range(len(schedule)), 2))
        segment = schedule[i:j+1]
        random.shuffle(segment)
        schedule[i:j+1] = segment
        return schedule