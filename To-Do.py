import json

tarefas = []

def carregar():
    global tarefas
    try:
        with open("tarefas.json", "r") as f:
            tarefas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tarefas = []

def salvar():
    with open("tarefas.json", 'w') as f:
        json.dump(tarefas, f)



def adicionar():
    tarefa = input("Digite a tarefa: ")
    prioridade = input("Digite a prioridade (Alta/Media/Baixa): ")
    if prioridade.lower() not in ["alta", "media", "baixa"]:
        print("Prioridade invalida! Use Alta, Media ou Baixa.")
        return
    
    if tarefa.strip() == "":
        print("Tarefa não pode ser vazia!")
        return
    
    tarefas.append([tarefa, False, prioridade.capitalize()])
    salvar()
    print("Tarefa adicionada com sucesso!")


def listar():
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
        return
    mapa = {
    "Alta": "🔴",
    "Media": "🟡",
    "Baixa": "🟢"
}
    
    for i, t in enumerate(tarefas):
        status = "✔" if t[1] else "✘"
        prioridade = t[2] if len(t) > 2 else "Media"
        print(f"{i + 1} - {t[0]} [{status}] - {mapa.get(prioridade, '⚪')} {prioridade}")


def concluir():
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
        return
    listar()
    try:
        i = int(input("Digite o numero da tarefa a concluir: "))
        if 0 < i <= len(tarefas):
            tarefas[i - 1][1] = True
            salvar()
            print("Tarefa concluida com sucesso!")
        else:
            print("Numero invalido!")
    except ValueError:
        print("Valor invalido, digite apenas numeros.")


def remover():
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
        return
    listar()
    try:
        i = int(input("Digite o numero da tarefa a remover: "))
        if 0 < i <= len(tarefas):
            tarefas.pop(i - 1)
            salvar()
            print("Tarefa removida com sucesso!")
        else:
            print("Numero invalido!")
    except ValueError:
        print("Valor invalido, digite apenas numeros.")

def editar():
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
        return
    listar()
    try:
        i = int(input("Digite o numero da tarefa a editar: "))
        if 0 < i <= len(tarefas):
            nova_tarefa = input("Digite a nova tarefa: ")
            if nova_tarefa.strip() == "":
                print("Tarefa não pode ser vazia!")
                return
            tarefas[i - 1][0] = nova_tarefa
            salvar()
            print("Tarefa editada com sucesso!")
        else:
            print("Numero invalido!")
    except ValueError:
        print("Valor invalido, digite apenas numeros.")




def menu():
    print("\nMENU")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Editar tarefa")
    print("6 - Sair")


carregar()

while True:
    menu()

    op = input("Escolha: ")

    if op == "1":
        adicionar()

    elif op == "2":
        listar()
    
    elif op == "3":
        concluir()
    
    elif op == "4":
        remover()
    
    elif op == "5":
        editar()
    
    elif op == "6":
        break