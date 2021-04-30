def maior_primo(x):


    primo = x
    divisor = 2
    maior = False

    while maior == False:

        while primo % divisor != 0 and divisor ** 2 <= primo:
            divisor = divisor + 1


        if primo % divisor != 0 and divisor ** 2 >= primo:
            maior = True


        elif divisor ** 2 <= primo or primo % divisor == 0:
            primo = primo - 1
            divisor = 2


    if maior == True:
        return(primo)
