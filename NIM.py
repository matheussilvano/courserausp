def computador_escolhe_jogada(n, m):
    """
    Função que determina a jogada do computador.

    Recebe como parâmetros o número atual de peças no tabuleiro (n) e o limite máximo de peças a serem retiradas (m).
    Retorna o número de peças que o computador deve retirar.
    """
    if n <= m:
        return n
    else:
        return (n % (m + 1))


def usuario_escolhe_jogada(n, m):
    """
    Função que solicita ao usuário sua jogada.

    Recebe como parâmetros o número atual de peças no tabuleiro (n) e o limite máximo de peças a serem retiradas (m).
    Retorna o número de peças que o usuário escolheu.
    """
    jogada = 0
    while jogada < 1 or jogada > m or jogada > n:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada < 1 or jogada > m or jogada > n:
            print("Oops! Jogada inválida! Tente novamente.")
    return jogada


def partida():
    """
    Função que inicia uma partida do jogo NIM.
    """
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    jogador = 0  # 0 indica que o jogador é o computador, 1 indica que o jogador é o usuário

    if n % (m + 1) == 0:
        print("Você começa!")
        jogador = 1
    else:
        print("Computador começa!")

    while n > 0:
        if jogador == 0:  # Vez do computador
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peça(s).")
            jogador = 1
        else:  # Vez do usuário
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peça(s).")
            jogador = 0
        n -= jogada

    if jogador == 0:  # Se o computador jogou por último, o usuário ganhou
        print("Você ganhou!")
        return 1
    else:  # Se o usuário jogou por último, o computador ganhou
        print("O computador ganhou!")
        return 0


def campeonato():
    """
    Função que inicia um campeonato do jogo NIM, composto por 3 partidas.
    """
    print("**** Campeonato ****")

    vitorias_usuario = 0
    vitorias_computador = 0

    for rodada in range(1, 4):
        print(f"**** Rodada {rodada} ****")
        vencedor = partida()
        if vencedor == 1:
            vitorias_usuario += 1
        else:
            vitorias_computador += 1

    print("**** Final do Campeonato ****")
    print(f"Placar: Você {vitorias_usuario} X {vitorias_computador} Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    opcao = int(input())

    if opcao == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif opcao == 2:
        print("Você escolheu um campeonato!")
        campeonato()
    else:
        print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
