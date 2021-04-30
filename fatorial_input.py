def main ():
    n = int(input("Digite um número: "))
    while n >= 0:
        fatorial(n)
        n = int(input("Digite o próximo numero: "))


def fatorial(n):
    fat = 1
    while n > 0:
        fat = n * fat
        n  = n - 1
    print(fat)

    
