import requests
from bs4 import BeautifulSoup
import time

inicio = time.time()

URL = "https://uspdigital.usp.br/mercurioweb/PatrimonioMostrar?numpat=##START_INDEX##"
unidade = 7
inicial = 1
final = 12460

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

main()

fim = time.time()
print("Tempo de execução: " + str(fim - inicio) + "segundos")
myfile.close()

