def bin_search(arr, x):
    comps = 0
    l = 0
    r = len(arr)-1;
    m = int((l+r)/2)
    
    while (arr[m] != x):
        comps += 1
        if (arr[m]<x):
            l = m+1
        else:
            r = m-1
        comps +=1
        m = int((l+r)/2)
    
    print(m)
    print('Comps = {}'.format(comps-1))
    
if __name__ == '__main__':
    arr = [0,3,4,5,6,7,8,9,10,12,13,15,16,17,19]
    x = 6
    print('Array:', arr)
    bin_search(arr, x)