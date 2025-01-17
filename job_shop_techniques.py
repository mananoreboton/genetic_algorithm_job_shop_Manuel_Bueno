import job_shop_genetic_algorithm

class Techniques:
    def __init__(self, selection, mutation, crossover, fitness):
        self.fitness = fitness
        self.crossover = crossover
        self.mutation = mutation
        self.selection = selection

