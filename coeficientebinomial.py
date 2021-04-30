def fatorial(n):
    fator = 1
    while n > 1:
        fator = fator * n
        n = n -1
    return fator

def numero_binomial(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))


def testa_fatorial():
    if fatorial(1) == 1:
        print("funciona para 1")
    else:
        print("não funciona para 1")
    if fatorial(2) == 2:
        print("funciona para 2")
    else:
        print("não funciona para 2")
    if fatorial(0) == 1:
        print("funciona para 0")
    else:
        print("não funciona para 0")
    if fatorial(5) == 120:
        print("funciona para 5")
    else:
        print("não funciona para 5")


def testa_binomial():
    if numero_binomial(9,3) == 84:
        print("funciona para 9,3")
    else:
        print("não funciona para 9")
    if numero_binomial(4,2) == 6:
        print("funciona para 4,2")
    else:
        print("não funciona para 4")
    if numero_binomial(6,4) == 15:
        print("funciona para 6,4")
    else:
        print("não funciona para 6,4")
    
              
        
