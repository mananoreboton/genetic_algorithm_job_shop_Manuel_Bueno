def is_valid_schedule(schedule):

    # Validation 1: Each machine can only handle one task at a time
    machine_usage = {}
    for job_id, op_id, machine, start_time, end_time in schedule:
        if machine not in machine_usage:
            machine_usage[machine] = []
        machine_usage[machine].append((start_time, end_time))

    for machine, intervals in machine_usage.items():
        # Sort tasks by start time
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                print(f"Conflict on machine {machine}: intervals {intervals[i]} and {intervals[i + 1]} overlap.")
                return False

    # Validation 2: Operations for each job must be executed in the correct order
    job_operations = {}
    for job_id, op_id, machine, start_time, end_time in schedule:
        if job_id not in job_operations:
            job_operations[job_id] = []
        job_operations[job_id].append((op_id, start_time, end_time))

    for job_id, ops in job_operations.items():
        # Sort operations by op_id
        ops.sort()
        for i in range(len(ops) - 1):
            if ops[i][2] > ops[i + 1][1]:  # end_time of one operation > start_time of the next
                print(f"Conflict in job {job_id}: operation {ops[i][0]} ends after operation {ops[i + 1][0]} starts.")
                return False

    # Validation 3: No operation can start before the previous operation in the same job ends
    for job_id, ops in job_operations.items():
        ops.sort()  # Sort operations by op_id
        for i in range(1, len(ops)):
            if ops[i][1] < ops[i - 1][2]:
                print(f"Conflict in job {job_id}: operation {ops[i][0]} starts before operation {ops[i - 1][0]} ends.")
                return False

    # Validation 4: All operations must have consistent times (start_time < end_time)
    for job_id, op_id, machine, start_time, end_time in schedule:
        if start_time >= end_time:
            print(f"Inconsistency in operation {op_id} of job {job_id}: start time {start_time} is not less than end time {end_time}.")
            return False

    # If all validations pass
    return True


def main():
    pass
    # ejemplo_schedule = [
    #     (1, 1, 'M1', 0, 3),
    #     (1, 2, 'M2', 4, 6),
    #     (2, 1, 'M1', 3, 5),
    #     (2, 2, 'M3', 6, 8)
    # ]
    #
    # print(is_valid_schedule(ejemplo_schedule))

if __name__ == "__main__":
    main()
