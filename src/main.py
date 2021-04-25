#!/usr/bin/python3

import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename', help='file with ints to process')
parser.add_argument('error', help='margin of error, in percentage')
args = parser.parse_args()

# Returns true if i is within the lower/upper bounds
def within_range(i, upper, lower):
    return lower <= i <= upper

# ============= https://www.geeksforgeeks.org/perfect-sum-problem/ ============
# Function to print the subsets whose sum is within upper and lower bounds
def sumSubsets(sets, n, upper, lower, result) :
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
    if (within_range(sum, upper, lower)) :
        temp_list = []
        for i in range(len(sets)) :
            if (x[i] == 1) :
                temp_list.append(sets[i]); 
        result.add(tuple(temp_list))
  
# Function to find the subsets with sum within upper/lower bounds
def findSubsets(arr, upper, lower) :
    # Calculate the total no. of subsets 
    x = pow(2, len(arr)); 
  
    # Run loop till total no. of subsets and call the function for each subset 
    result = set()
    for i in range(1, x) :
        sumSubsets(arr, i, upper, lower, result); 
    return result
# ============= https://www.geeksforgeeks.org/perfect-sum-problem/ ============

# Returns true if the string s is a number
# https://stackoverflow.com/q/354038
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Duplicates each element in list l, n times
def list_multiply(nums, multipliers):
    list_copy = []
    for i in range(len(nums)):
        for _ in range(int(multipliers[i])):
            list_copy.append(nums[i])
    return list_copy


def read_weights():
    weights = open(args.filename, 'r')
    # Reading from the file
    content = weights.readlines()
    list_weights = []
    # Iterating through the content of the file
    for line in content:
        if is_number(line):
            list_weights.append(float(line))
    return list_weights

def filter_nonessential(subsets, essential):
    copy_subsets = []
    for subset in subsets:
        if essential in subset:
            copy_subsets.append(subset)
    return copy_subsets

def tup_to_dict(tup):
    result = {}
    for num in tup:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result

def compare():
    raw_values = read_weights()
    lower_bound = raw_values[0] * (1 - float(args.error))
    upper_bound = raw_values[0] * (1 + float(args.error))
    len_weights = (len(raw_values) - 1) / 2
    weights = raw_values[1: int(1+len_weights)]
    multipliers = raw_values[int(1+len_weights):]
    print(weights)
    print(multipliers)
    print(lower_bound)
    print(upper_bound)

    multiplied_weights = list_multiply(weights, multipliers)

    subsets = findSubsets(multiplied_weights, upper_bound, lower_bound)

    # the first weight MUST be used
    filtered_subsets = filter_nonessential(subsets, weights[0])

    f = open('out/' + args.filename, 'a')
    for item in filtered_subsets:
        item_to_dict = tup_to_dict(item)
        f.write(str(sum(list(item))) + '\n')
        f.write(str(item_to_dict) + '\n\n')

if __name__ == '__main__':
    compare()
