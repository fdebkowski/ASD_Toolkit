def partition(arr):
    l = -1
    r = 0
    n = len(arr)
    tmp = 0
    
    while r<n-1:
        if arr[r]<arr[n-1]:
            if r>l+1:
                tmp = arr[l+1]
                arr[l+1] = arr[r]
                arr[r] = tmp
            l+=1
        r+=1
        
    if l+1<n-1:
        tmp = arr[l+1]
        arr[l+1] = arr[n-1]
        arr[n-1] = tmp
    
    print('split = ' + str(l+1))
    return l+1

def hoare_partition(arr, k):
    m = 0
    tmp = 0
    n = len(arr)
    
    m = partition(arr)
    if n-m==k:
        print(m)
        return m
    else:
        if n-m>k:
            tmp = m+1+hoare_partition(arr[m+1:], k)
        else:
            tmp = hoare_partition(arr[:m], k-(n-m))
    
    print('tmp = ' + str(tmp))
    return tmp

def quick_sort_partiion(arr):
    print('QuickSort Executed')
    print(arr)
    m = 0
    n = len(arr)
    
    m = partition(arr)
    
    if m>1:
        quick_sort_partiion(arr[:m])
    if (n-m-1)>1:
        quick_sort_partiion(arr[m+1:])

if __name__ == '__main__':
    arr = [19,12,5,4,6,10,9,8,16,7,3]
    quick_sort_partiion(arr)