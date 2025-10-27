from flask import Blueprint, jsonify
from src.services import scraper 
import threading
import logging

logger = logging.getLogger(__name__)

scraper_bp = Blueprint('scraping', __name__, url_prefix='/api/v1/scraping')

def background_scraper():
    """Função que executa o scraper em segundo plano"""
    try:
        scraper.run_scraper()  
        logger.info("Endpoint /scraping/trigger - Scraper finalizado com sucesso")
    except Exception as e:
        logger.error(f"Endpoint /scraping/trigger - Erro ao executar scaper {e}")

@scraper_bp.route('/trigger', methods=['POST'])
def run_scraper():
    """
    Executar web scrapping no site https://books.toscrape.com.
    ---
    tags:
      - Trigger
    description: Executar script que realiza o web scrapping no site https://books.toscrape.com e retorna um .csv contendo os dados encontrados.
    consumes:
      - application/json
    responses:
      200:
        description: Execução do web scrapping.
        schema:
          properties:
            message:
              example: "Scraper executado com sucesso!"
      500:
        description: Erro na execução do scraper.
        schema:
          properties:
            message:
              example: "Erro na execução do scraper"
    """
    
    logger.info(f"Endpoint /scraping/trigger acessado - Iniciando execucao do scraper em segundo plano")

    thread = threading.Thread(target=background_scraper)
    thread.start()

    return jsonify({"message": "Scraper iniciado em segundo plano"}), 202

    


