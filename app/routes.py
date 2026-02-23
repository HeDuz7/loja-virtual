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

# --- ROTAS DE API (DADOS DO SUPABASE) ---

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