"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

"""
First loop:
    array index: 0
    array element: 2

    diff = target - element
    diff = 9 - 2 
    diff = 7
    
    is 7 in tracker? No
    since 7 is not in tracker, add { 2: 0 } to it

Second loop:
    array index: 1
    array element: 7

    diff = target - element
    diff = 9 - 7
    diff = 2
    
    is 2 in tracker? Yes
    since 2 is in tracker, return the index of 2 and the index of the current number being iterated on i.e. 1

    Value of the diff (i.e. 2) in tracker: 0
    Index of current number: 1

If the array is [2, 7, 11, 15], and the target is 9,
it should return [0, 1]
"""


def two_sum(arr, target):
    tracker = {}

    for i, num in enumerate(arr):
        diff = target - num
        if diff not in tracker:
            tracker[num] = i
        else:
            return [tracker[diff], i]
