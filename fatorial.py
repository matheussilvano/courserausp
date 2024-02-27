# Solicita o valor de n ao usuário
n = int(input("Digite o valor de n: "))

# Inicializa o fatorial como 1
fatorial = 1

# Calcula o fatorial de n
if n == 0:
    fatorial = 1
else:
    for i in range(1, n + 1):
        fatorial *= i

# Imprime o resultado
print(fatorial)
