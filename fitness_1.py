from fitness import Fitness
from job_shop_data import JobShopData


class Fitness1(Fitness):
    def __init__(self, job_shop_data: JobShopData):
        self.job_shop_data = job_shop_data

    def fitness(self, schedule):
        """
        Evaluates a schedule to calculate the makespan.
        """
        # print("Using Fitness 1")
        result = {}
        machine_time = [0] * self.job_shop_data.num_machines
        job_time = [0] * self.job_shop_data.num_jobs

        for job_id, operation_index in schedule:
            if job_id not in result:
                result[job_id] = []  # Initialize a list for the key if it doesn't exist
            result[job_id].append(operation_index)

            machine, time = self.job_shop_data.jobs[job_id][operation_index]
            start_time = max(machine_time[machine], job_time[job_id])
            machine_time[machine] = start_time + time
            job_time[job_id] = start_time + time
        return self.count_unsorted_values(result) * max(machine_time)

        # return max(machine_time)

    def count_unsorted_values(self, data):
        unsorted_counts = {}
        for key, value_list in data.items():
            count = sum(1 for i in range(1, len(value_list)) if value_list[i] < value_list[i - 1])
            unsorted_counts[key] = count
        return sum(unsorted_counts.values()) * 2