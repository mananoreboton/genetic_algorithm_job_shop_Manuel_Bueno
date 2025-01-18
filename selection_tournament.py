import random

from selection import Selection


class TournamentSelection(Selection):

    def selection(self, population, fitness):
        """Selects a parent using tournament selection."""
        tournament = random.sample(list(zip(population, fitness)), k=3)
        tournament.sort(key=lambda x: x[1])
        return tournament[0][0]