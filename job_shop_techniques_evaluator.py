# Crossover
import sys

from crossover import Crossover
from crossover_ippx import IPPXCrossover
from crossover_one_point import OnePointCrossover
from crossover_ox import OXCrossover
# Fitness
from fitness_makespan_count_unsorted_tasks import MakespanCountUnsortedTasksFitness
# Data types
from job_shop_data import JobShopData
# Genetic Algorithm
from job_shop_genetic_algorithm import GeneticAlgorithm
from job_shop_reporter import JobShopReporter
from job_shop_techniques import Techniques
# Mutation
from mutation import Mutation
from mutation_scramble import ScrambleMutation
from mutation_swap import SwapMutation
# Selection
from selection import Selection
from selection_probabilistic_tournament import ProbabilisticTournamentSelection
from selection_tournament import TournamentSelection

crossover_list = [OnePointCrossover(), IPPXCrossover()]
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

population_size_list = [500]
generations_list = [200]
crossover_rate_list = [0.8]

def build_parameters_combinations():
    combinations = []
    for population_size in population_size_list:
        for generations in generations_list:
            for crossover_rate in crossover_rate_list:
                combinations.append((population_size, generations, crossover_rate))
    return combinations

parameters_combinations = build_parameters_combinations()

def evaluate_techniques(job_shop_data: JobShopData):
    job_shop_reporter = JobShopReporter(case_name=job_shop_data.case_name)
    for techniques in techniques_combinations:
        print(f">> Executing genetic algorithm with techniques: {techniques.description()}")
        for parameters in parameters_combinations:
            best = sys.maxsize
            for i in range(10):
                print(f">>> Executing genetic algorithm with population_size: {parameters[0]} generations: {parameters[1]} crossover_rate: {parameters[2]}")
                fitness = MakespanCountUnsortedTasksFitness(job_shop_data)
                genetic_algorithm = GeneticAlgorithm(
                    job_shop_data=job_shop_data,
                    population_size=parameters[0],
                    generations=parameters[1],
                    crossover_rate=parameters[2],
                )
                best_solution, best_fitness, fitness_history, execution_time = genetic_algorithm.evolve(techniques=techniques, fitness=fitness)
                print("Best Solution:", best_solution)
                print("Best Fitness:", best_fitness)
                print("Fitness History", fitness_history)
                print("Execution Time:", execution_time)
                should_be_added = False
                if best_fitness < best:
                    best = best_fitness
                    should_be_added = True
                job_shop_reporter.add_case_result(
                    best_solution=best_solution,
                    best_fitness=best_fitness,
                    fitness_history=fitness_history,
                    execution_time=execution_time,
                    job_shop_data=job_shop_data,
                    techniques=techniques,
                    parameters=parameters,
                    should_be_added=should_be_added
                )

