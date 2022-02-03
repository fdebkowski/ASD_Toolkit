"""Python program for implementation of Insertion Sort
"""
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    
    swaps = 0
    comps = 0
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
            comps += 1
        arr[j + 1] = key
        comps += 1
        
        print('Arr:{}   Iteration:{} Swaps:{} Comps:{}'.format(arr, i, swaps, comps))
        
# Driver code to test above
if __name__ == '__main__':
    nums = [5,4,3,2,1]
    insertion_sort(nums)
    print(nums)
