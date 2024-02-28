# Exercício 2
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

for i in range(altura):
    for j in range(largura):
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()  # Quebra de linha após cada linha do retângulo
