import os
import functions as fc

numeroInstituto = input("Insira o número do instituto\n")
pastaInstituto = fc.procurarNomes(int(numeroInstituto))

files = [f for f in os.listdir(pastaInstituto)]
logResponsaveis = open("logResponsaveis.txt", "a+")

#Adiciona o nome da pasta do instituto buscado
if not fc.procurarRepeticao(logResponsaveis, pastaInstituto):
  logResponsaveis.write(pastaInstituto + "\n")

for filename in files:
 name = pastaInstituto + "/" + filename
 dados = open(name, "r", encoding = "utf8")
 responsavel = fc.procurarResponsavel(dados)

 if not fc.procurarRepeticao(logResponsaveis, responsavel):
  logResponsaveis.write(responsavel + "\n")
 dados.close()
logResponsaveis.close()
