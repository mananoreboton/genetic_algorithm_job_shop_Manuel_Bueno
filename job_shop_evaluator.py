import genetic_algorithm_js as algo

techniques = [[]]

def evaluate_techniques(jobs):
    for combination in techniques:
        algo.genetic_algorithm(jobs, combination)