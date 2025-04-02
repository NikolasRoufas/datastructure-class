import time
import random
import copy
import matplotlib.pyplot as plt
from sorting_algorithms import (
    bubble_sort, quick_sort, merge_sort, selection_sort, 
    insertion_sort, shell_sort, heap_sort
)

sorting_algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Shell Sort", shell_sort),
    ("Heap Sort", heap_sort)
]

def run_benchmark():
    scenarios = [100 * i for i in range(1, 11)]  
    num_runs = 5  
    
    
    with open("benchmark_results.txt", "w") as results_file:
        all_times = {name: [] for name, _ in sorting_algorithms}
        
        for size in scenarios:
            print(f"\nΕκτέλεση σεναρίου με {size} ακεραίους...")
            results_file.write(f"\n--- Σενάριο με {size} ακεραίους ---\n")
            
            original_array = [random.randint(0, 1000000) for _ in range(size)]
            
            for name, algorithm in sorting_algorithms:
                total_time = 0
                
                for run in range(num_runs):
                    arr = copy.deepcopy(original_array)
                    
                    start_time = time.time()
                    sorted_arr = algorithm(arr)
                    end_time = time.time()
                    
                    assert sorted(original_array) == sorted_arr, f"Ο αλγόριθμος {name} δεν ταξινόμησε σωστά τον πίνακα"
                    
                    total_time += end_time - start_time
                
                avg_time = total_time / num_runs
                
                all_times[name].append(avg_time)
                
                result = f"Αλγόριθμος {name} Πλήθος δεδομένων {size} Χρόνος εκτέλεσης {avg_time:.6f} sec"
                print(result)
                results_file.write(result + "\n")
        
        create_plots(scenarios, all_times)

def create_plots(scenarios, all_times):
    plt.figure(figsize=(14, 8))
    
    for name in all_times:
        plt.plot(scenarios, all_times[name], marker='o', label=name)
    
    plt.title('Σύγκριση Χρόνου Εκτέλεσης Αλγορίθμων Ταξινόμησης')
    plt.xlabel('Πλήθος Στοιχείων')
    plt.ylabel('Χρόνος Εκτέλεσης (sec)')
    plt.grid(True)
    plt.legend()
    plt.savefig('sorting_comparison_all.png')
    plt.close()
    
    plt.figure(figsize=(14, 8))
    for name in all_times:
        if name != "Bubble Sort":
            plt.plot(scenarios, all_times[name], marker='o', label=name)
    
    plt.title('Σύγκριση Χρόνου Εκτέλεσης Αλγορίθμων Ταξινόμησης (χωρίς Bubble Sort)')
    plt.xlabel('Πλήθος Στοιχείων')
    plt.ylabel('Χρόνος Εκτέλεσης (sec)')
    plt.grid(True)
    plt.legend()
    plt.savefig('sorting_comparison_no_bubble.png')
    
    for name in all_times:
        plt.figure(figsize=(10, 6))
        plt.plot(scenarios, all_times[name], marker='o', color='blue')
        plt.title(f'Χρόνος Εκτέλεσης για {name}')
        plt.xlabel('Πλήθος Στοιχείων')
        plt.ylabel('Χρόνος Εκτέλεσης (sec)')
        plt.grid(True)
        plt.savefig(f'sorting_{name.lower().replace(" ", "_")}.png')
        plt.close()

if __name__ == "__main__":
    run_benchmark()
