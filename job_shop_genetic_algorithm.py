import random
import time
import numpy as np

from fitness import Fitness
from job_shop_techniques import Techniques

# Genetic Algorithm Implementation
class GeneticAlgorithm:
    def __init__(self, job_shop_data, population_size, generations, crossover_rate):
        self.job_shop_data = job_shop_data
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate

    def initialize_population(self):
        """Randomly initializes the population."""
        population = []
        for _ in range(self.population_size):
            schedule = []
            for job_id in range(self.job_shop_data.num_jobs):
                for operation_index in range(len(self.job_shop_data.jobs[job_id])):
                    schedule.append((job_id, operation_index))
            random.shuffle(schedule)
            population.append(schedule)
        return population

    def evolve(self, techniques: Techniques, fitness: Fitness):
        """Main genetic algorithm loop."""
        start_time = time.time()
        population = self.initialize_population()
        fitness_history = []
        for generation in range(self.generations):
            fitness_of_all_individuals = [fitness.fitness(individual) for individual in population]
            next_population = []

            for _ in range(self.population_size // 2):
                parent1 = techniques.selection.selection(population, fitness_of_all_individuals)
                parent2 = techniques.selection.selection(population, fitness_of_all_individuals)

                if random.random() < self.crossover_rate:
                    child1 = techniques.crossover.crossover(parent1, parent2)
                    child2 = techniques.crossover.crossover(parent2, parent1)
                else:
                    child1, child2 = parent1[:], parent2[:]

                techniques.mutation.mutation(child1)
                techniques.mutation.mutation(child2)

                next_population.extend([child1, child2])

            population = next_population[:self.population_size]
            best_fitness = min(fitness_of_all_individuals)
            fitness_history.append(best_fitness)
            #print(f"Generation {generation}: Best fitness = {best_fitness}")

        # Return the best solution
        fitness_of_all_individuals = [fitness.fitness(individual) for individual in population]
        best_index = np.argmin(fitness_of_all_individuals)
        end_time = time.time()
        execution_time = end_time - start_time
        return population[best_index], fitness_of_all_individuals[best_index], fitness_history, execution_time

