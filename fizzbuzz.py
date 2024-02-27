# Recebendo o número inteiro na entrada
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é divisível por 3 e por 5 e imprimindo "FizzBuzz" ou o número
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
else:
    print(numero)
