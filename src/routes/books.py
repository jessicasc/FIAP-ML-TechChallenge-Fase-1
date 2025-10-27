from flask import jsonify, request, current_app
import pandas as pd
from src.schemas.book_schema import BookSchema
from src.services.blueprint_controller import create_books_blueprint, load_books

books_bp = create_books_blueprint('books', '/api/v1/books')

df = load_books()

@books_bp.route('', methods=['GET'])
def all_books():
    """
    Listar todos os livros.
    ---
    tags:
      - Books
    description: Retorna todos os livros e suas informações.
    consumes:
      - application/json
    responses:
      200:
        description: Lista de livros.
        schema:
          properties:
            id:
              example: 0
            title:
              example: "It's Only the Himalayas"
            price:
              example: 45.17
            rating:
              example: 2
            availability:
              example: "In stock"
            category:
              example: "Travel"
            image_url:
              example: "https://books.toscrape.com/media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg"
    """

    current_app.logger.info("Endpoint /books acessado - Listar todos os livros.")

    return jsonify(df.to_dict(orient='records'))

@books_bp.route('<int:id>', methods=['GET'])
def book_by_id(id):
    """
    Buscar livro por ID.
    ---
    tags:
      - Books
    description: Retorna todas as informações do livro com o ID pesquisado.
    consumes:
      - application/json
    parameters:
      - in: body
        name: id
        required: true
        description: ID do livro a ser pesquisado
        schema:
          properties:
            id:
              example: 0
    responses:
      200:
        description: Detalhes do livro
        schema:
          properties:
            id:
              example: 0
            title:
              example: "It's Only the Himalayas"
            price:
              example: 45.17
            rating:
              example: 2
            availability:
              example: "In stock"
            category:
              example: "Travel"
            image_url:
              example: "https://books.toscrape.com/media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg"
      404:
        description: 'Livro não encontrado.'
    """
    current_app.logger.info(f"Endpoint /books acessado - Buscando livros pelo ID: {id}")
    
    if 0 <= id < len(df):
        current_app.logger.info("Endpoint /books - Livro encontrado com sucesso")
        return jsonify(df.iloc[id].to_dict())
    else:
        current_app.logger.error("Endpoint /books - Livro nao encontrado")
        return jsonify({'error': 'Livro nao encontrado.'}), 404

@books_bp.route('/search', methods=['GET'])
def book_by_title_and_category():
    """
    Buscar livro por título e/ou categoria.
    ---
    tags:
      - Books
    description: Retorna todas as informações do livro com o título e/ou categoria pesquisado.
    consumes:
      - application/json
    parameters:
      - in: body
        name: title
        required: true
        description: Título do livro a ser pesquisado
        schema:
          properties:
            title:
              example: "It's Only the Himalayas"
      - in: body
        name: category
        required: true
        description: Categoria do livro a ser pesquisado
        schema:
          properties:
            category:
              example: "Travel"
    responses:
      200:
        description: Detalhes do livro
        schema:
          properties:
            id:
              example: 0
            title:
              example: "It's Only the Himalayas"
            price:
              example: 45.17
            rating:
              example: 2
            availability:
              example: "In stock"
            category:
              example: "Travel"
            image_url:
              example: "https://books.toscrape.com/media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg"
      400:
        description: 'Você deve fornecer ao menos um parâmetro: title ou category.'
      404:
        description: 'Livro não encontrado.'
    """
    title = request.args.get('title')
    category = request.args.get('category')

    if not title and not category:
        current_app.logger.error(f"Endpoint /books/search - Erro ao fornecer parametros.")
        return jsonify({'error': 'Voce deve fornecer ao menos um parametro: title ou category'}), 400

    current_app.logger.info(f"Endpoint /books/search acessado - Buscando livros pelo titulo: '{title}' e/ou pela categoria: '{category}'")

    if title and not category:
        book_found = df.loc[df['title'].str.lower() == title.lower()]
    elif category and not title:
        book_found = df.loc[df['category'].str.lower() == category.lower()]
    else:
        book_found = df.loc[(df['title'].str.lower() == title.lower()) | (df['category'].str.lower() == category.lower())]

    if not book_found.empty:
        current_app.logger.info(f"Endpoint /books/search - Livro encontrado com sucesso")
        return jsonify(book_found.to_dict(orient='records'))
    else:
        current_app.logger.error(f"Endpoint /books/search - Livro nao encontrado")
        return jsonify({'error': 'Livro nao encontrado'}), 404

