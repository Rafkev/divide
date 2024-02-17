def binary_search(arr, target):
    """
    Perform binary search to find the index of the target element in a sorted array.

    Parameters:
    - arr: A sorted array.
    - target: The element to search for.

    Returns:
    - The index of the target element if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
index = binary_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found.")
