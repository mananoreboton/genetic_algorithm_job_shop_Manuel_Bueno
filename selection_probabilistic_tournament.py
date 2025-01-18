import random

from selection import Selection


class ProbabilisticTournamentSelection(Selection):

    def selection(self, population, fitness):
        tournament = random.sample(list(zip(population, fitness)), 3)
        tournament.sort(key=lambda x: x[1])
        if random.random() < 0.8:
            return tournament[0][0]
        else:
            return random.choice(tournament)[0]