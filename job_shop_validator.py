def is_valid_schedule(best_schedule, jobs):

    n_machines = max(op[0] for job in jobs for op in job) + 1
    n_jobs = len(jobs)

    machine_end_times = [0] * n_machines
    job_end_times = [0] * n_jobs

    job_operation_count = [0] * n_jobs

    for job_id, task_id in best_schedule:
        if task_id >= len(jobs[job_id]):
            print(f"Error: Task {task_id} not found in Job {job_id}.")
            return False

        machine, time = jobs[job_id][task_id]

        if task_id != job_operation_count[job_id]:
            print(f"Error: Task {task_id} of Job {job_id} is out of order.")
            return False

        start_time = max(machine_end_times[machine], job_end_times[job_id])
        end_time = start_time + time

        if start_time < machine_end_times[machine]:
            print(f"Error: Machine {machine} is not available for Task {task_id} of Job {job_id}.")
            return False

        machine_end_times[machine] = end_time
        job_end_times[job_id] = end_time
        job_operation_count[job_id] += 1

    print("Job shop schedule is valid!")
    return True

tjobs = [
    [(0, 3), (1, 2), (2, 2)],
    [(0, 2), (2, 1), (1, 4)],
    [(1, 4), (2, 3)]
]

tbest_schedule = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 1)]
is_valid_schedule(tbest_schedule, tjobs)
