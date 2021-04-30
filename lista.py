n = int(input('Digite uma sequencia de números terminados em 0: '))
lista = []
while n != 0:
    n = int(input('Digite o próximo numero: '))
    lista.append(n)
print(lista[::-1])
lista.reverse()
print(lista)

     
          
