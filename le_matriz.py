def cria_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            valor = int(input("Informe o elemento [" + str(i) + "][" + str(j) +"]: "))
            linha.append(valor)            
        matriz.append(linha)
        print(end = "")
    return matriz


def le_matriz():
    lin = int(input("Digite o número de linhas: "))
    col = int(input("Digite o número de colunas: "))
    return cria_matriz(lin, col)
        




    
    

              
            
            
            
        
