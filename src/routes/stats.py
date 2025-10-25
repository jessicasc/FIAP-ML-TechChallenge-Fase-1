from flask import jsonify, current_app
import pandas as pd
from src.schemas.book_schema import BookSchema
from src.routes.blueprint_controller import create_books_blueprint, load_books

stats_bp = create_books_blueprint('stats', '/api/v1/stats')

df = load_books()

@stats_bp.route('/overview', methods=['GET'])
def stats_overview():
    """
    Estatísticas gerais dos livros.
    ---
    tags:
      - Stats
    description: Retorna quantidade total de livros, preço médio e a distribuição por rating.
    consumes:
      - application/json
    responses:
      200:
        description: Estatísticas gerais.
        schema:
          properties:
            total_books:
              example: 80
            average_price:
              example: 50
            rating_distribution:
              example: "5: 10, 4: 20, 3: 10, 2: 15, 1: 15"
    """
    current_app.logger.info(f"Endpoint /stats/overview acessado - Retornando estatísticas gerais dos livros")

    overview = {
        "total_books": len(df),
        "average_price": round(df['price'].mean(), 2),
        "rating_distribution": df['rating'].value_counts().sort_index().to_dict()
    }
    return jsonify(overview)
    
@stats_bp.route('/categories', methods=['GET'])
def stats_categories():
    """
    Estatísticas gerais por categoria.
    ---
    tags:
      - Stats
    description: Retorna quantidade total de livros e preço médio por categoria.
    consumes:
      - application/json
    responses:
      200:
        description: Estatísticas gerais por categoria.
        schema:
          properties:
            categories:
              example: "Travel"
            average_price:
              example: 50
            total_books:
              example: 10
    """

    current_app.logger.info(f"Endpoint /stats/categories acessado - Retornando estatísticas gerais por categoria")

    grouped = df.groupby('category')
    overview_by_category = {}

    for category, group in grouped:
        overview_by_category[category] = {
            "total_books": len(group),
            "average_price": round(group['price'].mean(), 2),
        }
    return overview_by_category
