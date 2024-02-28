import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    return re.split(r'[.!?]+', texto)


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def calcula_tamanho_medio_palavras(palavras):
    '''A funcao recebe uma lista de palavras e devolve o tamanho medio das palavras'''
    total_caracteres = sum(len(palavra) for palavra in palavras)
    return total_caracteres / len(palavras)


def calcula_type_token(palavras):
    '''A funcao recebe uma lista de palavras e devolve a relacao Type-Token'''
    palavras_unicas = set(palavras)
    return len(palavras_unicas) / len(palavras)


def calcula_hapax_legomana(palavras):
    '''A funcao recebe uma lista de palavras e devolve a Razao Hapax Legomana'''
    freq_palavras = {}
    for palavra in palavras:
        freq_palavras[palavra] = freq_palavras.get(palavra, 0) + 1

    hapax_legomana = sum(1 for palavra, freq in freq_palavras.items() if freq == 1)
    return hapax_legomana / len(palavras)


def calcula_tamanho_medio_sentenca(sentencas):
    '''A funcao recebe uma lista de sentencas e devolve o tamanho medio das sentencas'''
    total_caracteres = sum(len(sentenca) for sentenca in sentencas)
    return total_caracteres / len(sentencas)


def calcula_complexidade_sentenca(frases, sentencas):
    '''A funcao recebe uma lista de frases e uma lista de sentencas e devolve a complexidade media das sentencas'''
    return len(frases) / len(sentencas)


def calcula_tamanho_medio_frase(frases):
    '''A funcao recebe uma lista de frases e devolve o tamanho medio das frases'''
    total_caracteres = sum(len(frase) for frase in frases)
    return total_caracteres / len(frases)


def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = [frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    palavras = [palavra for frase in frases for palavra in separa_palavras(frase)]

    tam_medio_palavra = calcula_tamanho_medio_palavras(palavras)
    type_token = calcula_type_token(palavras)
    hapax_legomana = calcula_hapax_legomana(palavras)
    tam_medio_sentenca = calcula_tamanho_medio_sentenca(sentencas)
    complexidade_sentenca = calcula_complexidade_sentenca(frases, sentencas)
    tam_medio_frase = calcula_tamanho_medio_frase(frases)

    return [tam_medio_palavra, type_token, hapax_legomana, tam_medio_sentenca, complexidade_sentenca, tam_medio_frase]


def compara_assinatura(as_a, as_b):
    '''A funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similaridade = 0
    for i in range(len(as_a)):
        similaridade += abs(as_a[i] - as_b[i])
    return similaridade / 6


def avalia_textos(textos, ass_cp):
    '''A funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = []

    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_texto, ass_cp)
        similaridades.append(similaridade)

    return similaridades.index(min(similaridades)) + 1


def main():
    ass_cp = le_assinatura()
    print("Assinatura do aluno infectado: ", ass_cp)
    n = int(input("Digite o número de textos a serem analisados: "))
    textos = []
    for i in range(n):
        print(f"Digite o texto {i + 1}: ")
        texto = input()
        textos.append(texto)
    texto_infectado = avalia_textos(textos, ass_cp)
    print("O autor do texto", texto_infectado, "está infectado com COH-PIAH.")

if __name__ == "__main__":
    main()
