from flask import Flask, render_template
import json
import os
from datetime import datetime

app = Flask(__name__) 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/curriculo")
def curriculo():
    # Formação acadêmica
    with open("docportifolio/formacao.json", "r", encoding="utf-8") as f:
        formacoes = json.load(f)

    # Cursos
    with open("docportifolio/cursos.json", "r", encoding="utf-8") as f:
        cursos = json.load(f)

    # Experiência profissional
    with open("docportifolio/experiencia.json", "r", encoding="utf-8") as f:
        experiencias = json.load(f)

    # Ordenar experiências pelo inicio
    experiencias_sorted = sorted(
        experiencias,
        key=lambda x: datetime.strptime(x["inicio"], "%Y-%m")
    )

    # Adicionar valor vertical (posição na linha) e converter data para ISO
    for idx, exp in enumerate(experiencias_sorted, 1):
        exp["valor_vertical"] = idx
        exp["inicio_iso"] = exp["inicio"] + "-01"  # YYYY-MM-DD para Chart.js

    return render_template(
        "curriculo.html",
        formacoes=formacoes,
        cursos=cursos,
        experiencias=experiencias_sorted
    )



@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

@app.route("/habilidades")
def habilidades():
    return render_template("habilidades.html")

'''
if __name__ == "__main__":
    app.run(debug=True)
'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

