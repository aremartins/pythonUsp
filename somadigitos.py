n = int(input("Digite um número: "))
soma= 0
x= 0
while n > 0:
    x = n % 10
    n = n // 10
    soma= soma + x
print(soma)
              
              
