import random


def multi_point_crossover(parent1, parent2, points=2):
    indices = sorted(random.sample(range(1, len(parent1) - 1), points))
    child = parent1[:indices[0]]
    for i in range(points):
        segment = parent2[indices[i]:indices[i + 1] if i + 1 < points else None]
        child.extend([op for op in segment if op not in child])
    return child