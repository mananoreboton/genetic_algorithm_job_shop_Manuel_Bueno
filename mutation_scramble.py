import random

from mutation import Mutation


class ScrambleMutation(Mutation):

    def mutation(self, schedule):
        i, j = sorted(random.sample(range(len(schedule)), 2))
        segment = schedule[i:j+1]

        # Group operations by job within the segment
        job_groups = {}
        for operation in segment:
            job_id, op_index = operation
            if job_id not in job_groups:
                job_groups[job_id] = []
            job_groups[job_id].append(operation)

        # Create a list of job IDs to shuffle
        job_ids = list(job_groups.keys())
        random.shuffle(job_ids)

        # Rebuild the segment in the shuffled job order
        shuffled_segment = []
        for job_id in job_ids:
            shuffled_segment.extend(job_groups[job_id])

        schedule[i:j+1] = shuffled_segment
        return schedule