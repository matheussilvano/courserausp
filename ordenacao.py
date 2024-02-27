# Recebendo os três números inteiros na entrada
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

# Verificando se os números estão em ordem crescente e imprimindo o resultado
if numero1 < numero2 < numero3:
    print("crescente")
else:
    print("não está em ordem crescente")
