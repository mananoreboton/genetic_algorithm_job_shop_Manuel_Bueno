import crossover_1
import fitness_1
import mutation_1
import selection_1
from fitness_1 import Fitness1
from job_shop_genetic_algorithm import GeneticAlgorithm
from job_shop_data import JobShopData
from job_shop_techniques import Techniques
from mutation_1 import Mutation1

techniques_combinations = [
    Techniques(
        description="Combination 1 of techniques",
        selection=selection_1.selection,
        mutation=Mutation1(mutation_rate=0.2),
        crossover=crossover_1.crossover
    )
]

def evaluate_techniques(job_shop_data: JobShopData):
    for techniques in techniques_combinations:
        genetic_algorithm = GeneticAlgorithm(
            job_shop_data=job_shop_data,
            population_size=50,
            generations=100,
            crossover_rate=0.8
        )
        print(f"Executing genetic algorithm with techniques: {techniques.description}")
        fitness = Fitness1(job_shop_data)
        best_population, best_fitness = genetic_algorithm.evolve(techniques=techniques, fitness=fitness)
        print("Best Solution:", best_population)
        print("Best Fitness (Makespan):", best_fitness)
