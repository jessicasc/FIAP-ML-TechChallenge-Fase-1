class Config:
    CACHE_TYPE = 'simple'
    SWAGGER = {
            'title': 'API de Livros - FIAP ML Tech Challenge 1',
            'uiversion': 3,
            'description': 'RESTful API para análise dos livros obtidos via web scrapping no site https://books.toscrape.com.'
    }
    JWT_SECRET_KEY = ''