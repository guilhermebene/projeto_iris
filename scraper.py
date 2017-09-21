import requests
from bs4 import BeautifulSoup
import time
import os
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def selecionarUnidade():
    achou = False
    print("Digite o instituto ou unidade para baixar")
    instituto = input()
    listaInstitutos = open("Códigos Institutos")
    
    for line in listaInstitutos:
      
       x = listaInstitutos.readline()
       Y = similar(x, instituto)
       
       if(Y > 0.2):
          print(x)
          achou = True
    
    
    if (achou == True):
       print("Estes foram os resultados obtidos, digite agora o código ideal, ignore os '0' presentes à esquerda do número")
       listaInstitutos.close()
    
    else:
       print(listaInstitutos.readlines())

    

def itemData(i): #função retorna a sopa da ficha do item de código i

    rURL = URL.replace("##START_INDEX##", str(unidade).rjust(3, '0') + '.' + str(i).rjust(6,'0'))

    pageSoup = BeautifulSoup(requests.get(rURL).text, "html.parser") #sopa da página do item

    dataSoup = pageSoup.find("table", align = 'center', cellspacing ='1') #sopa da ficha do item

    return dataSoup


          	

def main():

    for n in range(inicial, final + 1):
        print(str(unidade).rjust(3, '0') + '.' + str(n).rjust(6, '0'))
        dataSoup = itemData(n)
        myFile = open("teste" + str(n).rjust(6, '0') + ".txt", "w")
        if dataSoup is not None:
            myFile.write(dataSoup.get_text())
        else:
            myFile.write("Erro")
        myFile.close()


selecionarUnidade()
inicio = time.time()

URL = "https://uspdigital.usp.br/mercurioweb/PatrimonioMostrar?numpat=##START_INDEX##"
unidade = input('Unidade: ')
inicial = int(input('Ínicio: '))
final = int(input('Fim: '))




main()

fim = time.time()
tempo = fim - inicio

print("Tempo de execução: " + str((tempo/60)//1) + ' minuto e ' + str((tempo%60)//1) + " segundos")

