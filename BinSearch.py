def bin_search(arr, x):
    l = 0
    r = len(arr)-1;
    m = (l+r)/2
    
    while (arr[m] != x):
        if (arr[m]<x):
            l = m+1
        else:
            r = m-1
        m = (l+r)/2
    
    print(m)
    
if __name__ == '__main__':
    arr = [0,1,2,3]
    x = 2
    print('Array:', arr)
    bin_search(arr, x)