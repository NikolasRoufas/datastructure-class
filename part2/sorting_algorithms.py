def bubble_sort(arr, key=None):
    """
    Implementation of Bubble Sort algorithm
    
    Args:
        arr: List to be sorted
        key: Function to extract comparison key (for struct sorting)
    
    Returns:
        Sorted list
    """
    n = len(arr)
    for i in range(n):
        # Flag to optimize if no swaps occur
        swapped = False
        for j in range(0, n - i - 1):
            # Compare based on key function if provided
            left = arr[j] if key is None else key(arr[j])
            right = arr[j + 1] if key is None else key(arr[j + 1])
            
            if left > right:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break
    
    return arr

def insertion_sort(arr, key=None):
    """
    Implementation of Insertion Sort algorithm
    
    Args:
        arr: List to be sorted
        key: Function to extract comparison key (for struct sorting)
    
    Returns:
        Sorted list
    """
    for i in range(1, len(arr)):
        # Element to be inserted at correct position
        current = arr[i]
        current_key = current if key is None else key(current)
        
        # Move elements that are greater than current
        # to one position ahead of their current position
        j = i - 1
        while j >= 0:
            # Get comparison key
            compare_key = arr[j] if key is None else key(arr[j])
            if compare_key <= current_key:
                break
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = current
    
    return arr

def selection_sort(arr, key=None):
    """
    Implementation of Selection Sort algorithm
    
    Args:
        arr: List to be sorted
        key: Function to extract comparison key (for struct sorting)
    
    Returns:
        Sorted list
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        min_val = arr[i] if key is None else key(arr[i])
        
        for j in range(i + 1, n):
            curr_val = arr[j] if key is None else key(arr[j])
            if curr_val < min_val:
                min_idx = j
                min_val = curr_val
                
        # Swap the found minimum element with the first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def merge_sort(arr, key=None):
    """
    Implementation of Merge Sort algorithm
    
    Args:
        arr: List to be sorted
        key: Function to extract comparison key (for struct sorting)
    
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Recursive division
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    
    # Merge sorted halves
    return merge(left, right, key)

def merge(left, right, key=None):
    """
    Helper function for merge sort to merge two sorted arrays
    
    Args:
        left: First sorted subarray
        right: Second sorted subarray
        key: Function to extract comparison key
    
    Returns:
        Merged sorted array
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        left_val = left[i] if key is None else key(left[i])
        right_val = right[j] if key is None else key(right[j])
        
        if left_val <= right_val:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr, key=None):
    """
    Implementation of Quick Sort algorithm (wrapper function)
    
    Args:
        arr: List to be sorted
        key: Function to extract comparison key (for struct sorting)
    
    Returns:
        Sorted list
    """
    # Create a copy to avoid modifying original array
    arr_copy = arr.copy()
    _quick_sort(arr_copy, 0, len(arr_copy) - 1, key)
    return arr_copy

def _quick_sort(arr, low, high, key=None):
    """
    Recursive implementation of Quick Sort
    
    Args:
        arr: List to be sorted
        low: Starting index
        high: Ending index
        key: Function to extract comparison key
    """
    if low < high:
        # Partition and get pivot index
        pivot_idx = partition(arr, low, high, key)
        
        # Sort elements before and after partition
        _quick_sort(arr, low, pivot_idx - 1, key)
        _quick_sort(arr, pivot_idx + 1, high, key)

def partition(arr, low, high, key=None):
    """
    Helper function for quicksort that partitions the array
    
    Args:
        arr: List to be partitioned
        low: Starting index
        high: Ending index
        key: Function to extract comparison key
    
    Returns:
        Index of the pivot element
    """
    # Use the rightmost element as pivot
    pivot = arr[high]
    pivot_key = pivot if key is None else key(pivot)
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # Get current element's key
        current_key = arr[j] if key is None else key(arr[j])
        
        # If current element is smaller than the pivot
        if current_key <= pivot_key:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def heap_sort(arr, key=None):
    """
    Implementation of Heap Sort algorithm
    
    Args:
        arr: List to be sorted
        key: Function to extract comparison key (for struct sorting)
    
    Returns:
        Sorted list
    """
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root with last element
        heapify(arr, i, 0, key)  # Heapify the reduced heap
    
    return arr

def heapify(arr, n, i, key=None):
    """
    Helper function to maintain heap property
    
    Args:
        arr: Array representing a heap
        n: Size of the heap
        i: Index of the root of the subtree
        key: Function to extract comparison key
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2
    
    # See if left child exists and is greater than root
    if left < n:
        left_key = arr[left] if key is None else key(arr[left])
        largest_key = arr[largest] if key is None else key(arr[largest])
        if left_key > largest_key:
            largest = left
    
    # See if right child exists and is greater than largest so far
    if right < n:
        right_key = arr[right] if key is None else key(arr[right])
        largest_key = arr[largest] if key is None else key(arr[largest])
        if right_key > largest_key:
            largest = right
    
    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the affected sub-tree
        heapify(arr, n, largest, key)