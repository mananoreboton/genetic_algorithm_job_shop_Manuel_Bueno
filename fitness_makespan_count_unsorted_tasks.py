from fitness import Fitness
from job_shop_data import JobShopData


class MakespanCountUnsortedTasksFitness(Fitness):
    def __init__(self, job_shop_data: JobShopData):
        self.job_shop_data = job_shop_data

    def fitness(self, schedule):
        # print("Using Fitness 1")
        task_order = {}
        machine_time = [0] * self.job_shop_data.num_machines
        job_time = [0] * self.job_shop_data.num_jobs

        for job_id, operation_index in schedule:
            if job_id not in task_order:
                task_order[job_id] = []
            task_order[job_id].append(operation_index)

            machine, time = self.job_shop_data.jobs[job_id][operation_index]
            start_time = max(machine_time[machine], job_time[job_id])
            machine_time[machine] = start_time + time
            job_time[job_id] = start_time + time
        return self.count_unsorted_tasks(task_order) * max(machine_time)

        # return max(machine_time)

    def count_unsorted_tasks(self, data):
        unsorted_counts = {}
        for key, value_list in data.items():
            count = sum(1 for i in range(1, len(value_list)) if value_list[i] < value_list[i - 1])
            unsorted_counts[key] = count
        return (sum(unsorted_counts.values()) + 1) * 2