import math

def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
    print("A maior temperatura do mês foi: ", máxima(temperaturas), "C.")
    print("A média das temperaturas para esse mês foi: ", median(temperaturas), "C.")
    
def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def median(temps):
    calculo = sum(temps)/len(temps)
    return calculo


def testa_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para o array ", temp)
        print("valor esperado: ", valor_esperado, ", Valor_calculado: ",valor_calculado)

def testa_pontualmax(temp, valor_esperado):
    valor_calculado = máxima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para o array ", temp)
        print("valor esperado: ", valor_esperado, ", Valor_calculado: ",valor_calculado)


def testa_minima():
    print("Iniciando os testes")
    testa_pontual([0],0)
    testa_pontual([0, 12, 15, -14], -14)
    print("Finalizando os testes")

def testa_maxima():
    print("Iniciando os testes")
    testa_pontualmax([0],0)
    testa_pontualmax([0, 12, 15, -14], 15)
    print("Finalizando os testes")
    

def máxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i +1
    return max

        
