import random

from crossover import Crossover


class IPPXCrossover(Crossover):

    def crossover(self, parent1, parent2):
        # Partition parents into segments
        partition_size = random.randint(1, len(parent1) // 2)
        partitions = [range(i, i + partition_size) for i in range(0, len(parent1), partition_size)]
        offspring = [None] * len(parent1)
        included_jobs = set()

        # Alternate partitions from parents
        for i, partition in enumerate(partitions):
            selected_parent = parent1 if i % 2 == 0 else parent2
            for index in partition:
                if index < len(selected_parent):
                    operation = selected_parent[index]
                    job_id = operation[0]
                    if job_id not in included_jobs:
                        offspring[index] = operation
                        included_jobs.add(job_id)

        # Fill remaining positions from parents
        for operation in parent1 + parent2:
            if None not in offspring:
                break
            if operation not in offspring:
                for i in range(len(offspring)):
                    if offspring[i] is None:
                        offspring[i] = operation
                        break

        return offspring