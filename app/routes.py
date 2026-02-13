from flask import Blueprint, render_template, request, jsonify
# Importa a conexão que criamos no passo anterior
from app.database import supabase, supabase_admin 

main_bp = Blueprint("main", __name__)

# --- ROTAS DE PÁGINAS (HTML) ---
@main_bp.route("/")
def home():
    # Antes estava retornando texto, agora retorna seu HTML
    return render_template("auth/login.html") 

@main_bp.route("/login")
def login():
    return render_template("auth/login.html")

# --- ROTAS DE API (DADOS DO SUPABASE) ---

# Rota de Cadastro
@main_bp.route('/auth/cadastro', methods=['POST'])
def cadastro():
    data = request.json
    try:
        response = supabase.auth.sign_up({
            "email": data.get('email'),
            "password": data.get('password'),
            "options": {
                "data": {"full_name": data.get('full_name')}
            }
        })
        return jsonify({"msg": "Criado com sucesso!", "id": response.user.id}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

# Rota de Listar Produtos
@main_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    try:
        response = supabase.table('products').select("*").execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500