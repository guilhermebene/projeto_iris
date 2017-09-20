import os
from difflib import SequenceMatcher

def similar(a, b):
 return SequenceMatcher(None, a, b).ratio()

print("Qual objeto deseja procurar? (Não use palavras compostas)")
objeto = input()
objeto = objeto.upper()

files = [f for f in os.listdir("DadosMedRib")]
for filename in files:
 Dados = open("DadosMedRib/" + filename, "r", encoding="utf8")
 Dados.readline()
 for line in Dados:
  x = Dados.readline()
  Y = similar(x, objeto)
  if(Y > 0.6):
      print(x)
      print(filename)
      Dados.close()
      break	
