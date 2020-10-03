def linear_search(arr, target):
    for a in range(len(arr)):
        if(arr[a] == target):
            return a
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    arr.sort()
    start = 0
    end = len(arr)-1
    middle_index = -1

    while end >= start:
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            return middle_index
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1
    return middle_index
    
    # return -1  # not found


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

print(binary_search(arr1, -8))
