n = int(input("Digite um número inteiro positivo: "))

contador = 0
numero = 1

print("Os", n, "primeiros números ímpares naturais são:")

while contador < n:
    print(numero)
    numero += 2
    contador += 1
