def procurarNomes(unidade):
    nomes = open('NomesPastas')
    linhas = nomes.read().splitlines()
    nome = linhas[unidade-1]
    nomes.close()

    return nome

def procurarNoArquivo(arquivo, texto):
    linhas = arquivo.readlines()
    achou = False
    for linha in linhas:
        if texto in linha:
            i = linhas.index(linha)
            linhaSeguinte = linhas[i+1].rstrip()
            break

    return linhaSeguinte

def procurarResponsavel(arquivo):
    linhaResponsavel = procurarNoArquivo(arquivo, 'Responsável')
    linhaResponsavel = linhaResponsavel.split()
    linhaResponsavel.remove(linhaResponsavel[0])
    linhaResponsavel = " ".join(linhaResponsavel)

    return linhaResponsavel
