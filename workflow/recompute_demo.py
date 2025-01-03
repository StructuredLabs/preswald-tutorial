from preswald import Workflow, RetryPolicy
import random

workflow = Workflow()

@workflow.atom()
def load_data():
    print("Loading data...")
    return [1, 2, 3, 4, 5]

@workflow.atom(dependencies=['load_data'])
def process_data(load_data):
    print("Processing data...")
    return [x * 2 for x in load_data]

@workflow.atom(dependencies=['process_data'])
def analyze_data(process_data):
    print("Analyzing data...")
    total = sum(process_data)
    average = total / len(process_data)
    return {'total': total, 'average': average}

# First execution - all atoms will run
print("\nFirst execution:")
results = workflow.execute()

# Second execution - should use cached results
print("\nSecond execution (should use cache):")
results = workflow.execute()

# Third execution - force recomputation of process_data and its dependents
print("\nThird execution (recomputing process_data):")
results = workflow.execute(recompute_atoms={'process_data'})
