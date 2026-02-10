from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.get("/")
def home():
    return "OK - app rodando"

@main_bp.get("/login")
def login():
    return render_template("auth/login.html")
