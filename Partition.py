def partition(arr):
    l = -1
    r = 0
    n = len(arr)
    tmp = 0
    swaps = 0
    comps = 0

    while r < n-1:
        comps += 1
        if arr[r] < arr[n-1]:
            if r > l+1:
                tmp = arr[l+1]
                arr[l+1] = arr[r]
                arr[r] = tmp
                swaps += 1
                print('l = {}   r = {}  swaps = {}  comps = {}'.format(l+1,r+1,swaps,comps))
                print(arr)
            l += 1
        r += 1
    if l+1 < n-1:
        tmp = arr[l+1]
        arr[l+1] = arr[n-1]
        arr[n-1] = tmp

    print('split = ' + str(l+1))
    return l+1


def hoare_partition(arr, k):
    print('Hoare exec ! k = {}   Arr = {}'.format(k, arr))
    m = 0
    tmp = 0
    n = len(arr)

    m = partition(arr)
    if n-m == k:
        print(m)
        return m
    else:
        if n-m > k:
            tmp = m+1+hoare_partition(arr[m+1:], k)
        else:
            tmp = hoare_partition(arr[:m], k-(n-m))

    print('tmp = ' + str(tmp))
    return tmp


def quick_sort_partition(arr):
    print('QuickSort Executed')
    print(arr)
    m = 0
    n = len(arr)

    m = partition(arr)

    if m > 1:
        quick_sort_partition(arr[:m])
    if (n-m-1) > 1:
        quick_sort_partition(arr[m+1:])


if __name__ == '__main__':
    arr = [19,13,14,10,2,1,12,18,8,3,7,11,9]
    k = 9
    # partition(arr)
    partition(arr)
    # quick_sort_partition(arr)
