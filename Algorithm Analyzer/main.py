#  For checking the input_generator.py file
'''
from src.input_generator import generate_all_inputs

inputs = generate_all_inputs(10)

for key, value in inputs.items():
    print(key, ":", value)
'''

# For checking the sorting.py
'''
from src.input_generator import generate_all_inputs
from src.sorting import bubble_sort, insertion_sort, merge_sort, quick_sort

inputs = generate_all_inputs(10)

for input_type, data in inputs.items():
    print(f"\n{input_type} Data:")

    print("Bubble:", bubble_sort(data))
    print("Insertion:", insertion_sort(data))
    print("Merge:", merge_sort(data))
    print("Quick:", quick_sort(data))
'''

from experiments import run_experiments, run_search_experiments

if __name__ == "__main__":
    run_experiments()
    run_search_experiments()