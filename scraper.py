import requests
from bs4 import BeautifulSoup
import time

inicio = time.time()

URL = "https://uspdigital.usp.br/mercurioweb/PatrimonioMostrar?numpat=##START_INDEX##"
unidade = input('Unidade: ')
inicial = int(input('Ínicio: '))
final = int(input('Fim: '))

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

main()

fim = time.time()
tempo = fim - inicio
print("Tempo de execução: " + str((tempo/60)//1) + ' min e ' + str((tempo%60)//1) + " segundos")
