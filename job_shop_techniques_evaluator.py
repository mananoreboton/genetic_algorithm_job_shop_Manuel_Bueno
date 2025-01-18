from crossover_one_point import OnePointCrossover
from crossover_ox import OXCrossover

from selection_tournament import TournamentSelection
from selection_elitism import SelectionElitism

from mutation_swap import SwapMutation

from fitness_1 import MakespanCountUnsortedTasksFitness


import job_shop_plotter
from job_shop_genetic_algorithm import GeneticAlgorithm
from job_shop_data import JobShopData
from job_shop_techniques import Techniques

import job_shop_validator

techniques_combinations = [
    Techniques(
        selection=TournamentSelection(),
        mutation=SwapMutation(),
        crossover=OnePointCrossover()
    )
]

def evaluate_techniques(job_shop_data: JobShopData):
    for techniques in techniques_combinations:
        print(f"Executing genetic algorithm with techniques: {techniques.description()}")
        fitness = MakespanCountUnsortedTasksFitness(job_shop_data)
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

