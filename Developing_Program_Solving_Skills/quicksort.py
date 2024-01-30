"""
Quicksort Algorithm - based on 'divide and conquer'

- Given an array of elements (for example, integers):
    - If array contains zero or 1 elements, return.
    - Otherwize: 
        - pick one element to use as pivot (we will use the 'middle': length of list // 2)
        - partition elements into three sub-arrays: 
            - elements less than the pivot
            - elements with the same value as the pivot
            - elements greater than the pivot
        - Quicksort the sub-arrays and join the sorted results to get the solution

"""

def quicksort(arr:list[int], left:int, right:int):
    # check if the array has more than 1 element:
    if left < right:
        partition_idx = partition(arr, left, right)
        
        # recursive call on the left side
        quicksort(arr, left, partition_idx - 1)
        
        # recursive call on the right side
        quicksort(arr, partition_idx + 1, right)


def partition(arr:list[int], left:int, right:int):
    # we choose the last element to be the pivot element
    pivot = arr[right]
    
    i = left
    j = right - 1
    
    # when i passes j we know that we sorted all the elements
    while i < j:
        # move towards the end of the array until you find an element that is larger than the pivot and needs to move to the right sub-array
        while arr[i] < pivot and i < right:
            i += 1

        # move towards the begining of the array until you find an element that is smaller than the pivot and needs to move to the left sub-array
        while arr[j] >= pivot and j > left:
            j -= 1
        # if the two indexes didn't cross - it means that we found elements to swap, to arrange the elements in the respective sub-arrays:
        if i < j:
            # swap
            arr[i], arr[j] = arr[j], arr[i]
    
    # after the indexes i and j crossed:
    # if the pivot is smaller than the element in the index i (the conjuction of the subarrays we arranged) - swap the elements. 
    if arr[i] > pivot:
        # swap
        arr[i], arr[right] = arr[right], arr[i]
    
    # return the index of the conjuction of the two sub-arrays (to the left- smaller elements, to the right - larger elements) - 
    # this index tells us where to split the array
    return i


my_list = [2,1,8,6,5,7,3,4]
print(my_list)
quicksort(arr=my_list, left=0, right=len(my_list)-1)
print(my_list)