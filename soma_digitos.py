numero = int(input("Digite um número inteiro: "))

soma_digitos = 0

# Enquanto o número for maior que zero, continuamos separando os dígitos e somando
while numero > 0:
    # Pegamos o último dígito usando o operador de módulo (%)
    ultimo_digito = numero % 10
    # Adicionamos o último dígito à soma
    soma_digitos += ultimo_digito
    # Removemos o último dígito do número usando divisão inteira (//)
    numero //= 10

print("A soma dos dígitos é:", soma_digitos)
