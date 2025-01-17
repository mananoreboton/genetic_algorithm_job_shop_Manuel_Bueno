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
        machine_time = [0] * self.job_shop_data.num_machines
        job_time = [0] * self.job_shop_data.num_jobs

        for job_id, operation_index in schedule:
            machine, time = self.job_shop_data.jobs[job_id][operation_index]
            start_time = max(machine_time[machine], job_time[job_id])
            machine_time[machine] = start_time + time
            job_time[job_id] = start_time + time

        return max(machine_time)