import crossover_1
import fitness_1
import mutation_1
import selection_1
from job_shop_genetic_algorithm import GeneticAlgorithm
from job_shop_data import JobShopData
from job_shop_techniques import Techniques

techniques_combinations = [
    Techniques(
        fitness=fitness_1.fitness,
        selection=selection_1.selection,
        mutation=mutation_1.mutation,
        crossover=crossover_1.crossover
    )
]

def evaluate_techniques(job_shop_data: JobShopData):
    for techniques in techniques_combinations:
        genetic_algorithm = GeneticAlgorithm(
            job_shop_data=job_shop_data,
            population_size=50,
            generations=100,
            crossover_rate=0.8,
            mutation_rate=0.2
        )
        genetic_algorithm.evolve(techniques=techniques)