#  API de Gerenciamento de Tarefas

Projeto desenvolvido com Python utilizando FastAPI para criação de uma API REST simples com persistência em JSON.

# Funcionalidades

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Concluir tarefa
- Remover tarefa

# Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- JSON (persistência de dados)

# Estrutura do projeto

- `main.py` → rotas da API
- `models.py` → estrutura dos dados
- `storage.py` → manipulação e persistência dos dados

# ▶️ Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt

Rode a API:
python -m uvicorn main:app --reload

Acesse no navegador:
http://127.0.0.1:8000/docs