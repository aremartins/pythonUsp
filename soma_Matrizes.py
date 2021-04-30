m1 = ([[1, 2], [3, 4]])
m2 =([[1, 2], [3, 4]])


        
def soma_matrizes(m1, m2):
    if len(m1) !=  len(m2) or len(m1[0]) != len(m2[0]):
        return False
    else:
        calculo = m1
        linsm1 = len(m1)
        colsm1 = len(m1[0])
        for i in range(linsm1):
            for j in range(colsm1):
                calculo[i][j] = m1[i][j] + m2[i][j]
        return calculo
        
                
        

