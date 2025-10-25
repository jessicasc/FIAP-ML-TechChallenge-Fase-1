from flask import jsonify, current_app
import pandas as pd
from src.schemas.book_schema import BookSchema
from src.routes.blueprint_controller import create_books_blueprint, load_books

categories_bp = create_books_blueprint('categories', '/api/v1/categories')

df = load_books()

@categories_bp.route('', methods=['GET'])
def all_categories():
    """
    Listar todas as categorias.
    ---
    tags:
      - Categories
    description: Retorna todas as categorias de livros.
    consumes:
      - application/json
    responses:
      200:
        description: Lista de categorias.
        schema:
          properties:
            categories:
              example: "Travel, Mystery, Classics"
    """
    current_app.logger.info(f"Endpoint /categories acessado - Listar todas as categorias")

    return jsonify(df['category'].unique().tolist())

