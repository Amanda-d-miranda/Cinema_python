🎬 API de Filmes e Personagens

API REST em Flask para gerenciar filmes e personagens, com CRUD completo. O projeto também já está preparado para evoluir para um banco PostgreSQL usando Flask-SQLAlchemy e Flask-Migrate.

📑 Índice
Sobre o projeto
Funcionalidades
Tecnologias
Estrutura do projeto
Pré-requisitos
Instalação passo a passo
Configuração do ambiente (.env)
Como executar
Documentação da API
Testando com cURL, Postman e Python
Banco de dados e migrations
Roadmap
Problemas comuns
Contribuindo
Licença
📖 Sobre o projeto

Este projeto é uma API para cadastrar, consultar, editar e excluir filmes e seus personagens.

Ele está dividido em duas partes:

Parte	Arquivo	Situação
🟢 API funcional (dados em memória)	teste.py	Pronta para uso e testes
🟡 Base para integração com PostgreSQL	app.py, db.py, migrations.py	Configuração inicial feita, modelos em construção

💡 Resumindo: hoje você já consegue rodar a API completa com teste.py. Os dados ficam na memória (reiniciou o servidor, voltou ao estado inicial). A migração para o banco de dados real é o próximo passo.

✨ Funcionalidades
✅ Listar todos os filmes
✅ Consultar filme por ID
✅ Cadastrar novo filme
✅ Editar filme (atualização parcial)
✅ Excluir filme
✅ Listar todos os personagens
✅ Consultar personagem por ID
✅ Cadastrar novo personagem
✅ Editar personagem
✅ Excluir personagem
🔜 Persistência em PostgreSQL
🔜 Migrations com Flask-Migrate / Alembic
🛠 Tecnologias
Tecnologia	Para que serve
Python	Linguagem principal
Flask	Framework web / API REST
Flask-SQLAlchemy	ORM para integrar o Flask ao banco
Flask-Migrate	Controle de versões do banco (Alembic)
PostgreSQL	Banco de dados relacional
psycopg2	Driver de conexão com o PostgreSQL
python-dotenv	Leitura de variáveis do arquivo .env
📂 Estrutura do projeto
.
├── app.py              # Configuração do Flask + conexão com PostgreSQL
├── db.py               # Instância do SQLAlchemy (e futuros modelos)
├── migrations.py       # Configuração das migrations
├── teste.py            # API REST funcional com dados em memória
├── requirements.txt    # Dependências do projeto
├── .env                # Variáveis de ambiente (NÃO vai para o Git)
└── .gitignore          # Arquivos ignorados pelo Git
📋 Pré-requisitos

Antes de começar, tenha instalado:

 Python 3.11 ou superior → python --version
 pip → pip --version
 Git → git --version
 PostgreSQL (só necessário para a parte do banco de dados)
🚀 Instalação passo a passo
1️⃣ Clone o repositório
bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
2️⃣ Crie e ative um ambiente virtual
<details> <summary>🐧 Linux / macOS</summary>
bash
python3 -m venv venv
source venv/bin/activate
</details> <details> <summary>🪟 Windows (PowerShell)</summary>
powershell
python -m venv venv
venv\Scripts\Activate.ps1
</details> <details> <summary>🪟 Windows (CMD)</summary>
cmd
python -m venv venv
venv\Scripts\activate.bat
</details>
3️⃣ Instale as dependências
bash
pip install -r requirements.txt
🔐 Configuração do ambiente (.env)

Crie um arquivo chamado .env na raiz do projeto:

env
# Exemplo de configuração
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/books

⚠️ O arquivo .env já está no .gitignore. Nunca envie senhas ou credenciais para o repositório.

💡 Dica: atualmente a URL do banco está fixa em app.py. Uma boa melhoria é lê-la do .env:

python
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
▶️ Como executar
Rodar a API (dados em memória)
bash
python teste.py

O servidor sobe em: http://localhost:7500

Abra no navegador para testar rapidamente:

👉 http://localhost:7500/filmes 👉 http://localhost:7500/personagens

📡 Documentação da API

Base URL: http://localhost:7500

🎞️ Filmes
Método	Rota	Descrição	Sucesso	Erro
GET	/filmes	Lista todos os filmes	200	—
GET	/filmes/<id>	Busca um filme por ID	200	404
POST	/filmes	Cadastra um novo filme	201	—
PUT	/filmes/<id>	Edita um filme existente	200	404
DELETE	/filmes/<id>	Exclui um filme	200	404

Modelo de filme:

json
{
  "id": 8,
  "filme": "Titanic",
  "diretor": "James Cameron",
  "ano": 1997,
  "genero": "Romance"
}
🧑‍🎤 Personagens
Método	Rota	Descrição	Sucesso	Erro
GET	/personagens	Lista todos os personagens	200	—
GET	/personagens/<id>	Busca um personagem por ID	200	404
POST	/personagens	Cadastra um novo personagem	201	—
PUT	/personagens/<id>	Edita um personagem existente	200	404
DELETE	/personagens/<id>	Exclui um personagem	200	404

Modelo de personagem:

json
{
  "id": 14,
  "nome": "Jack Dawson",
  "filme_id": 8
}

🔗 O campo filme_id relaciona o personagem ao filme correspondente.

