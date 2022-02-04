def selection_sort(arr):
    swaps = 0
    comps = 0
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            comps += 1
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        if min_idx!=i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
        
        print('Arr:{}   Iteration:{} Swaps:{} Comps:{}'.format(arr, i+1, swaps, comps))


# Driver code to test above
if __name__ == "__main__":
    arr = [10,15,17,13,16,0,9,11]
    selection_sort(arr)
    print("Sorted array", arr)
