def e_primo(n):
    div = 0
    for i in range (1, n+1):        
        resto = n % i
        if resto == 0:
            div =div + 1

    if div == 2:
        return n
    else:
        return False
    
def maior_primo(n):
    maior = 0
    lista = []
    maior_p = 0
    for i in range (1, n):
        maior = e_primo(i)
        i = i +1
        if maior != False:
            lista.append(maior)
    print(lista[-1])
        
