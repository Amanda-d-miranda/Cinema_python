from flask import Flask, jsonify, request

app = Flask(__name__)

filmes = [
    {"id": 1, "filme": "A Culpa é das Estrelas", "diretor": "Michelle Johnston", "ano": None, "genero": "Comédia"},
    {"id": 2, "filme": "Barbie", "diretor": "Greta Gerwig", "ano": 2023, "genero": "Comédia"},
    {"id": 3, "filme": "Para Todos os Garotos que Já Amei", "diretor": "Joe Menendez", "ano": 2025, "genero": "Comédia"},
    {"id": 4, "filme": "La La Land", "diretor": "Francis Ford Coppola", "ano": 1972, "genero": "Crime"},
    {"id": 5, "filme": "Como se fosse a Primeira Vez", "diretor": "Peter Segal", "ano": 2004, "genero": "Romance"},
    {"id": 6, "filme": "Click", "diretor": "Frank Coraci", "ano": 2006, "genero": "Comédia"},
    {"id": 7, "filme": "Como eu era antes de você", "diretor": "Dolly Wells", "ano": 2016, "genero": "Romance"},
    {"id": 8, "filme": "Titanic", "diretor": "James Cameron", "ano": 1997, "genero": "Romance"},
]

personagens = [
    {"id": 1, "nome": "Hazel Grace", "filme_id": 1},
    {"id": 2, "nome": "Augustus Waters", "filme_id": 1},
    {"id": 3, "nome": "Barbie", "filme_id": 2},
    {"id": 4, "nome": "Ken", "filme_id": 2},
    {"id": 5, "nome": "Lara Jean Covey", "filme_id": 3},
    {"id": 6, "nome": "Peter Kavinsky", "filme_id": 3},
    {"id": 7, "nome": "Mia", "filme_id": 4},
    {"id": 8, "nome": "Sebastian", "filme_id": 4},
    {"id": 9, "nome": "Henry Roth", "filme_id": 5},
    {"id": 10, "nome": "Lucy Whitmore", "filme_id": 5},
    {"id": 11, "nome": "Michael Newman", "filme_id": 6},
    {"id": 12, "nome": "Louisa Clark", "filme_id": 7},
    {"id": 13, "nome": "Will Traynor", "filme_id": 7},
    {"id": 14, "nome": "Jack Dawson", "filme_id": 8},
    {"id": 15, "nome": "Rose", "filme_id": 8},
]

# ---------- FILMES ----------

# LISTAR
@app.route("/filmes", methods=["GET"])
def obter_filmes():
    return jsonify(filmes)


# CONSULTAR (por id)
@app.route("/filmes/<int:id>", methods=["GET"])
def obter_filme_id(id):
    for filme in filmes:
        if filme.get("id") == id:
            return jsonify(filme)
    return jsonify({"message": "filme não encontrado!"}), 404


# EDITAR
@app.route("/filmes/<int:id>", methods=["PUT"])
def editar_filme_por_id(id):
    filme_alterado = request.get_json()

    for indice, filme in enumerate(filmes):
        if filme.get("id") == id:
            filmes[indice].update(filme_alterado)
            return jsonify(filmes[indice])

    return jsonify({"message": "filme não encontrado!"}), 404


# CRIAR
@app.route("/filmes", methods=["POST"])
def incluir_novo_filme():
    novo_filme = request.get_json()
    filmes.append(novo_filme)
    return jsonify(filmes), 201


# EXCLUIR
@app.route("/filmes/<int:id>", methods=["DELETE"])
def excluir_filme(id):
    for indice, filme in enumerate(filmes):
        if filme.get("id") == id:
            del filmes[indice]
            return jsonify({"message": "filme excluído!"})
    return jsonify({"message": "filme não encontrado!"}), 404


# ---------- PERSONAGENS ----------

# LISTAR
@app.route("/personagens", methods=["GET"])
def obter_personagens():
    return jsonify(personagens)


# CONSULTAR (por id)
@app.route("/personagens/<int:id>", methods=["GET"])
def obter_personagem_id(id):
    for personagem in personagens:
        if personagem.get("id") == id:
            return jsonify(personagem)
    return jsonify({"message": "personagem não encontrado!"}), 404


# EDITAR
@app.route("/personagens/<int:id>", methods=["PUT"])
def editar_personagem_por_id(id):
    personagem_alterado = request.get_json()

    for indice, personagem in enumerate(personagens):
        if personagem.get("id") == id:
            personagens[indice].update(personagem_alterado)
            return jsonify(personagens[indice])

    return jsonify({"message": "personagem não encontrado!"}), 404


# CRIAR
@app.route("/personagens", methods=["POST"])
def incluir_novo_personagem():
    novo_personagem = request.get_json()
    personagens.append(novo_personagem)
    return jsonify(personagens), 201


# EXCLUIR
@app.route("/personagens/<int:id>", methods=["DELETE"])
def excluir_personagem(id):
    for indice, personagem in enumerate(personagens):
        if personagem.get("id") == id:
            del personagens[indice]
            return jsonify({"message": "personagem excluído!"})
    return jsonify({"message": "personagem não encontrado!"}), 404


# INICIALIZAÇÃO DO SERVIDOR (sempre no final)
if __name__ == "__main__":
    app.run(host="localhost", port=7500, debug=True)