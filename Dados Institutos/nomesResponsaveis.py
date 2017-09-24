import os
import functions as fc

numeroInstituto = input("Insira o número do instituto\n")
pastaInstituto = fc.procurarNomes(int(numeroInstituto))
responsavel = ""
files = [f for f in os.listdir(pastaInstituto)]
for filename in files:
 dados = open(pastaInstituto + "/" + filename, "r", encoding = "utf8")
 for line in dados:
  x = dados.readline()
  print(x)
  if(x == "Responsável:"):
   responsavel = dados.readline()
   break
 dados.close()
 print(responsavel)
