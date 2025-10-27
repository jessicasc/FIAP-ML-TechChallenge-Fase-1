from flask import Blueprint
import pandas as pd
from src.schemas.book_schema import BookSchema
from pydantic import ValidationError
import logging

logger = logging.getLogger(__name__)

def create_books_blueprint(name, url_prefix):
    bp = Blueprint(name, __name__, url_prefix=url_prefix)
    return bp

def load_books():
    logger.info("Criando conexãoo com a fonte de dados")

    try:
        logger.info("validando dados de acordo com Schema pré definido")
        df = pd.read_csv('src/data/books.csv')
        books_data = df.to_dict(orient='records')

        books = [BookSchema(**book) for book in books_data]

    except ValidationError as e:
        logger.error("Erro na validação dos dados")
        print("Erro na validação dos dados")
        print(e)

    return df
