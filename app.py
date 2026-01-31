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
    with open("docportifolio/formacao.json", "r", encoding="utf-8") as f:
        formacoes = json.load(f)
    with open("docportifolio/cursos.json", "r", encoding="utf-8") as f:
        cursos = json.load(f)
    with open("docportifolio/experiencia.json", "r", encoding="utf-8") as f:
        experiencias = json.load(f)
    experiencias_sorted = sorted(
        experiencias,
        key=lambda x: datetime.strptime(x["inicio"], "%Y-%m")
    )
    for idx, exp in enumerate(experiencias_sorted, 1):
        exp["valor_vertical"] = idx
        exp["inicio_iso"] = exp["inicio"] + "-01"
    return render_template(
        "curriculo.html",
        formacoes=formacoes,
        cursos=cursos,
        experiencias=experiencias_sorted
    )

@app.route("/projetos")
def projetos():
    caminho_json = os.path.join("docportifolio", "projetos.json")
    with open(caminho_json, encoding="utf-8") as f:
        projects = json.load(f)
    return render_template("projetos.html", projects=projects)

@app.route("/habilidades")
def habilidades():
    caminho_json_hard = os.path.join(
        app.root_path,
        "docportifolio",
        "habilidadeshardskill.json"
    )
    caminho_json_soft = os.path.join(
    app.root_path,
    "docportifolio",
    "habilidadessoftskill.json"
)
    with open(caminho_json_hard, "r", encoding="utf-8") as f:
        hard_skills = json.load(f)
    with open(caminho_json_soft, "r", encoding="utf-8") as f:
        soft_skills = json.load(f)

    return render_template(
        "habilidades.html",
        hard_skills=hard_skills,
        soft_skills=soft_skills
    )

'''
if __name__ == "__main__":
    app.run(debug=True)
'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

