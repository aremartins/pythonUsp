a = int(input("Entre com um número: "))

div = 0
for i in range(1, a+1):
    resto = a % i
    if resto == 0:
        div =div + 1
        
if div == 2:
    print("primo")
else:
    print("não primo")
