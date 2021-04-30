x = int(input("Digite a largura: "))
y = int(input("Digite a altura: "))

print("#" * x)
for i in range(y -2):
    a = x - 4
    print("#", a * " ", "#", end="\n" )
    y = y -1
print("#" * x)
