import json
import os

ARQUIVO_JSON = "dados.json"

# Criar arquivo JSON se não existir
def criar_arquivo():
    if not os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump({"usuarios": []}, f, indent=4, ensure_ascii=False)

# Ler dados do JSON
def ler_dados():
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

# Salvar dados no JSON
def salvar_dados(dados):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Adicionar um usuário
def adicionar_usuario(nome, email):
    dados = ler_dados()
    novo_usuario = {
        "id": len(dados["usuarios"]) + 1,
        "nome": nome,
        "email": email,
        "ativo": True
    }
    dados["usuarios"].append(novo_usuario)
    salvar_dados(dados)

# Listar usuários
def listar_usuarios():
    dados = ler_dados()
    for u in dados["usuarios"]:
        status = "Ativo" if u["ativo"] else "Inativo"
        print(f"{u['id']} - {u['nome']} ({u['email']}) [{status}]")

# Programa principal
def menu():
    criar_arquivo()

    while True:
        print("\n1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            adicionar_usuario(nome, email)
            print("Usuário adicionado com sucesso!")

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

menu()