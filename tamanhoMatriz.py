matriz = ([[1, 2], [3, 4]])
        
def dimensoes(matriz):
    dimensao = 0
    linhas = 0
    colunas = 0
    for i in range(len(matriz)):
        linhas += 1
        for j in range(len(matriz[0])):
            colunas += 1
    print( f'{linhas}X{colunas}')
        

