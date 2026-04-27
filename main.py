from fastapi import FastAPI
from pydantic import BaseModel
import json

class Tarefa(BaseModel):
    nome: str

app = FastAPI(
    title="API de Tarefas",
    description="API simples para gerenciamento de tarefas",
    version="1.0.0"
)

tarefas = []
proximo_id = 1


def salvar():
    print("SALVANDO...")
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)


def carregar():
    global tarefas, proximo_id

    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)

            if tarefas:
                proximo_id = max(t["id"] for t in tarefas) + 1

    except FileNotFoundError:
        tarefas = []
        proximo_id = 1


carregar()


@app.get("/")
def inicio():
    return {
        "status": "ok",
        "mensagem": "API funcionando"
    }


@app.post("/tarefas")
def adicionar_tarefa(tarefa: Tarefa):
    global proximo_id

    nova_tarefa = {
        "id": proximo_id,
        "nome": tarefa.nome,
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    proximo_id += 1
    salvar()

    return nova_tarefa


@app.get("/tarefas")
def listar_tarefas():
    return {
        "total": len(tarefas),
        "tarefas": tarefas,
    }

@app.put("/tarefas/{id}")
def editar_tarefa(id: int, dados: Tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["nome"] = dados.nome
            
            salvar()
            
            return {
                "mensagem": "Tarefa atualizada!",
                "tarefa": tarefa
            }
            
    return {"erro": "Tarefa não encontrada"}     


@app.delete("/tarefas/{id}")
def remover_tarefa(id: int):
    for indice, tarefa in enumerate(tarefas):
        if tarefa["id"] == id:
            tarefa_removida = tarefas.pop(indice)
            salvar()

            return {
                "mensagem": "Tarefa removida",
                "tarefa": tarefa_removida
            }

    return {"erro": "Tarefa não encontrada"}


@app.get("/tarefas/{id}")
def buscar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return tarefa

    return {"erro": "Tarefa não encontrada"}


