def eh_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def maior_primo(num):
    for i in range(num, 1, -1):
        if eh_primo(i):
            return i

# Exemplos de execução
print(maior_primo(100))  # Saída: 97
print(maior_primo(7))    # Saída: 7
