# Counting sort in Python programming

def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1
    print(count)

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    print(count)

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    print(count)

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [0, 0, 5, 1, 1, 0, 0, 3, 5, 0, 0, 0]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
