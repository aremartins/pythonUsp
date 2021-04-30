def dimensao(matriz):
    linha = 0
    coluna = 0
    for i in matriz:
        linha = linha +1
        for j in matriz[0]:
            coluna = coluna + 1
    print (linha,"X", coluna, sep = "")

matriz = [[1], [2], [3]]

def dimensoes(matriz):
    a = len(matriz)
    b = len(matriz([0]))
    print(a,"X", b)

dimensoes(matriz)
