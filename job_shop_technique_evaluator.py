import job_shop_genetic_algorithm

techniques = [
    []
]

def evaluate_techniques(jobs):
    for combination in techniques:
        job_shop_genetic_algorithm.genetic_algorithm(jobs=jobs, techniques=techniques)