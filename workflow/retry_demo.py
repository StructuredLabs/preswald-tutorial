from preswald import Workflow, RetryPolicy
import random

workflow = Workflow(
    default_retry_policy=RetryPolicy(
        max_attempts=3,
        delay=1.0,
        backoff_factor=2.0,
        retry_exceptions=(IOError, TimeoutError)
    )
)

@workflow.atom()
def load_data():
    # Simulate potential failure
    if random.random() < 0.5:
        raise IOError("Failed to load data")
    return [1, 2, 3, 4, 5]

@workflow.atom(dependencies=['load_data'])
def process_data(load_data):
    return [x * 2 for x in load_data]

@workflow.atom(
    dependencies=['process_data'],
    retry_policy=RetryPolicy(max_attempts=5)  # Custom retry policy for this atom
)
def analyze_data(process_data):
    total = sum(process_data)
    average = total / len(process_data)
    return {'total': total, 'average': average}

# Execute the workflow and handle results
results = workflow.execute()

# Print execution summary
for atom_name, result in results.items():
    print(f"\nAtom: {atom_name}")
    print(f"Status: {result.status.value}")
    print(f"Attempts: {result.attempts}")
    if result.execution_time:
        print(f"Execution time: {result.execution_time:.2f}s")
    if result.error:
        print(f"Error: {str(result.error)}")
    elif result.value is not None:
        print(f"Result: {result.value}")
