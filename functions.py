def procurarNomes(unidade):
    nomes = open('NomesPastas')
    linhas = nomes.read().splitlines()
    nome = linhas[unidade-1]
    nomes.close()

    return nome
