import random
# TO-DO: Complete the selection_sort() function below
def selection_sort(arr): # O(n^2)
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(smallest_index, len(arr)):
            if arr[j] < arr[smallest_index]:                
                smallest_index = j
        # TO-DO: swap 
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr): # O(n^2)
    # Your code here
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None): # O(n+k) , because it doesn't work good for big numbers
    # Your code here
    if len(arr) > 0:
        if min(arr) < 0:
            return "Error, negative numbers not allowed in Count Sort"
        # maximum number in arr
        maximum = max(arr) 
        # arr length
        size = len(arr)
        # temp output array
        output = [0] * size
        # count array
        count = [0] * (maximum+1)

        # Store the count of each elements in count array
        for i in range(0, size):
            count[arr[i]] += 1

        # Store the cummulative count
        for j in range(1, maximum+1):
            count[j] += count[j - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        k = size - 1
        while k >= 0:
            output[count[arr[k]] - 1] = arr[k]
            count[arr[k]] -= 1
            k -= 1

        # Copy the sorted elements into original array
        for n in range(0, size):
            arr[n] = output[n]
       
    return arr


l = [8, 2, 5, 5, 1, 6, 50000000 ]
print(counting_sort(l))
