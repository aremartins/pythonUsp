lista = [1,2,3,4,5,6,6,6,7,7,8]
lista_nova = []

def remove_repetidos(lista):
    lista.sort()
    for i in lista:
        if i not in lista_nova:
            lista_nova.append(i)
        return (lista_nova)
