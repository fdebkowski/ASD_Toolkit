def my_split(arr):

    l = 1
    r = len(arr) - 1
    tmp = 0

    while (l <= r):
        
        while ((l <= r) and (arr[r] > arr[0])):
            r-=1
        while ((l <= r) and (arr[l] < arr[0])):
            l+=1

        if (l < r):
            tmp = arr[l]
            arr[l] = arr[r]
            arr[r] = tmp
            l+=1
            r-=1

    if (r > 0):
        tmp = arr[0]
        arr[0] = arr[r]
        arr[r] = tmp

    print(arr)
    print("r = " + str(r))
    print("val r = " + str(arr[r]))
    return(r)

def hoare_split(arr ,k):
    m = 0
    tmp = 0
    n = len(arr)
    
    m = my_split(arr)
    if n-m==k:
        print(m)
        return m
    else:
        if n-m>k:
            tmp = m+1+hoare_split(arr[m+1:n], k)
        else:
            tmp = hoare_split(arr[:m], k-(n-m))
    
    print('tmp = ' + tmp)
    return tmp

def quick_sort_split(arr):
    print('QuickSort Executed')
    print(arr)
    m = 0
    n = len(arr)
    
    m = my_split(arr)
    
    if m>1:
        quick_sort_split(arr[:m])
    if (n-m-1)>1:
        quick_sort_split(arr[m+1:])
    
if __name__ == '__main__':
    arr = [6,8,5,7,4]
    print('Array:', arr)
    my_split(arr)