@books_bp.route('/top-rated', methods=['GET'])
def top_rated_books():
    """
    Buscar os livros mais bem avaliados.
    ---
    tags:
      - Books
    description: Retorna todas as informações dos livros com o maior rating da base de dados.
    consumes:
      - application/json
    responses:
      200:
        description: Detalhes do livro
        schema:
          properties:
            id:
              example: 10
            title:
              example: "1,000 Places to See Before You Die"
            price:
              example: 45.17
            rating:
              example: 5
            availability:
              example: "In stock"
            category:
              example: "Travel"
            image_url:
              example: "https://books.toscrape.com/media/cache/d7/0f/d70f7edd92705c45a82118c3ff6c299d.jpg"
      404:
        description: 'Livro não encontrado.'
    """
    current_app.logger.info(f"Endpoint /books/top-rated acessado - Buscando livros com maior rating")

    top_rating = df['rating'].max()

    book_found = df.loc[(df['rating'] == top_rating)]

    if not book_found.empty:
        current_app.logger.info('Endpoint /books/top-rated - Livros encontrados com sucesso')
        return jsonify(book_found.to_dict(orient='records'))
    else:
        current_app.logger.error('Endpoint /books/top-rated - Livros nao encontrado')
        return jsonify({'error': 'Livro nao encontrado'}), 404

@books_bp.route('/price-range', methods=['GET'])
def book_by_price_range():
    """
    Filtrar livros dentro de uma faixa de preços.
    ---
    tags:
      - Books
    description: Retorna todas as informações dos livros dentro da faixa de preços especificada.
    consumes:
      - application/json
    parameters:
      - in: body
        name: min
        required: true
        description: Preço mínimo
        schema:
          properties:
            min:
              example: 40
      - in: body
        name: max
        required: true
        description: Preço máximo
        schema:
          properties:
            max:
              example: 50
    responses:
      200:
        description: Detalhes do livro
        schema:
          properties:
            id:
              example: 0
            title:
              example: "It's Only the Himalayas"
            price:
              example: 45.17
            rating:
              example: 2
            availability:
              example: "In stock"
            category:
              example: "Travel"
            image_url:
              example: "https://books.toscrape.com/media/cache/27/a5/27a53d0bb95bdd88288eaf66c9230d7e.jpg"
      400:
        description: 'Você deve fornecer os parâmetros necessários: min e max.'
      404:
        description: 'Livro não encontrado.'
    """

    try:
        min_price = float(request.args.get('min'))
        max_price = float(request.args.get('max'))
    except (TypeError, ValueError):
        current_app.logger.error(f"Endpoint /books/price-range - Erro ao fornecer parametros.")
        return jsonify({'error': 'Voce deve fornecer os parametros necessarios: min e max.'}), 400

    current_app.logger.info(f"Endpoint /books/price-range acessado - Buscando livros na faixa de preco de: {min_price} a {max_price}")

    book_found = df.loc[(df['price'] >= min_price) & (df['price'] <= max_price)]

    if not book_found.empty:
        current_app.logger.info('Endpoint /books/price-range - Livro encontrado com sucesso')
        return jsonify(book_found.to_dict(orient='records'))
    else:
        current_app.logger.error('Endpoint /books/price-range - Livro nao encontrado')
        return jsonify({'error': 'Livro nao encontrado'}), 404
