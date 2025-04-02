import random
import string
import time
import os
import json
import matplotlib.pyplot as plt
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort

# Define the Record class for Part B
class Record:
    def __init__(self, id_num, string1, string2, string3):
        self.id_num = id_num
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3
    
    def __str__(self):
        return f"ID: {self.id_num}, String1: {self.string1}, String2: {self.string2}, String3: {self.string3}"
    
    def to_dict(self):
        return {
            "id_num": self.id_num,
            "string1": self.string1,
            "string2": self.string2,
            "string3": self.string3
        }

def generate_random_string(length=10):
    """Generate a random string of specified length"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_records(num_records=1000):
    """Generate random records for testing"""
    records = []
    for i in range(num_records):
        record = Record(
            id_num=random.randint(1, 10000),
            string1=generate_random_string(8),
            string2=generate_random_string(12),
            string3=generate_random_string(10)
        )
        records.append(record)
    return records

def save_records_to_file(records, filename="records.json"):
    """Save records to a JSON file"""
    with open(filename, 'w') as f:
        json.dump([record.to_dict() for record in records], f, indent=2)
    print(f"Saved {len(records)} records to {filename}")

def load_records_from_file(filename="records.json", limit=None):
    """Load records from a JSON file"""
    with open(filename, 'r') as f:
        data = json.load(f)
        if limit:
            data = data[:limit]
        records = [Record(**item) for item in data]
    print(f"Loaded {len(records)} records from {filename}")
    return records

def measure_sort_time(sort_func, arr, key=None, num_runs=5):
    """Measure the execution time of a sorting algorithm"""
    total_time = 0
    
    for _ in range(num_runs):
        # Create a copy to avoid sorting the same array multiple times
        arr_copy = arr.copy()
        
        # Measure time
        start_time = time.time()
        sort_func(arr_copy, key)
        end_time = time.time()
        
        total_time += (end_time - start_time)
    
    # Return average time
    return total_time / num_runs

def run_part_a_experiments():
    """Run experiments for Part A (integer arrays)"""
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort
    }
    
    results = {algo: [] for algo in algorithms}
    
    # Create output file
    with open("part_a_results.txt", "w") as f:
        f.write("Results for Part A (Integer Arrays)\n")
        f.write("="*50 + "\n")
    
    for size in sizes:
        # Generate random array of integers
        arr = [random.randint(1, 10000) for _ in range(size)]
        
        print(f"\nTesting with array size {size}:")
        
        for algo_name, sort_func in algorithms.items():
            # Measure execution time
            exec_time = measure_sort_time(sort_func, arr)
            results[algo_name].append(exec_time)
            
            # Print and append to results file
            print(f"Algorithm {algo_name} Array Size {size} Execution Time {exec_time:.6f} sec")
            
            with open("part_a_results.txt", "a") as f:
                f.write(f"Algorithm {algo_name} Array Size {size} Execution Time {exec_time:.6f} sec\n")
    
    # Create visualization
    plt.figure(figsize=(12, 8))
    for algo_name, times in results.items():
        plt.plot(sizes, times, marker='o', label=algo_name)
    
    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithms Performance - Integer Arrays')
    plt.legend()
    plt.grid(True)
    plt.savefig('part_a_performance.png')
    
    return results

def run_part_b_experiments():
    """Run experiments for Part B (record arrays)"""
    # First, generate and save 1000 records if not already done
    if not os.path.exists("records.json"):
        records = generate_records(1000)
        save_records_to_file(records)
    
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort
    }
    
    results = {algo: [] for algo in algorithms}
    
    # Create output file
    with open("part_b_results.txt", "w") as f:
        f.write("Results for Part B (Record Arrays)\n")
        f.write("="*50 + "\n")
    
    for size in sizes:
        # Load records
        records = load_records_from_file(limit=size)
        
        print(f"\nTesting with record array size {size}:")
        
        for algo_name, sort_func in algorithms.items():
            # Define key function for string1 field
            key_func = lambda r: r.string1
            
            # Measure execution time
            exec_time = measure_sort_time(sort_func, records, key_func)
            results[algo_name].append(exec_time)
            
            # Print and append to results file
            print(f"Algorithm {algo_name} Record Array Size {size} Execution Time {exec_time:.6f} sec")
            
            with open("part_b_results.txt", "a") as f:
                f.write(f"Algorithm {algo_name} Record Array Size {size} Execution Time {exec_time:.6f} sec\n")
    
    # Create visualization
    plt.figure(figsize=(12, 8))
    for algo_name, times in results.items():
        plt.plot(sizes, times, marker='o', label=algo_name)
    
    plt.xlabel('Record Array Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithms Performance - Record Arrays (by string1)')
    plt.legend()
    plt.grid(True)
    plt.savefig('part_b_performance.png')
    
    return results

def compare_results(part_a_results, part_b_results):
    """Create comparison charts between part A and part B results"""
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    
    # Create separate plots for each algorithm to compare performance
    for algo_name in part_a_results.keys():
        plt.figure(figsize=(10, 6))
        
        plt.plot(sizes, part_a_results[algo_name], marker='o', label='Integers')
        plt.plot(sizes, part_b_results[algo_name], marker='s', label='Records')
        
        plt.xlabel('Array Size')
        plt.ylabel('Execution Time (seconds)')
        plt.title(f'{algo_name} Performance: Integers vs Records')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'{algo_name.replace(" ", "_")}_comparison.png')

def main():
    # Check if records file exists, if not generate and save
    if not os.path.exists("records.json"):
        print("Generating 1000 random records...")
        records = generate_records(1000)
        save_records_to_file(records)
    
    # Run Part A experiments
    print("\n--- Running Part A: Integer Arrays ---")
    part_a_results = run_part_a_experiments()
    
    # Run Part B experiments
    print("\n--- Running Part B: Record Arrays ---")
    part_b_results = run_part_b_experiments()
    
    # Create comparison charts
    print("\n--- Creating Comparison Charts ---")
    compare_results(part_a_results, part_b_results)
    
    print("\nExperiments completed. Check result files and charts.")

if __name__ == "__main__":
    main()
