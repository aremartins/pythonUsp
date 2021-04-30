matriz = [1,2,3], [4,5,6]

def dimensoes(matriz):
    linha = 0
    coluna = 0
    for i in matriz:
        linha = linha +1
    for j in matriz[0]:
        coluna = coluna + 1
    return (linha,"X", coluna)
    
