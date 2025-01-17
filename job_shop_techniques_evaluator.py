import crossover_1
import job_shop_plotter
import selection_1
import v4
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
        genetic_algorithm = GeneticAlgorithm(
            job_shop_data=job_shop_data,
            population_size=50,
            generations=100,
            crossover_rate=0.8
        )


        scheduler = v4.JobShopScheduler(job_shop_data.jobs, num_machines=job_shop_data.num_machines, population_size=20, generations=100, mutation_rate=0.1)
        best_schedule, fitness_history = scheduler.run()
        print("Best Schedule:", best_schedule)
        print("Best Solution:", scheduler.calculate_fitness(best_schedule))
        print("Fitness History:", fitness_history)
        is_valid_schedule = job_shop_validator.is_valid_schedule(schedule=best_schedule)
        print("Valid schedule:", is_valid_schedule)
        job_shop_plotter.draw_schedule(best_schedule, job_shop_data.jobs)
