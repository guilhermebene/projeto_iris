import os
from functions import *

numeroInstituto = input("Insira o número do instituto\n")
pastaInstituto = procurarNomes(int(numeroInstituto))

files = [f for f in os.listdir(pastaInstituto)]
files.sort()

nameFolder = pastaInstituto + '-Dados'
os.mkdir(nameFolder)

for filename in files:
    name = pastaInstituto + '/' + filename
    dadoGerado = open(nameFolder + '/' + filename[5:], 'w')

    dadoGerado.write(numeroInstituto + filename[5:11] + '\n')
    dadoGerado.write(numeroInstituto + '\n')
    
    dados = open(name, 'r')
    dadoGerado.write(procurarNumResponsavel(dados) + ' ')
    dados.close()

    dados = open(name, 'r')
    dadoGerado.write(procurarNomeResponsavel(dados) + '\n')
    dados.close()
    
    dados = open(name, 'r')
    dadoGerado.write(procurarMaterial(dados) + '\n')
    dados.close()
    
    dados = open(name, 'r')
    dadoGerado.write(procurarSituacao(dados) + '\n')
    dados.close()

    dados = open(name, 'r')
    dadoGerado.write(procurarUtilizacao(dados) + '\n')
    dados.close()

    dados = open(name, 'r')
    dadoGerado.write(procurarLocal(dados) + '\n')
    dados.close()

    dados = open(name, 'r')
    dadoGerado.write(procurarComplemento(dados) + '\n')
    dados.close()

    dados = open(name, 'r')
    dadoGerado.write(procurarMarca(dados) + '\n')
    dados.close()

    dados = open(name, 'r')
    dadoGerado.write(procurarModelo(dados) + '\n')
    dados.close()

    dados = open(name, 'r')
    dadoGerado.write(procurarTipo(dados) + '\n')
    dados.close()

    dadoGerado.close()

