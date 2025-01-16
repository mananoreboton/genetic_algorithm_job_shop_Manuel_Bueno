class JobShopDataset:
    def __init__(self, text: str):
        """
        Load test case with the format defined in:
        https://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/jobshop1.txt

        Each instance consists of a line of description, a line containing the
        number of jobs and the number of machines, and then one line for each job,
        listing the machine number and processing time for each step of the job.
        The machines are numbered starting with 0.
        """
        self.jobs = []
        lines = text.strip().split("\n")
        num_jobs, num_machines = map(int, lines[0].split())
        for i in range(num_jobs):
            job_data = list(map(int, lines[i + 1].split()))
            job = [(job_data[j], job_data[j + 1]) for j in range(0, len(job_data), 2)]
            self.jobs.append(job)

    def get_jobs(self):
        return self.jobs

    def show_jobs(self):
        for i, job in enumerate(self.jobs):
            print(f"Job {i}: {job}")


if __name__ == "__main__":
    text = """ 6 6
    2  1  0  3  1  6  3  7  5  3  4  6
    1  8  2  5  4 10  5 10  0 10  3  4
    2  5  3  4  5  8  0  9  1  1  4  7
    1  5  0  5  2  5  3  3  4  8  5  9 
    2  9  1  3  4  5  5  4  0  3  3  1
    1  3  3  3  5  9  0 10  4  4  2  1
    """
    jobShopDataset = JobShopDataset(text=text)
    print(jobShopDataset.get_jobs())
    jobShopDataset.show_jobs()


