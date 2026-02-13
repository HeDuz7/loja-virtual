from flask import Flask
from app.routes import main_bp # 1. Importa as rotas do arquivo routes.py

app = Flask(__name__)

# 2. Registra o Blueprint (Liga o arquivo routes ao app principal)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(debug=True)