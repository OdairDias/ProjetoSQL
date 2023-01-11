#primeiras imposrtações
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_compras=[]

principal='https://lista.mercadolivre.com.br/'

busca=input('Qual será a pesquisa de hoje?: ')
#print(principal+busca)
resposta= requests.get(principal+busca)

ml=BeautifulSoup(resposta.text, 'html.parser')

produtos=  ml.findAll( 'div', attrs= {'class':"andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default"})

for produto in produtos:

    nome_produto=produto.find('h2', attrs={'class':'ui-search-item__title'})

    link_produto=produto.find('a', attrs={'class':'ui-search-link'})

    preço_produtoreal= produto.find('span', attrs={'class':'price-tag-fraction'})
    preço_produtocentavos= produto.find('span', attrs={'class':'price-tag-cents'})

    if(preço_produtocentavos):
        lista_compras.append([nome_produto,preço_produtoreal.text, preço_produtocentavos.text,link_produto['href']])
    else:
      lista_compras.append([nome_produto,preço_produtoreal.text,'',link_produto['href']])

# print(ml.prettify())
    #print("titulo produto",nome_produto.text) 
    #print('link do produto:',link_produto['href'])
    #if (preço_produtocentavos):
        #print('Preço do produto: R$',preço_produtoreal.text  + ',' + preço_produtocentavos.text)
    #else:
       #print('Preço do produto: R$',preço_produtoreal.text) 
    #print('\n\n')

#class="andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default"

pesquisa=pd.DataFrame(lista_compras,columns=['Produto','Preço produto real','Preço centavos produto','Link produto'])
print(pesquisa)
pesquisa.to_excel('resultado_pesquisa.xlsx', index=False)