import random


def selection(population, fitness):
    """Selects a parent using tournament selection."""
    tournament = random.sample(list(zip(population, fitness)), k=3)
    tournament.sort(key=lambda x: x[1])
    return tournament[0][0]