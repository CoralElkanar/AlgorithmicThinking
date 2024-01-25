"""
Question: 
Selection sort algorithm - finds the smallest element in the list and exchange it with the element in the first 
position of the list. 
repeat until the end of the list.
"""


def find_min_idx(arr:list):
    min_idx = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

data = [2,4,1,5]
def selection_sort(arr:list):
    for idx in range(len(arr)-1):
        min_val = find_min_idx(arr[idx:])
        min_idx = arr.index(min_val)
        arr[idx], arr[min_idx] = min_val, arr[idx]

selection_sort(data)
print(data)