from crossover import Crossover
from mutation import Mutation
from selection import Selection


class Techniques:
    def __init__(self, selection: Selection, mutation: Mutation, crossover: Crossover):
        self.crossover = crossover
        self.mutation = mutation
        self.selection = selection
        self.crossover_name = self.crossover.__class__.__name__
        self.mutation_name  = self.mutation.__class__.__name__
        self.selection_name = self.selection.__class__.__name__

    def description(self):
        return f"""
        {self.crossover_name}
        {self.mutation_name}
        {self.selection_name}
        """

