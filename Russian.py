def russian(a,b):
    res = 0
    i = 0
    while True:
        i += 1
        if b % 2 != 0:
            res += a
        a = int(a*2)
        b = int(b/2)
        print ('iter = {}   a = {}   b = {}'.format(i,a,b))
        if b <= 0:
            break
    print('res = {}'.format(res))

russian(4,8)