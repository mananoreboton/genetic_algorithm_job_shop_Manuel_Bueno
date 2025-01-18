# Crossover
from crossover import Crossover
from crossover_one_point import OnePointCrossover
from crossover_ox import OXCrossover
# Selection
from selection import Selection
from selection_tournament import TournamentSelection
from selection_probabilistic_tournament import ProbabilisticTournamentSelection
# Mutation
from mutation import Mutation
from mutation_swap import SwapMutation
from mutation_scramble import ScrambleMutation
# Fitness
from fitness_1 import MakespanCountUnsortedTasksFitness
# Genetic Algorithm
from job_shop_genetic_algorithm import GeneticAlgorithm
# Tools (validator, plotter)
import job_shop_plotter
import job_shop_validator
# Data types
from job_shop_data import JobShopData
from job_shop_techniques import Techniques

crossover_list = [OnePointCrossover(), OXCrossover()]
selection_list = [TournamentSelection(), ProbabilisticTournamentSelection()]
mutation_list = [SwapMutation(), ScrambleMutation()]


def build_techniques_combinations(crossovers: [Crossover], selections: [Selection], mutations: [Mutation]):
    combinations = []
    for crossover in crossovers:
        for selection in selections:
            for mutation in mutations:
                techniques = Techniques(selection=selection, crossover=crossover, mutation=mutation)
                combinations.append(techniques)
    return combinations


techniques_combinations = build_techniques_combinations(crossover_list, selection_list, mutation_list)

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

