import crossover_1
import job_shop_plotter
import selection_1
from fitness_1 import Fitness1
from job_shop_genetic_algorithm import GeneticAlgorithm
from job_shop_data import JobShopData
from job_shop_techniques import Techniques
from mutation_1 import Mutation1

import job_shop_validator

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
        print(f"Executing genetic algorithm with techniques: {techniques.description}")
        fitness = Fitness1(job_shop_data)
        genetic_algorithm = GeneticAlgorithm(
            job_shop_data=job_shop_data,
            population_size=500,
            generations=200,
            crossover_rate=0.8
        )
        best_solution, best_fitness, fitness_history = genetic_algorithm.evolve(techniques=techniques, fitness=fitness)
        print("Best Solution:", best_solution)
        print("Best Fitness:", best_fitness)
        print("Fitness History", fitness_history)
        schedule = job_shop_plotter.generate_schedule(best_solution, job_shop_data.jobs)
        job_shop_validator.is_valid_schedule(schedule=schedule)
        job_shop_plotter.draw_schedule(schedule, job_shop_data.jobs)

