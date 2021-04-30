num = int(input("Informe uma sequencia de numeros: "))
var = 0
a = 0
u=0
while num !=0:
    u = num % 10
    num = num // 10
    a = num % 10
    if a == u:
        var = var + 1
if var > 0:
    print('sim')
else:
    print('não')
