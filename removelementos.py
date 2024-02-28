def remove_repetidos(lista):
    lista_sem_repeticao = sorted(set(lista))
    return lista_sem_repeticao

# Exemplo de uso:
lista = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista))  # Saída: [1, 2, 3, 4]
print(remove_repetidos([1, 2, 3, 3, 3, 4]))  # Saída: [1, 2, 3, 4]
