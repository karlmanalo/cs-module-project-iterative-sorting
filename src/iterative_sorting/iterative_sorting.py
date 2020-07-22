# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    # Iterating over sorted-unsorted boundary 
    for i in range(len(arr)):
        current_index = i
        smallest_index = current_index
        smallest_value = arr[i]
        
        # Comparing values in unsorted boundary to current candidate for lowest value
        for j in range(i + 1, len(arr)):
            if arr[j] < smallest_value:
                smallest_index = j
                smallest_value = arr[j]

        # Swapping lowest value to current index of sorted-unsorted boundary
        if current_index != smallest_index:
            arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    # Iterating through all elements of array
    for i in range(len(arr) - 1):
        # Iterating from first element to i - 1 (The last i elements are sorted)
        for j in range(len(arr) - i - 1):
            # Swapping elements if index j's value is greater than index j + 1's value
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
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
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
