#### A2: Optimization with Genetic Algorithms
#### Neural and Evolutionary Computation (NEC)
#### Manuel R. Bueno G.

### Description
This project tackles the **Job Shop Scheduling Problem (JSSP)**, a combinatorial optimization problem involving the 
scheduling of jobs on machines to minimize the makespan while try to satisfy precedence and resource constraints. 
A genetic algorithm is implemented to provide effective solutions to this problem.


### Problems and Results
- Each test case generates results stored in a subfolder within the `results` directory.
- Test cases are located in the `test_cases` folder.

### Output Files for Each Execution
1. **fitness.png**: Fitness evolution plot across generations.
2. **fitness_history.txt**: Raw data of fitness evolution per generation.
3. **is_valid_schedule_True.txt**: Indicates a valid solution (generated only if the schedule is valid).
4. **schedule.png**: Gantt chart of the best schedule.
5. **schedule.txt**: Raw data of the best schedule.

### How to Execute
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python job_shop_files_evaluator.py`.

### Additional Options
- For more execution options, run the `job_shop_files_evaluator.py script` with the `--help` flag.

### Implementation Details
- **Genetic Algorithm Implementation**: `job_shop_genetic_algorithm.py`
- **Parameter and Technique Selection**: `job_shop_techniques_evaluator.py`
- **Fitness Evaluation**: `fitness_makespan_count_unsorted_tasks.py`
- **Solution Validation**: `job_shop_validator.py`
