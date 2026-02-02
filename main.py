from flask import Flask

app = Flask(__name__)

# Rotas
@app.route("/")
def homepage():
    return "Meu site no Flask"

if __name__ == "__main__":
    app.run()