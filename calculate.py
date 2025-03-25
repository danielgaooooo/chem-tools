#!/usr/bin/python3
import concurrent.futures


def within_range(i, upper, lower):
    '''
    Returns true if i is within the lower/upper bounds
    '''
    return lower <= i <= upper

# ============= https://www.geeksforgeeks.org/perfect-sum-problem/ ============
def sum_subsets(sets, n, upper, lower, result) :
    '''
    Function to print the subsets whose sum is within upper and lower bounds
    '''
    # Create the new array with size equal to array set[] to create
    # binary array as per n(decimal number)
    x = [0]*len(sets)
    j = len(sets) - 1
  
    # Convert the array into binary array
    while (n > 0) :
        x[j] = n % 2
        n = n // 2
        j -= 1
    sum_total = 0

    # Calculate the sum of this subset
    for i in range(len(sets)):
        if (x[i] == 1):
            sum_total += sets[i]

    # Check whether sum is equal to target if it is equal, then print the subset
    if within_range(sum_total, upper, lower):
        temp_list = []
        for i in range(len(sets)):
            if (x[i] == 1) :
                temp_list.append(sets[i]); 
        result.add(tuple(temp_list))

def process_subset(i, arr, upper, lower, result):
    # This function will encapsulate the call to sum_subsets for each subset index i
    sum_subsets(arr, i, upper, lower, result)

def find_subsets(arr, upper, lower):
    '''
    Function to find the subsets with sum within upper/lower bounds using multithreading
    '''
    # Calculate the total no. of subsets
    x = pow(2, len(arr))
    
    # Initialize a set to store the results
    result = set()
    
    # Create a ThreadPoolExecutor to run the tasks concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Submit tasks to the thread pool for each subset
        futures = [
            executor.submit(process_subset, i, arr, upper, lower, result)
            for i in range(1, x)
        ]
        
        # Wait for all tasks to complete
        concurrent.futures.wait(futures)
    
    return result

def _filter_nonessential(subsets, essential):
    copy_subsets = []
    for subset in subsets:
        if essential in subset:
            copy_subsets.append(subset)
    return copy_subsets

def compare(sum_total, error, weights):
    '''
    finds all possible combinations of weights that sum to sum_total within err
    '''
    lower_bound = sum_total * (1 - float(error))
    upper_bound = sum_total * (1 + float(error))

    subsets = find_subsets(weights, upper_bound, lower_bound)

    # the first weight MUST be used
    filtered_subsets = _filter_nonessential(subsets, weights[0])

    return filtered_subsets
