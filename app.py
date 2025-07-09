from flask import Flask, render_template, request
import pyodbc
import os

app = Flask(__name__)

# Usa variável de ambiente definida no App Service
conn_str = os.environ.get("DATABASE_URL")
conn = pyodbc.connect(conn_str)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        disciplina = request.form["disciplina"]
        
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO alunos (nome, email, disciplina) VALUES (?, ?, ?)",
            nome, email, disciplina
        )
        conn.commit()
        return render_template("confirmacao.html", nome=nome)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
