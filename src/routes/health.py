from flask import jsonify, current_app
import os
import pandas as pd
from src.routes.blueprint_controller import create_books_blueprint

health_bp = create_books_blueprint('health', '/api/v1/health')

@health_bp.route('', methods=['GET'])
def health_check():
    """
    Avalia a 'saúde' da API.
    ---
    tags:
      - Health
    description: Avalia a conexão da API com a fonte de dados.
    consumes:
      - application/json
    responses:
      200:
        description: Status ok
        schema:
          properties:
            status:
              example: "ok"
            data_file_found:
              example: true
            data_accessible:
              example: true
      500:
        description: "Erro no acesso aos dados."
    """
    
    current_app.logger.info(f"Endpoint /health acessado - Avaliando a saúde da API")

    try:
        # Verifica se o arquivo de dados existe
        data_path = 'src/data/books.csv'
        data_exists = os.path.exists(data_path)

        # Tenta ler o CSV pra checar se está acessível
        data_accessible = False
        if data_exists:
            df = pd.read_csv(data_path)
            data_accessible = not df.empty

        status = {
            "status": "ok" if data_exists and data_accessible else "error",
            "data_file_found": data_exists,
            "data_accessible": data_accessible
        }

        current_app.logger.info(f"Endpoint /health - Status: {status}")
        return jsonify(status), 200 if status["status"] == "ok" else 500

    except Exception as e:
        current_app.logger.error(f"Endpoint /health - erro com a API: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
