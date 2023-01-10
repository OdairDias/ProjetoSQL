#primeiras imposrtações
import requests
from bs4 import BeautifulSoup

principal='https://lista.mercadolivre.com.br/'

busca=input('Qual será a pesquisa de hoje?')
#print(principal+busca)
resposta= requests.get(principal+busca)

ml=BeautifulSoup(resposta.text, 'html.parser')
print(ml.prettify())