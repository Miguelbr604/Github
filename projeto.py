import json 
usuario_logado = None



def carregar_dados():
        try:
            with open("projeto.py", "r", encoding = "utf-8") as arquivo:
                  dados = json.load(arquivo)

            if "usuarios" not in dados:
                  raise ValueError
            return dados
        
        except:
              return{"usuarios": []}
        
def salvar_dados(dados):
      with open("projeto.py", "w", encoding = "utf-8") as arquivo:
            json.dump(dados, arquivo, indent= 4, ensure_ascii = False)


def buscar_usuario_por_nome(dados, nome):
        for u in dados["usuarios"]:
              if u ["nome"] == nome:
                    return u
def criar_usuario(dados, nome, senha):
      if buscar_usuario_por_nome(dados, nome):
            print("usuario ja existe")
            return
      novo_id = max([u["id"] for u in dados["usuarios"]], default = 0) +1
      dados["usuarios"].append({
            "id" : novo_id,
            "nome" : nome,
            "senha":senha,
            "ativo" : True,
            "projetos" : []

      })

def login(dados, nome, senha):
      global usuario_logado
      usuario = buscar_usuario_por_nome(dados, nome)

      if not usuario or usuario ["senha"] != senha:
            print("login invalido")
            return False
      
def logout():
      global usuario_logado
      usuario_logado = None


def criar_projeto(dados, nome_projeto):
    if not usuario_logado:
            print("faça login")
            return
      
    novo_id = max([p["id"]for p in usuario_logado["projetos"]], default = 100) + 1

    usuario_logado["projetos"].append({
          "id" : novo_id,
          "nome" : nome_projeto,
          "status" : "ativo", 
          "tarefas" : []


    })


def menu():
      dados = carregar_dados()

      while True:
            print("\n1 - criar usuario")
            print("2- login")
            print("3- criar projeto")
            print("4- Logout")
            print("0- sair")

            op = input("escolha: ")

            if op == "1":
                  nome = input("nome:")
                  senha = input("senha")
                  criar_usuario(dados, nome, senha)

            elif op == "2":
                  nome = input("nome:")
                  senha = input("senha:")
                  login(dados, nome, senha)

            elif op == "3":
                  nome = input("nome do projeto")
                  criar_projeto(dados, nome)

            elif op == "4":
                  logout()
            
            elif op == "0":
                salvar_dados(dados)
                break


if __name__ == "__main__":
      menu()
            


        
