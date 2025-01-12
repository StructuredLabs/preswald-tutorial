from preswald import Workflow, WorkflowAnalyzer
import random

# Create a sample workflow
workflow = Workflow()


@workflow.atom()
def load_data():
    return [1, 2, 3, 4, 5]


@workflow.atom(dependencies=['load_data'])
def process_data(load_data):
    return [x * 2 for x in load_data]


@workflow.atom(dependencies=['process_data'])
def analyze_data(process_data):
    return {'total': sum(process_data), 'average': sum(process_data)/len(process_data)}


@workflow.atom(dependencies=['process_data'])
def visualize_data(process_data):
    return f"Data visualization for {process_data}"


# Create analyzer
analyzer = WorkflowAnalyzer(workflow)

# Execute workflow
workflow.execute()

# Create and display visualization
fig = analyzer.visualize()
# fig.show()  # Opens in web browser

# Show critical path
critical_path = analyzer.get_critical_path()
print("Critical path:", ' -> '.join(critical_path))
fig_critical = analyzer.visualize(
    highlight_path=critical_path,
    title="Workflow Critical Path"
)
fig_critical.show()

# Show parallel execution groups
parallel_groups = analyzer.get_parallel_groups()
print("\nParallel execution groups:")
for i, group in enumerate(parallel_groups, 1):
    print(f"Group {i}: {', '.join(group)}")
