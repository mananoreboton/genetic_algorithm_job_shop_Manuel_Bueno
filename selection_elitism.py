from selection import Selection


class SelectionElitism(Selection):

    def selection(self, population, fitness, num_elites=1):
        elites = sorted(zip(population, fitness), key=lambda x: x[1])[:num_elites]
        return [elite[0] for elite in elites]