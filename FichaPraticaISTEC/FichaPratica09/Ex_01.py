import json
from textwrap import indent


def imprimir_funcionario(funcionario):
    print(
        f"Nome: {funcionario["nome"]} | Idade: {funcionario["idade"]} | Cargo: {funcionario["cargo"]} | Salário: {funcionario["salario"]} €")


def consultar_dados(dados):
    for funcionario in dados:
        imprimir_funcionario(funcionario)


def adicionar_funcionario(dados, nome, idade, cargo, salario):
    # Criar um novo funcionario
    novoFuncionario = {
        "nome": nome,
        "idade": idade,
        "cargo": cargo,
        "salario": salario
    }

    if (idade < 18):
        print("Erro ao adicionar novo funcionário: Menor de 18 anos")
    else:
        # Adicionar o novo funcionario ao dicionario
        dados.append(novoFuncionario)

    # Retornar o dicionario já com as alterações
    return dados


def filtrar_salario(dados):
    for funcionario in dados:
        if (funcionario["salario"] >= 5000):
            imprimir_funcionario(funcionario)


def subir_salarios(dados):
    for funcionario in dados:
        funcionario["salario"] = funcionario["salario"] * 1.1

    return dados


def menu(dados):
    opcao = 1

    while (opcao != 0):
        print("\n***** Gestão de Funcionários *****")
        print("1. Consultar Dados")
        print("2. Filtrar por Salário (acima de 5000€)")
        print("3. Atualizar Salário")
        print("4. Novo Funcionário")
        print("0. Sair")

        opcao = int(input("\nInsira a opção: "))

        match (opcao):
            case 1:  # Consultar Dados
                consultar_dados(dados)

            case 2:  # Filtrar por Salário
                filtrar_salario(dados)

            case 3:  # Atualizar Salário
                dados = subir_salarios(dados)

            case 4:  # Novo Funcionário
                print("***** Novo Funcionário *****")
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                cargo = input("Cargo: ")
                salario = float(input("Salário: "))

                dados = adicionar_funcionario(dados, nome, idade, cargo, salario)

            case 0:  # Sair
                guardar_dados(
                    "C:/Users/vmvs0/Desktop/ISTEC/PAC I/ISTEC_Ciber_PACI_2425/FichaPraticaISTEC/Ficheiros/funcionarios.json",
                    dados)

                print("Sair do Programa...")

            case _:
                print("Opção Inválida")


def carregar_dados(caminho):
    dados = {}
    with open(caminho, 'r') as ficheiro:
        dados = json.load(ficheiro)

    return dados


def guardar_dados(caminho, dados):
    with open(caminho, 'w') as ficheiro:
        json.dump(dados, ficheiro, indent=4)


if __name__ == "__main__":
    caminhoFicheiro = "../Ficheiros/funcionarios.json"
    dados = carregar_dados(caminhoFicheiro)

    menu(dados)
