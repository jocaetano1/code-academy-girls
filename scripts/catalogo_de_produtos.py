from colorama import Fore, Back, Style
from getpass import getpass
from time import sleep

from secretos import formatar_em_kwanza


produtos = []
root = {"usuario": "root", "senha": "demo"}

login = False
run = True
while run:
    print("=" * 50)
    print("Bem-vindo ao seu catálogo".center(50))
    print("=" * 50)
    if not login:
        usuario = input("Digite o seu usuário: ")
        senha = getpass("Digite a senha: ")
    if usuario is None or senha is None:
        print("Usuaário ou senha incorrectos.")
    if root["usuario"] == usuario and root["senha"] == senha:
        login = True

        print("""

Opções de navegação:

[1] - Inserir um novo produto.
[2] - Lista geral dos produtos.
[3] - Remover produto.
[9] - Terminar sessão. 

""")

    opcao = input("Escolha uma das opções: ").strip()

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a sua descricão: ")
        quantidade = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço [Kz]: "))

        produto = {}

        identificador = len(produtos) + 1

        produto["id"] = f"{identificador:06d}"
        produto["nome"] = nome
        produto["descricao"] = descricao
        produto["quantidade"] = quantidade
        produto["preco"] = preco

        produtos.append(produto)

        print(Style.NORMAL + Fore.GREEN, "Produto cadastrado com sucesso.")

    if opcao == "2":
        produtos = sorted(produtos)
        for produto in produtos:
            identificador = produto.get("id")
            nome = produto.get("nome")
            descricao = produto.get("descricao")
            quantidade = produto.get("quantidade")
            preco = produto.get("preco")
            print(f"""
-------------------------------------------
ID: {identificador}
Nome: {nome}
Descrição: {descricao}
Qtd.: {quantidade}
Preço: {formatar_em_kwanza(preco)}
-------------------------------------------
""")
    if opcao == "3":
        identificador = input("Digite o ID do produto: ").strip()
        for index, produto in enumerate(produtos):
            id_ = produto.get("id")
            if id_ == identificador:
                produtos.remove(produto)
                print(Style.NORMAL + Fore.GREEN,
                      f"\nProduto removido com sucesso. \n")

    if opcao == "9":
        print("""

Terminando a sessão...

""")
        run = False
        sleep(2.5)
