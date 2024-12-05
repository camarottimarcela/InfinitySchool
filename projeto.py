# Definição de Dados
tarefas = []

# Funções
def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }
    tarefas.append(tarefa)

def listar_tarefas():
    for tarefa in tarefas:
        print(f"Nome: {tarefa['nome']}, Descrição: {tarefa['descricao']}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Concluída: {tarefa['concluida']}")

def marcar_tarefa_concluida(nome):
    for tarefa in tarefas:
        if tarefa['nome'] == nome:
            tarefa['concluida'] = True
            break

def exibir_tarefas_por_prioridade(prioridade):
    for tarefa in tarefas:
        if tarefa['prioridade'] == prioridade:
            print(f"Nome: {tarefa['nome']}, Descrição: {tarefa['descricao']}, Categoria: {tarefa['categoria']}, Concluída: {tarefa['concluida']}")

def exibir_tarefas_por_categoria(categoria):
    for tarefa in tarefas:
        if tarefa['categoria'] == categoria:
            print(f"Nome: {tarefa['nome']}, Descrição: {tarefa['descricao']}, Prioridade: {tarefa['prioridade']}, Concluída: {tarefa['concluida']}")

# Menu de Comandos
def menu():
    while True:
        print("\nMenu de Comandos:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome da Tarefa: ")
            descricao = input("Descrição da Tarefa: ")
            prioridade = input("Prioridade da Tarefa: ")
            categoria = input("Categoria da Tarefa: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            nome = input("Nome da Tarefa a ser marcada como concluída: ")
            marcar_tarefa_concluida(nome)
        elif escolha == '4':
            prioridade = input("Prioridade das Tarefas a serem exibidas: ")
            exibir_tarefas_por_prioridade(prioridade)
        elif escolha == '5':
            categoria = input("Categoria das Tarefas a serem exibidas: ")
            exibir_tarefas_por_categoria(categoria)
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()