"""
Question:
Given an unsorted list of integers, find the indices of pairs that adds up to a given value.
The indices of the elements must be distinct.

"""

def two_sum(arr:list[int], target:int):
    # key - element : value - index
    dictionary_of_elements = {}

    # pairs_list = []
    for idx, num in enumerate(arr):
        if (target-num) in dictionary_of_elements:
            # pairs_list.append((dictionary_of_elements[target-num], idx))
            return (dictionary_of_elements[target-num], idx)
        else:
            dictionary_of_elements[num] = idx
    # return pairs_list
    return None

assert two_sum([1,2,3], 4) in [(0,2), (2,0)]
assert two_sum([1234,5678,9012], 14690) in [(1,2), (2,1)]
assert two_sum([2,2,3], 4) in [(0,1), (1,0)]
assert two_sum([2,2], 4) in [(0,1), (1,0)]
assert two_sum([8,7,2,5,3,1], 10) in [(0,2), (2,0), (1,4), (4,1)]
