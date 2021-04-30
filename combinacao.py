def fatorial(n):
    x = n
    a = 1

    while x > 0:
        a =x * a
        x = x -1
    return(a)

def combinacao(n,k):
    return fatorial(n) / (fatorial(k)* fatorial(n - k))

