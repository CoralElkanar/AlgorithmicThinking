"""
"""
import random

def binary_search(arr:list[int], target:int):
    left = 0
    right = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:  # arr[mid] > target
            right = mid - 1
    return mid

n = 10
max_val = 100
data = [random.randint(1, max_val) for i in range(n)]
data.sort()
print("list: ",data)
target = int(input("Enter target value: "))
target_pos = binary_search(data, target)
if target_pos == -1:
    print("Your target value is not in the list.")
else:
    print(f"Your target value has been found at index {target_pos}")
