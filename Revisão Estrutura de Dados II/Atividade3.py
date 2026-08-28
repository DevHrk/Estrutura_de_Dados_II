# Importa o deque, uma estrutura de dados própria para trabalhar com filas
from collections import deque

# Cria uma fila vazia para armazenar os pacientes
fila = deque()


# Função responsável por adicionar um novo paciente à fila
def adicionar_paciente():

    # Solicita o nome do paciente
    nome = input("Nome: ")

    # Solicita a idade e converte o valor digitado para inteiro
    idade = int(input("Idade: "))

    # Solicita o nível de prioridade do paciente
    prioridade = input("Nível de prioridade: ")

    # Cria um dicionário contendo os dados do paciente
    paciente = {
        "nome": nome,
        "idade": idade,
        "prioridade": prioridade
    }

    # Adiciona o paciente no final da fila
    fila.append(paciente)

    # Exibe uma mensagem confirmando que o paciente foi adicionado
    print(f"\nPaciente {nome} adicionado à fila.")


# Função responsável por atender o primeiro paciente da fila
def atender_paciente():

    # Verifica se a fila está vazia
    if len(fila) == 0:
        print("\nA fila está vazia.")

    # Caso a fila tenha pacientes
    else:
        # Remove o primeiro paciente da fila
        paciente = fila.popleft()

        # Mostra o nome do paciente que foi atendido
        print(f"\nPaciente atendido: {paciente['nome']}")


# Função responsável por listar os pacientes que estão esperando
def listar_espera():

    # Verifica se não existem pacientes na fila
    if len(fila) == 0:
        print("\nA fila está vazia.")

    # Caso existam pacientes
    else:
        # Exibe o título da lista
        print("\n--- Pacientes aguardando ---")

        # Percorre todos os pacientes da fila
        # enumerate() serve para numerar os pacientes começando pelo número 1
        for i, paciente in enumerate(fila, start=1):

            # Exibe os dados de cada paciente
            print(
                f"{i}. Nome: {paciente['nome']} | "
                f"Idade: {paciente['idade']} | "
                f"Prioridade: {paciente['prioridade']}"
            )


# Função responsável por verificar se a fila está vazia
def checar_vazia():

    # Verifica se não há nenhum paciente na fila
    if len(fila) == 0:
        print("\nA fila está vazia.")

    # Caso existam pacientes
    else:
        # Mostra a quantidade de pacientes aguardando
        print(f"\nA fila possui {len(fila)} paciente(s).")


# Laço principal do sistema
# O programa continuará funcionando até que o usuário escolha a opção 0
while True:

    # Exibe o menu principal
    print("\n===== SISTEMA DA CLÍNICA =====")
    print("1 - Adicionar paciente")
    print("2 - Atender paciente")
    print("3 - Listar espera")
    print("4 - Checar se está vazia")
    print("0 - Sair")

    # Solicita ao usuário que escolha uma opção
    opcao = input("Escolha uma opção: ")


    # Se o usuário escolher 1, chama a função para adicionar paciente
    if opcao == "1":
        adicionar_paciente()


    # Se escolher 2, chama a função para atender o primeiro paciente
    elif opcao == "2":
        atender_paciente()


    # Se escolher 3, mostra os pacientes que estão esperando
    elif opcao == "3":
        listar_espera()


    # Se escolher 4, verifica a quantidade de pacientes na fila
    elif opcao == "4":
        checar_vazia()


    # Se escolher 0, encerra o programa
    elif opcao == "0":
        print("\nSistema encerrado.")
        break


    # Caso o usuário digite uma opção que não existe
    else:
        print("\nOpção inválida.")
