import job_shop_genetic_algorithm
from mutation import Mutation


class Techniques:
    def __init__(self, description, selection, mutation: Mutation, crossover):
        self.description = description
        self.crossover = crossover
        self.mutation = mutation
        self.selection = selection

