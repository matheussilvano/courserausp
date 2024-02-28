import re

def le_assinatura():
    '''A função lê os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def separa_sentenca(texto):
    '''A função recebe um texto e devolve uma lista das sentenças dentro do texto'''
    return re.split(r'[.!?]+', texto)

def separa_frase(sentenca):
    '''A função recebe uma sentença e devolve uma lista das frases dentro da sentença'''
    return re.split(r'[,:;]+', sentenca)

def calcula_assinatura(texto):
    '''Essa função recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentenca(texto)
    frases = [separa_frase(sentenca) for sentenca in sentencas]

    # IMPLEMENTAR - Cálculo dos traços linguísticos

def compara_assinatura(as_a, as_b):
    '''Essa função recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # IMPLEMENTAR - Cálculo da similaridade entre as assinaturas

def avalia_textos(textos, ass_cp):
    '''Essa função recebe uma lista de textos e uma assinatura ass_cp e deve devolver o número (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    # IMPLEMENTAR - Comparação das assinaturas dos textos com a assinatura de referência

def main():
    assinatura_referencia = le_assinatura()
    textos = le_textos()
    texto_infectado = avalia_textos(textos, assinatura_referencia)
    print("O autor do texto", texto_infectado, "está infectado com COH-PIAH")

if __name__ == '__main__':
    main()
