numero = input("Digite um número inteiro: ")
soma_digitos = 0
# Itera sobre cada dígito do número
for digito in numero:
    # Converte o dígito de string para inteiro e adiciona à soma
    soma_digitos += int(digito)
print(soma_digitos)
