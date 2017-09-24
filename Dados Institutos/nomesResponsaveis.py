import os
import functions as fc

numeroInstituto = input("Insira o número do instituto\n")
pastaInstituto = fc.procurarNomes(int(numeroInstituto))
responsavel = ""

files = [f for f in os.listdir(pastaInstituto)]
logResponsaveis = open("logResponsaveis.txt", "a+")
if pastaInstituto not in logResponsaveis.readlines():
 logResponsaveis.write(pastaInstituto + "\n")

for filename in files:
 name = pastaInstituto + "/" + filename
 dados = open(name, "r", encoding = "utf8")
 responsavel = fc.procurarResponsavel(dados)
 if responsavel not in logResponsaveis.readlines():
  logResponsaveis.write(responsavel + "\n")
 dados.close()
logResponsaveis.close()
