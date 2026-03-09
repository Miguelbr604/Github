{
  "usuarios": [
    {
      "id": 1,
      "nome": "Miguel",
      "ativo": True,
      "projetos": []
    }
  ]
}


import json

def carregar_dados():
    try: 
        with open("sistema.json", "r", encoding= "utf-8") as arquivo:
            dados = json.load(arquivo)
        print("DEBUG - Dados carregados:")
        print(dados)
        print("Tipo de usuarios:", type(dados.get("usuarios")))

        if "usuarios" not in dados or not isinstance(dados["usuarios"], list):
            raise ValueError("Estrutura invalida")
        return dados
    except Exception as e:
        print("ERRO:", e)
        return {"usuarios": []}
    
    
    
def buscar_usuario(dados, nome):
    usuario_id = buscar_usuario(dados, usuario_id)
    novo_id = max([u["id"] for u in dados["usuarios"]], default=0) + 1

    dados["usuarios"].append({
        "id": novo_id,
        "nome": nome,
        "ativo": True,
        "projetos": []
    })
    
    


def adicionar_projeto(dados, usuario_id, nome_projeto):
    usuario = buscar_usuario(dados, usuario_id)

    if not usuario:
        print("infelizmente, usuario nao foi encontrado")
        return
    if not usuario["ativo"]:
        print("usuario inativo")
        return
    
    novo_id = max([p["id"] for p in usuario["projetos"]], default=100) + 1

    usuario["projetos"].append({
        "id": novo_id,
        "nome": nome_projeto,
        "status": "novo",
        "tarefas": []
    })
        
        


def adicionar_tarefa(dados, usuario_id, projeto_id, titulo):
    usuario = buscar_usuario(dados, usuario_id)
    if not usuario:
        return
    for projeto in usuario["projetos"]:
        if projeto["id"] == projeto_id:
            novo_id = max([t["id"] for t in projeto["tarefas"]], default = 1000) + 1

            projeto["tarefas"].append({
                "id": novo_id,
                "titulo" : titulo,
                "concluida" : False
            })

            return
        


def concluir_tarefa(dados, usuario_id, projeto_id, tarefa_id):
    usuario = buscar_usuario(dados, usuario_id)
    if not usuario:
        return
    
    for projeto in usuario["projetos"]:
        if projeto["id"] == projeto_id:
            for tarefa in projeto["tarefas"]:
                if tarefa["id"] == tarefa_id:
                    tarefa["concluida"] = True

            if all (t["concluida"] for t in projeto ["tarefas"]):
                projeto["status"] = "finalizado"

def salvar_dados(dados):
    with open("sistema.json", "w", encoding = "utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def buscar_usuario(dados, usuario_id):
    for usuario in dados["usuarios"]:
        if usuario["id"] == usuario_id:
            return usuario
    return None

dados = carregar_dados()
def login(dados, nome, senha):
    global usuario_logado

    for usuario in dados["usuarios"]:
        if usuario["nome"] == nome and usuario ["senha"] == senha:
            if not usuario["ativo"]:
                print("usuario inativo")
                return False
            
            usuario_logado = usuario
            print(f"login efetuado: {nome}")
            return True
    print("nome ou senhas invalidas")
    return False


def logout():
    global usuario_logado
    if usuario_logado is None:
        print("nenhum usuario esta logado")
        return
    
    print(f"logout realizado: {usuario_logado["nome"]}")
    usuario_logado = None




    

adicionar_projeto(dados, 1, "sistema de login")
adicionar_tarefa(dados, 1, 102, "criar autenticaçao")
concluir_tarefa(dados, 1, 102, 1001)

salvar_dados(dados)



