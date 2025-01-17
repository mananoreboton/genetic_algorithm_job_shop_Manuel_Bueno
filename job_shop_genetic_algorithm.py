import random
import numpy as np

from job_shop_techniques import Techniques

# Genetic Algorithm Implementation
class GeneticAlgorithm:
    def __init__(self, job_shop_data, population_size, generations, crossover_rate, mutation_rate):
        self.job_shop_data = job_shop_data
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate

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

    def evolve(self, techniques: Techniques):
        """Main genetic algorithm loop."""
        population = self.initialize_population()
        for generation in range(self.generations):
            fitness_of_all_individuals = [techniques.fitness(individual) for individual in population]
            next_population = []

            for _ in range(self.population_size // 2):
                parent1 = techniques.selection(population, fitness_of_all_individuals)
                parent2 = techniques.selection(population, fitness_of_all_individuals)

                if random.random() < self.crossover_rate:
                    child1 = techniques.crossover(parent1, parent2)
                    child2 = techniques.crossover(parent2, parent1)
                else:
                    child1, child2 = parent1[:], parent2[:]

                techniques.mutation(child1)
                techniques.mutation(child2)

                next_population.extend([child1, child2])

            population = next_population[:self.population_size]
            best_fitness = min(fitness_of_all_individuals)
            print(f"Generation {generation}: Best fitness = {best_fitness}")

        # Return the best solution
        fitness_of_all_individuals = [techniques.fitness(individual) for individual in population]
        best_index = np.argmin(fitness_of_all_individuals)
        return population[best_index], fitness_of_all_individuals[best_index]

