from collections import deque

fila = deque()


def adicionar_paciente():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    prioridade = input("Nível de prioridade: ")

    paciente = {
        "nome": nome,
        "idade": idade,
        "prioridade": prioridade
    }

    fila.append(paciente)
    print(f"\nPaciente {nome} adicionado à fila.")


def atender_paciente():
    if len(fila) == 0:
        print("\nA fila está vazia.")
    else:
        paciente = fila.popleft()
        print(f"\nPaciente atendido: {paciente['nome']}")


def listar_espera():
    if len(fila) == 0:
        print("\nA fila está vazia.")
    else:
        print("\n--- Pacientes aguardando ---")

        for i, paciente in enumerate(fila, start=1):
            print(
                f"{i}. Nome: {paciente['nome']} | "
                f"Idade: {paciente['idade']} | "
                f"Prioridade: {paciente['prioridade']}"
            )


def checar_vazia():
    if len(fila) == 0:
        print("\nA fila está vazia.")
    else:
        print(f"\nA fila possui {len(fila)} paciente(s).")


while True:
    print("\n===== SISTEMA DA CLÍNICA =====")
    print("1 - Adicionar paciente")
    print("2 - Atender paciente")
    print("3 - Listar espera")
    print("4 - Checar se está vazia")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_paciente()

    elif opcao == "2":
        atender_paciente()

    elif opcao == "3":
        listar_espera()

    elif opcao == "4":
        checar_vazia()

    elif opcao == "0":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")
