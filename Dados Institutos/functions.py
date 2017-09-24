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
            achou = True
            break
    if achou:
        return linhaSeguinte
    else:
        return "Erro"


def procurarResponsavel(arquivo):
    linhaResponsavel = procurarNoArquivo(arquivo, 'Responsável')
    linhaResponsavel = linhaResponsavel.split()
    linhaResponsavel.remove(linhaResponsavel[0])
    linhaResponsavel = " ".join(linhaResponsavel)

    return linhaResponsavel

def procurarRepeticao(arquivo, texto): #retorna True se texto repete e False se não
    linhas = arquivo.readlines()
    achou = False
    for linha in linhas:
        if texto in linha:
            achou = True
            break
    return achou

teste = open('CebiMar-030/teste000002.txt', 'r')
print(procurarResponsavel(teste))
