matriz = [[1, 1, 5, 7, 8, 9], [2, 3, 5, 7, 8, 9],[1, 1, 5, 7, 8, 9], [2, 3, 5, 7, 8, 9],[1, 1, 5, 7, 8, 9], [2, 3, 5, 7, 8, 9],[1, 1, 5, 7, 8, 9], [2, 3, 5, 7, 8, 9],[1, 1, 5, 7, 8, 9], [2, 3, 5, 7, 8, 9]]

def imprime_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print(matriz[i][j])
            else:
                print(matriz[i][j], end = " ")
  
    '''criar uma função(imprime_matriz) que receba uma matriz como parâmetro e imprima a matriz linha por linha.
    Obs: Os espaços após o último elemento de cada linha não devem ser impressos.'''


