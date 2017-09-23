import os

numeroInstituto = input("Insira o número do instituto\n")
pastaInstituto

files = [f for f in os.listdir("pastaInstituto")]
for filename in files:
 dados = open(pastaInstituto + "/" + filename, "r", encoding = "utf8")
 for line in dados:
  if(line.readline() == "Responsável"):
   responsavel = line.readline()
   break
print(responsavel)
