"""
Question: 
Selection sort algorithm - finds the smallest element in the list and exchange it with the element in the first 
position of the list. 
repeat until the end of the list.
"""


def find_min_idx(arr:list):
    # this function gets an array of integers and returns the index of the minimum value in it.
    min_idx = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def selection_sort_using_min_func(arr:list):
    for idx in range(len(arr)-1):
        min_idx = find_min_idx(arr[idx:]) + idx
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]

data = [3,10,2,16,7,19,4,1,5]
selection_sort_using_min_func(data)
print(data)


def selection_sort(arr:list[int]):
    for idx in range(len(arr)):
        min_idx = idx
        for j in range(idx+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # swap
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]

data = [3,10,2,16,7,19,4,1,5]
selection_sort(data)
print(data)