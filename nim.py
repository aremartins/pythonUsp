def computador_escolhe_jogada(n,m):
    if n <= m:
        return n
    else:
        q = n % (m+1)
        if q > 0:
            return q
        return m


def usuario_escolhe_jogada(n, m):
    jogada= 0
    while jogada == 0:
        jogada= int(input("Quantas peças vai tirar?"))
        if jogada > n or jogada > m or jogada < 1:
            print("")
            print("Jogada não válida!")
            print("")
            jogada= 0
    return jogada    

def partida():
    print("")
    n= int(input("Quantas peças? "))
    m= int(input("Limite de peças por jogada? "))
    x= n%(m+1)
    inicio_usuario= False
    inicio_computador= False
    if x != 0:
        pc_turn= True
        inicio_computador= True
    if x == 0:
        pc_turn= False
        inicio_usuario= True
    while n > 0:
        if pc_turn:
            if inicio_computador:
                print("")
                print("Computador começa!")
                print("")
            inicio_computador= False
            jogada=computador_escolhe_jogada(n,m)
            pc_turn= False
            if jogada == 1:
                print("O computador tirou uma peça")
            else:
                print("O computador retirou {} peças".format(jogada))

        else:
            if inicio_usuario:
                print("")
                print("Você começa!")
                print("")
            inicio_usuario= False
            jogada=usuario_escolhe_jogada(n,m)
            pc_turn=True
            if jogada == 1:
                print("Você tirou uma peça")
            else:
                print("Você tirou {} peças".format(jogada))
        n-=jogada
        if n > 0:
            print("Agora restam {} peças no tabuleiro".format(n))
    if pc_turn:
        print("Fim do jogo! Você ganhou!")
        print("")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        print("")
        return 0


def campeonato():
    computador=0
    usuario=0
    i=1
    for _ in range(3):
        print("**** Rodada {}! ****".format(i))
        print("")
        resultado=partida()
        i+=1
        if resultado==1:
            usuario+=1
        else:
            computador+=1
    print("**** Fim do Campeonato! ****")
    print("Placar: Você {} x {} Computador".format(usuario,computador))        
    return

tipo=0
while tipo==0:
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para um campeonato")
    tipo=int(input("Faça sua escolha: "))
