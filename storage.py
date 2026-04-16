import json

tarefas = []
proximo_id = 1


def salvar():
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