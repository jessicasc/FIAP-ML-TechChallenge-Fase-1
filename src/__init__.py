from flask import Flask
from flasgger import Swagger
from src.routes.books import books_bp
from src.routes.categories import categories_bp
from src.routes.health import health_bp
from src.routes.stats import stats_bp
from src.routes.scrapping import scraper_bp
from src.config.config import Config
import logging

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    Swagger(app)

    app.register_blueprint(books_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(stats_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(scraper_bp)

    handler = logging.StreamHandler()  
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    app.logger.info('Aplicação Flask iniciada')

    return app

