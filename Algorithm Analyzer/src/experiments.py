import time
import pandas as pd

from src.input_generator import generate_all_inputs
from src.sorting import bubble_sort, insertion_sort, merge_sort, quick_sort
from src.searching import linear_search, binary_search
import random

def run_experiments():
    
    results = []
    
    # Taking three sample sizes (100, 500, 1000)
    input_size = [100, 500, 1000]
    
    # Runing this mulitple times
    runs = 5
    
    for size in input_size:
        
        print("Running for size:", size)
        
        for run in range(runs):
            # TODO: Create function for this repetitive task
            
            inputs = generate_all_inputs(size)
            
            for input_type in inputs:
                
                data = inputs[input_type]
                
                # For Bubble Sort:
                start = time.perf_counter()
                bubble_sort(data)
                end = time.perf_counter()
                
                results.append({
                    "Algorithm": "Bubble",
                    "Input_Size": size,
                    "Input_Type": input_type,
                    "Time_Taken": end - start,
                    "Run": run + 1
                })
                
                # For Insertion Sort:
                start = time.perf_counter()
                insertion_sort(data)
                end = time.perf_counter()
                
                results.append({
                    "Algorithm": "Insertion",
                    "Input_Size": size,
                    "Input_Type": input_type,
                    "Time_Taken": end - start,
                    "Run": run + 1
                })
                
                # For Merge Sort:
                start = time.perf_counter()
                merge_sort(data)
                end = time.perf_counter()
                
                results.append({
                    "Algorithm": "Merge",
                    "Input_Size": size,
                    "Input_Type": input_type,
                    "Time_Taken": end - start,
                    "Run": run + 1
                })
                
                # For Quick Sort:
                start = time.perf_counter()
                quick_sort(data)
                end = time.perf_counter()
                
                results.append({
                    "Algorithm": "Quick",
                    "Input_Size": size,
                    "Input_Type": input_type,
                    "Time_Taken": end - start,
                    "Run": run + 1
                })
                
                # Convert to DataFrame
                df = pd.DataFrame(results)
                
                # Saving to csv
                df.to_csv("data/results.csv", index = False)
                
                print("Done! Rsults saved.")


def run_search_experiments():
    results = []

    input_sizes = [100, 500, 1000]
    runs = 5

    for size in input_sizes:
        print("Searching - size:", size)

        for run in range(runs):

            arr = generate_all_inputs(size)["Random"]

            # pick random target
            target = random.choice(arr.tolist())

            # Linear Search
            start = time.perf_counter()
            linear_search(arr, target)
            end = time.perf_counter()

            results.append({
                "Method": "Linear Search",
                "Input_Size": size,
                "Time_Taken": end - start,
                "Run": run + 1
            })

            # Binary Search (needs sorted)
            sorted_arr = sorted(arr)

            start = time.perf_counter()
            binary_search(sorted_arr, target)
            end = time.perf_counter()

            results.append({
                "Method": "Binary Search",
                "Input_Size": size,
                "Time_Taken": end - start,
                "Run": run + 1
            })

    df = pd.DataFrame(results)
    df.to_csv("data/search_results.csv", index=False)

    print("Search experiments done.")