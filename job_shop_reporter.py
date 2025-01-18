# Tools (validator, plotter)
import os
import re

import job_shop_plotter
import job_shop_validator
from job_shop_data import JobShopData
from job_shop_techniques import Techniques


class JobShopReporter:
    def __init__(self, root_folder: str = "results/"):
        self.root_folder = root_folder
        self.case_results_file_name = self.root_folder+"case_results.csv"
        with open(self.case_results_file_name, "w") as file:
            file.write("case_file, selection, crossover, mutation, is_valid_schedule, population_size, generations, crossover_rate, best_fitness, execution_time\n")

    def add_case_result(self, best_solution, best_fitness, fitness_history, execution_time, job_shop_data: JobShopData, techniques: Techniques, parameters: []):
        case_folder_name = self.build_case_folder_name(job_shop_data.case_name, techniques.description(),
                                    f"p{parameters[0]}_g{parameters[1]}_cr{parameters[2]}")
        os.makedirs(case_folder_name, exist_ok=True)
        print(f"Writing case result to folder: {case_folder_name}")

        schedule = job_shop_plotter.generate_schedule(solution=best_solution, jobs=job_shop_data.jobs)
        with open(case_folder_name+"schedule.txt", "w") as file:
            file.write(str(schedule))

        is_valid_schedule = job_shop_validator.is_valid_schedule(schedule)
        with open(case_folder_name+f"is_valid_schedule_{is_valid_schedule}.txt", "w") as file:
            file.write(str(is_valid_schedule))

        job_shop_plotter.draw_schedule(schedule=schedule, folder=case_folder_name)

        with open(self.case_results_file_name, "a") as file:
            file.write(f"{job_shop_data.case_name}, {techniques.selection_name}, {techniques.crossover_name}, {techniques.mutation_name}, {is_valid_schedule}, {parameters[0]}, {parameters[1]}, {parameters[2]}, {best_fitness}, {execution_time}\n")

        with open(case_folder_name+"fitness_history.txt", "w") as file:
            file.write(str(fitness_history))

        job_shop_plotter.plot_fitness_history(fitness_history=fitness_history, folder=case_folder_name)

    def build_case_folder_name(self, job_shop_case_name: str, techniques_names: str, parameters_names: str) -> str:
        s = job_shop_case_name + "_" + techniques_names + "_" + parameters_names
        s = s.strip()
        s = re.sub(r'\s+', '_', s)
        s = re.sub(r'[^\w_]', '', s)
        s = self.root_folder + s + '/'
        return s