import os
import functions as fc

numeroInstituto = input("Insira o número do instituto\n")
pastaInstituto = fc.procurarNomes(int(numeroInstituto))

files = [f for f in os.listdir(pastaInstituto)]
files.sort()
logResponsaveis = open("logResponsaveis.txt", "a")
logResponsaveis.close()
logResponsaveis = open("logResponsaveis.txt", "r")

#Adiciona o nome da pasta do instituto buscado
if not fc.procurarRepeticao(logResponsaveis, pastaInstituto):
  logResponsaveis.close()
  logResponsaveis = open("logResponsaveis.txt", "a")
  logResponsaveis.write(pastaInstituto + "\n")

logResponsaveis.close()
logResponsaveis = open("logResponsaveis.txt", "r")

for filename in files:
 name = pastaInstituto + "/" + filename
 dados = open(name, "r")
 responsavel = fc.procurarResponsavel(dados)

 if not fc.procurarRepeticao(logResponsaveis, responsavel):
   logResponsaveis.close()
   logResponsaveis = open("logResponsaveis.txt", "a")
   logResponsaveis.write(responsavel + "\n")

 logResponsaveis.close()
 logResponsaveis = open("logResponsaveis.txt", "r")

 dados.close()
logResponsaveis.close()
