import os

def procurarNomes(unidade): #devolve o nome da unidade
    nomes = open('NomesPastas')
    linhas = nomes.read().splitlines()
    nome = linhas[unidade-1]
    nomes.close()

    return nome

def procurarNoArquivo(arquivo, texto): #devolve o contéudo da linha seguinte à linha onde foi encontrado o texto
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
        return "Nao encontrado"

def procurarNomeResponsavel(arquivo):
    linhaResponsavel = procurarNoArquivo(arquivo, 'Responsável')
    linhaResponsavel = linhaResponsavel.split()
    linhaResponsavel.remove(linhaResponsavel[0])
    linhaResponsavel = " ".join(linhaResponsavel)

    return linhaResponsavel

def procurarNumResponsavel(arquivo):
    linhaResponsavel = procurarNoArquivo(arquivo, 'Responsável')
    linhaResponsavel = linhaResponsavel.split()

    return linhaResponsavel[0]

def procurarMaterial(arquivo):
    linhas = arquivo.readlines()
    achou = False
    linhaSeguinte = ''
    Material = []
    for linha in linhas:
        if 'Material' in linha:
            i = linhas.index(linha)

            Material.append(linhas[i+1].rstrip())
            Material.append(linhas[i+2].rstrip())
            Material.append(linhas[i+3].rstrip())

            achou = True
            break
    if achou:
        Material = ' '.join(Material)
        Material = Material.split()
        Material.remove(Material[0])
        Material.remove('-')
        Material = ' '.join(Material)

        return Material
    else:
        return "Não encontrado"

def procurarSituacao(arquivo):
    return procurarNoArquivo(arquivo, 'Situação')

def procurarUtilizacao(arquivo):
    return procurarNoArquivo(arquivo, 'Utilização')

def procurarLocal(arquivo):
    return procurarNoArquivo(arquivo, 'Localização')

def procurarComplemento(arquivo):
    return procurarNoArquivo(arquivo, 'Complemento')

def procurarMarca(arquivo):
    return procurarNoArquivo(arquivo, 'Marca')

def procurarModelo(arquivo):
    return procurarNoArquivo(arquivo, 'Modelo')

def procurarTipo(arquivo):
    return procurarNoArquivo(arquivo, 'Tipo')

def procurarRepeticao(arquivo, texto): #retorna True se o texto repete e False se não
    linhas = arquivo.readlines()
    achou = False
    for linha in linhas:
        if texto in linha:
            achou = True
            break
    return achou

