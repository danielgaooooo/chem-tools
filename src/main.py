#!/usr/bin/python3

# Returns true if i is within the lower/upper bounds
def _within_range(i, upper, lower):
    return lower <= i <= upper

# ============= https://www.geeksforgeeks.org/perfect-sum-problem/ ============
# Function to print the subsets whose sum is within upper and lower bounds
def _sumSubsets(sets, n, upper, lower, result) :
    # Create the new array with size equal to array set[] to create 
    # binary array as per n(decimal number) 
    x = [0]*len(sets)
    j = len(sets) - 1; 
  
    # Convert the array into binary array 
    while (n > 0) :
        x[j] = n % 2; 
        n = n // 2; 
        j -= 1; 
    sum = 0; 

    # Calculate the sum of this subset 
    for i in range(len(sets)) :
        if (x[i] == 1) :
            sum += sets[i]; 
  
    # Check whether sum is equal to target if it is equal, then print the subset 
    if (_within_range(sum, upper, lower)) :
        temp_list = []
        for i in range(len(sets)) :
            if (x[i] == 1) :
                temp_list.append(sets[i]); 
        result.add(tuple(temp_list))
  
# Function to find the subsets with sum within upper/lower bounds
def _findSubsets(arr, upper, lower) :
    # Calculate the total no. of subsets 
    x = pow(2, len(arr)); 
  
    # Run loop till total no. of subsets and call the function for each subset 
    result = set()
    for i in range(1, x) :
        _sumSubsets(arr, i, upper, lower, result); 
    return result
# ============= https://www.geeksforgeeks.org/perfect-sum-problem/ ============

# Duplicates each element in list l, n times
def _list_multiply(nums, multipliers):
    list_copy = []
    for i in range(len(nums)):
        for _ in range(int(multipliers[i])):
            list_copy.append(nums[i])
    return list_copy

def _filter_nonessential(subsets, essential):
    copy_subsets = []
    for subset in subsets:
        if essential in subset:
            copy_subsets.append(subset)
    return copy_subsets

def compare(sum, error, weights, occurrences):
    lower_bound = sum * (1 - float(error))
    upper_bound = sum * (1 + float(error))
    print(lower_bound)
    print(upper_bound)

    multiplied_weights = _list_multiply(weights, occurrences)

    subsets = _findSubsets(multiplied_weights, upper_bound, lower_bound)

    # the first weight MUST be used
    filtered_subsets = _filter_nonessential(subsets, weights[0])

    return filtered_subsets