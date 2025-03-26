#!/usr/bin/python3

import argparse
import time
import datetime
import sys

def loading_bar(iteration, total, length=40, start_time=None):
    '''
    Displays a progress bar with percentage and estimated time remaining.
    
    :param iteration: Current iteration (progress)
    :param total: Total number of iterations
    :param length: Length of the progress bar
    :param start_time: Time when the process started (for ETA calculation)
    '''
    progress = int(length * iteration / total)
    bar = '#' * progress + '-' * (length - progress)
    percent = (iteration / total) * 100

    # Calculate ETA
    elapsed_time = time.time() - start_time if start_time else 0
    avg_time_per_iter = elapsed_time / iteration if iteration > 0 else 0
    eta = avg_time_per_iter * (total - iteration)

    # Format ETA in hours, minutes, and seconds
    eta_hours, remainder = divmod(int(eta), 3600)
    eta_minutes, eta_seconds = divmod(remainder, 60)
    eta_display = f'{eta_hours:02}h {eta_minutes:02}m {eta_seconds:02}s' if iteration > 0 else 'Calculating...'

    sys.stdout.write(f'\r[{bar}] {percent:.1f}% | {eta_display} remaining')
    sys.stdout.flush()

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
                temp_list.append(sets[i])
        result.add(tuple(temp_list))

def find_subsets(arr, upper, lower):
    '''
    Function to find the subsets with sum within upper/lower bounds
    '''
    # Calculate the total no. of subsets 
    x = pow(2, len(arr))

    # Run loop till total no. of subsets and call the function for each subset
    result = set()
    start_time = time.time()  # Track start time for ETA

    for i in range(1, x):
        sum_subsets(arr, i, upper, lower, result)
        if i % 5000 == 0 or i == x - 1:
            loading_bar(i, x, start_time=start_time)

    print('\n')  # Move to a new line after completion
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




def check_positive(value):
    '''Check if the value is a positive float.'''
    num = float(value)
    if num <= 0:
        raise argparse.ArgumentTypeError(f'{value} must be a positive number.')
    return num

def check_between_0_and_1(value):
    '''Check if the value is between 0 and 1.'''
    num = float(value)
    if not (0 <= num <= 1):
        raise argparse.ArgumentTypeError(f'{value} must be between 0 and 1.')
    return num

def check_positive_list(value):
    '''Check if all values in the space-separated list are positive floats.'''
    try:
        num_list = list(map(float, value.split()))
        if any(num <= 0 for num in num_list):
            raise ValueError
        return num_list
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f'{value} must be a space-separated '
                                         f'list of positive numbers.') from exc

def parse_file(file_path):
    '''Parse the input file to extract num1, num2, and num_list.'''
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read lines and remove leading/trailing whitespaces
        lines = [line.strip() for line in file.readlines()]

        # Expected to have three lines: num1, num2, num_list
        if len(lines) != 3:
            raise ValueError('Input file must contain exactly 3 lines.')

        num1 = check_positive(lines[0])  # First line: num1
        num2 = check_between_0_and_1(lines[1])  # Second line: num2
        num_list = check_positive_list(lines[2])  # Third line: num_list

        return num1, num2, num_list

def get_arguments():
    '''Parse input file argument'''
    # Set up argument parser for the file path
    parser = argparse.ArgumentParser(description='Parse inputs from a file.')
    parser.add_argument('file', type=str, help='Path to the input file')

    # Parse arguments
    args = parser.parse_args()

    # Parse the file
    return parse_file(args.file)

def main():
    '''
    execute perfect sum problem and print results
    '''
    total_sum, error, parts = get_arguments()

    lower_bound = total_sum * (1 - float(error))
    upper_bound = total_sum * (1 + float(error))

    start = time.perf_counter()
    sets = compare(total_sum, error, parts)
    end = time.perf_counter()

    output_file = f'results_{datetime.datetime.now()}.txt'

    # Open the file for writing
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f'Target sum was {total_sum} within {error * 100}% error '
                   f'({lower_bound} to {upper_bound})\n\n')
        # Iterate through the list of sets
        for s in sets:
            # Convert the set to a string and write it to the file
            file.write(str(s) + '\n')

    print(f'total runtime = {1000 * (end - start)}ms\n')
    print(f'OUTPUT WRITTEN TO: {output_file}\n\n')

if __name__ == '__main__':
    main()