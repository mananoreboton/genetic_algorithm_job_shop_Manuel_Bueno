import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random



def generate_gantt_schedule(best_schedule, jobs):
    machine_indices = []

    for job in jobs:
        for operation in job:
            machine_indices.append(operation[0])
    max_machine_index = max(machine_indices)
    machine_times = [0] * (max_machine_index + 1)

    job_end_times = [0] * len(jobs)
    gantt_schedule = []

    for job_id, op_id in best_schedule:
        machine, duration = jobs[job_id][op_id]
        start_time = max(machine_times[machine], job_end_times[job_id])
        end_time = start_time + duration

        machine_times[machine] = end_time
        job_end_times[job_id] = end_time
        s = (job_id, op_id, machine, start_time, end_time)
        gantt_schedule.append(s)

    return gantt_schedule

def draw_schedule(schedule, jobs):
    num_machines = max(task[2] for task in schedule) + 1
    num_jobs = len(jobs)

    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(num_jobs)]

    fig, ax = plt.subplots(figsize=(10, 5))

    for task in schedule:
        job_id, op_id, machine, start, end = task
        color = colors[job_id]

        ax.broken_barh([(start, end - start)], (machine - 0.4, 0.8), facecolors=color, edgecolor="black")

        ax.text(
            start + (end - start) / 2, machine,
            f"J{job_id}O{op_id}",
            ha="center", va="center", color="white", fontsize=8
        )

    ax.set_xlabel("Time")
    ax.set_ylabel("Machine")
    ax.set_yticks(range(num_machines))
    ax.set_yticklabels([f"M{i}" for i in range(num_machines)])
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)

    legend_handles = [mpatches.Patch(color=colors[job_id], label=f"Job {job_id}") for job_id in range(num_jobs)]
    ax.legend(handles=legend_handles, loc="upper left", bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.title("Gantt of Schedule Job Shop")
    plt.show()


def main():
    # jobs = [
    #     [(3, 7), (1, 5), (2, 6), (4, 4), (5, 3)],
    #     [(2, 8), (3, 6), (5, 5), (1, 7), (4, 4)],
    #     [(1, 9), (5, 7), (4, 8), (3, 6), (2, 5)],
    #     [(4, 10), (3, 8), (2, 7), (1, 5), (5, 6)],
    #     [(5, 7), (3, 6), (1, 5), (2, 8), (4, 9)]
    # ]
    #
    # best_schedule = [(3, 3), (4, 0), (5, 4), (2, 2), (3, 1), (5, 4), (3, 0), (1, 2), (1, 1), (5, 2), (5, 0), (4, 4), (2, 3), (1, 1), (2, 3), (5, 0), (2, 2), (2, 4), (1, 1), (3, 3), (4, 3), (2, 2), (3, 1), (1, 3), (4, 4)]
    tjobs = [
        [(0, 3), (1, 2), (2, 2)],
        [(0, 2), (2, 1), (1, 4)],
        [(1, 4), (2, 3)]
    ]

    tbest_schedule = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 1)]
    gantt_schedule = generate_gantt_schedule(tbest_schedule, tjobs)
    draw_schedule(gantt_schedule, tjobs)

if __name__ == "__main__":
    main()
