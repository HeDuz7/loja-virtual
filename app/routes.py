from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app.database import supabase, supabase_admin 
from flask import request, render_template
from werkzeug.security import generate_password_hash

main_bp = Blueprint("main", __name__)

# --- ROTAS DE PÁGINAS (HTML) ---
@main_bp.route("/")
def home():
    # Antes estava retornando texto, agora retorna seu HTML
    return render_template("auth/login.html") 

@main_bp.route("/login")
def login():
    return render_template("auth/login.html")

@main_bp.route("/register")
def register_page():
    return render_template("auth/register.html")

@main_bp.get("/home")
def home_page():
    return render_template("home.html")
# --- ROTAS DE API (DADOS DO SUPABASE) ---

@main_bp.get("/produto/detalhe")
def produto_detalhe():
    # Tudo fixo por enquanto
    produto = {
        "nome": "Nome da Camisa",
        "temporada": "2026/2027 - Camisa 1",
        "modelo": "Modelo da Camisa",
        "descricao": (
            "Reviva a história com a camisa retrô do Manchester United, "
            "inspirada na temporada icônica de 1992-1994. Com design clássico "
            "e gola polo elegante, esta peça combina estilo e nostalgia, perfeita "
            "para os torcedores apaixonados."
        ),
        "imagem": "img/products/camisa1.jpg",
        "rating": 4
    }
    return render_template("produto/detalhe.html", produto=produto)

@main_bp.route('/cadastrar', methods=['POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('full_name')
        email = request.form.get('email')
        usuario = request.form.get('username')
        senha = request.form.get('password')
        senha_segura = generate_password_hash(senha)

        dados = {
            "full_name": nome,
            "email": email,
            "username": usuario,
            "password": senha_segura
        }

        try:
            supabase.table("users").insert(dados).execute()
            return redirect(url_for('main.login'))
            
        except Exception as erro:
            return f"Erro ao salvar: {erro}"

    return render_template('register.html')