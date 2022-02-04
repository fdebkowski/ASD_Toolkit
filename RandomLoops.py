def alg_a(n,m):
    k=1
    while(k<=n):
        n-=m
        m-=n
        k/=m*n
        print('{} {} {}'.format(n,m,k))
    
alg_a(1990,100)
