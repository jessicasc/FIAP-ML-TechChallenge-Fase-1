import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)

categories = {}
titleList = []
imageList = []
availabilityList = []
priceList = []
ratingList = []
categoriesList = []
url_base = 'https://books.toscrape.com/'

def run_scraper():
    """acessar url e armazenar seu conteúdo em HTML para scrapping""" 
    response = requests.get(url_base)
    books = BeautifulSoup(response.text, 'html.parser')

    logger.info(f'Acessando url: {url_base}')

    """lista lateral de categorias"""    
    list = books.select("ul.nav.nav-list ul a")

    """armazenar a categoria e seu respectivo link"""
    for a in list:
        categoria = a.get_text(strip=True)
        link = urljoin(url_base, a["href"])
        categories[categoria] = link

    logger.info(f'Acessando informação de cada livro disponível no site')
    
    """acessar link de cada categoria"""
    for categoria, link_categoria in categories.items():

        link = link_categoria

        """percorrer todas as páginas"""
        while link:
            response = requests.get(link)
            books = BeautifulSoup(response.text, 'html.parser')

            """percorrer todos os livros"""
            for i in books.select('article.product_pod'):
                title = i.h3.a['title'].replace('"', '')
                titleList.append(title) #titulo

                image = urljoin(link, i.img['src']) 
                imageList.append(image) #url_imagem

                availability = i.select_one('p.instock.availability').getText(strip=True)
                availabilityList.append(availability) #disponibilidade

                price = books.select_one('p.price_color').getText(strip=True).replace('Â£', '')
                priceList.append(price) #preco

                if i.find('p', class_='star-rating One'):
                    rating = 1
                elif i.find('p', class_='star-rating Two'):
                    rating = 2
                elif i.find('p', class_='star-rating Three'):
                    rating = 3
                elif i.find('p', class_='star-rating Four'):
                    rating = 4
                elif i.find('p', class_='star-rating Five'):
                    rating = 5
                ratingList.append(rating) #avaliacao

                categoriesList.append(categoria)
            
            """validar se existem mais páginas a serem percorridas nessa categoria"""
            next_page = books.select_one('li.next a')
            if next_page:
                link = urljoin(link, next_page["href"])
            else:
                link = None

    """armazenar em um DataFrame"""
    logger.info(f'Salvando dados em um dataFrame')
    dfBooks = pd.DataFrame({'title': titleList, 'price': priceList, 'rating': ratingList, 'availability': availabilityList, 'category': categoriesList, 'image_url': imageList})

    """exportar em formato .csv"""
    logger.info(f'Exportando os dados para o diretório app/data/books.csv')
    dfBooks.to_csv('src/data/books.csv', index_label="id")