📬 Exemplos de resposta
<details> <summary>✅ <code>GET /filmes/8</code> → 200 OK</summary>
json
{
  "id": 8,
  "filme": "Titanic",
  "diretor": "James Cameron",
  "ano": 1997,
  "genero": "Romance"
}
</details> <details> <summary>❌ <code>GET /filmes/999</code> → 404 Not Found</summary>
json
{
  "message": "filme não encontrado!"
}
</details> <details> <summary>✅ <code>DELETE /personagens/15</code> → 200 OK</summary>
json
{
  "message": "personagem excluído!"
}
</details>
🧪 Testando a API
Com cURL
bash
# Listar filmes
curl http://localhost:7500/filmes

# Buscar filme por ID
curl http://localhost:7500/filmes/2

# Criar filme
curl -X POST http://localhost:7500/filmes \
  -H "Content-Type: application/json" \
  -d '{"id": 9, "filme": "Interestelar", "diretor": "Christopher Nolan", "ano": 2014, "genero": "Ficção"}'

# Editar filme (apenas os campos enviados são alterados)
curl -X PUT http://localhost:7500/filmes/1 \
  -H "Content-Type: application/json" \
  -d '{"ano": 2014}'

# Excluir filme
curl -X DELETE http://localhost:7500/filmes/9
bash
# Criar personagem
curl -X POST http://localhost:7500/personagens \
  -H "Content-Type: application/json" \
  -d '{"id": 16, "nome": "Cooper", "filme_id": 9}'
Com Python (requests)
python
import requests

BASE = "http://localhost:7500"

# Listar
print(requests.get(f"{BASE}/filmes").json())

# Criar
novo = {"id": 9, "filme": "Interestelar", "diretor": "Christopher Nolan", "ano": 2014, "genero": "Ficção"}
r = requests.post(f"{BASE}/filmes", json=novo)
print(r.status_code)  # 201
Com Postman / Insomnia / Thunder Client
Crie uma nova requisição com o método desejado
Use a URL http://localhost:7500/filmes
Em requisições POST e PUT, vá em Body → raw → JSON
Envie o JSON no formato dos modelos acima
🗄 Banco de dados e migrations

A conexão com o PostgreSQL já está configurada em app.py:

python
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://postgres:postgres@localhost:5432/books"
)
1. Crie o banco
sql
CREATE DATABASE books;

Ou, pelo terminal:

bash
psql -U postgres -c "CREATE DATABASE books;"
2. Exemplo de modelos (em db.py)
python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Filme(db.Model):
    __tablename__ = "filmes"

    id = db.Column(db.Integer, primary_key=True)
    filme = db.Column(db.String(150), nullable=False)
    diretor = db.Column(db.String(100))
    ano = db.Column(db.Integer)
    genero = db.Column(db.String(50))

    personagens = db.relationship("Personagem", backref="filme", cascade="all, delete")

class Personagem(db.Model):
    __tablename__ = "personagens"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    filme_id = db.Column(db.Integer, db.ForeignKey("filmes.id"), nullable=False)
3. Inicialize o Flask-Migrate (em app.py)
python
from flask_migrate import Migrate

db.init_app(app)
migrate = Migrate(app, db)
4. Rode as migrations
bash
flask --app app db init        # só na primeira vez
flask --app app db migrate -m "criar tabelas filmes e personagens"
flask --app app db upgrade
🗺 Roadmap
 CRUD de filmes em memória
 CRUD de personagens em memória
 Configuração inicial do Flask + SQLAlchemy + PostgreSQL
 Criar modelos Filme e Personagem no db.py
 Configurar Flask-Migrate e gerar a primeira migration
 Migrar as rotas para usar o banco de dados
 Ler a URL do banco a partir do .env
 Validação dos dados de entrada (campos obrigatórios e tipos)
 Gerar ID automaticamente no POST
 Rota para listar personagens de um filme (/filmes/<id>/personagens)
 Documentação interativa com Swagger/OpenAPI
 Testes automatizados com pytest
 Dockerização (Dockerfile + docker-compose com PostgreSQL)
🩺 Problemas comuns
<details> <summary><b>❓ <code>ModuleNotFoundError: No module named 'flask'</code></b></summary>

O ambiente virtual não está ativo ou as dependências não foram instaladas.

bash
source venv/bin/activate   # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
</details> <details> <summary><b>❓ <code>connection refused</code> ao conectar no PostgreSQL</b></summary>
Verifique se o PostgreSQL está rodando
Confirme usuário, senha, porta (5432) e nome do banco (books)
Teste a conexão: psql -U postgres -h localhost -d books
</details> <details> <summary><b>❓ <code>Address already in use</code> na porta 7500</b></summary>

Outro processo está usando a porta. Encerre-o ou altere a porta em teste.py:

python
app.run(host="localhost", port=7501, debug=True)
</details> <details> <summary><b>❓ <code>415 Unsupported Media Type</code> no POST/PUT</b></summary>

Falta o cabeçalho Content-Type: application/json na requisição.

</details> <details> <summary><b>❓ Os dados sumiram após reiniciar o servidor</b></summary>

É o comportamento esperado: o teste.py guarda os dados em listas na memória. Para persistir, conclua a integração com o PostgreSQL (veja o Roadmap).

</details>
🤝 Contribuindo
Faça um fork do projeto
Crie uma branch: git checkout -b feature/minha-feature
Commit suas mudanças: git commit -m "feat: minha feature"
Envie para o GitHub: git push origin feature/minha-feature
Abra um Pull Request 🎉
📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, estudar e modificar.

<p align="center">Feito com ❤️ e Flask 🐍</p>
