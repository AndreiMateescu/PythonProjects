def partitii(n):
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(i,j):
                sum = sum + k
            if sum == n:
                for l in range(i,j):
                    print(l, end = ' ')
                print('\n')


def invers(i):
    inv = 0
    aux = i
    while aux != 0:
        inv = inv*10 + aux%10
        aux = aux//10

    if inv == i:
        return 1
    else:
        return 0


def palindrom(n):
    numar = 1
    i = 1
    while numar <= n:
        if invers(i) == 1:
            numar += 1;
        i += 1
    return i-1