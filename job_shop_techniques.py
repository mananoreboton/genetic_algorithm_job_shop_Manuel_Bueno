from crossover import Crossover
from mutation import Mutation
from selection import Selection


class Techniques:
    def __init__(self, selection: Selection, mutation: Mutation, crossover: Crossover):
        self.crossover = crossover
        self.mutation = mutation
        self.selection = selection

    def description(self):
        return f"""
        Crossover: {self.crossover.__class__.__name__}
        Mutation:  {self.crossover.__class__.__name__}
        Selection: {self.selection.__class__.__name__}
        """

