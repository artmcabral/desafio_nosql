from pymongo import MongoClient

uri = "mongodb+srv://artmcabral:Maxmots2025!@cluster0.767lktj.mongodb.net/?appName=Cluster0"

cliente = MongoClient(uri)

db = cliente["desafio_nosql"]
colecao = db["produtos"]


def inserir_produtos():

    produtos = [
        {
            "nome": "Mouse",
            "preco": 50,
            "categoria": "Perifericos"
        },
        {
            "nome": "Teclado",
            "preco": 120,
            "categoria": "Perifericos"
        },
        {
            "nome": "Caderno",
            "preco": 15,
            "categoria": "Papelaria"
        }
    ]

    if colecao.count_documents({}) == 0:
        colecao.insert_many(produtos)
        print("Produtos inseridos com sucesso!")
    else:
        print("Produtos já cadastrados!")


def consultar_produtos():

    print("\nProdutos com preço maior que 10:")

    produtos_encontrados = colecao.find(
        {"preco": {"$gt": 10}}
    )

    for produto in produtos_encontrados:
        print(produto)


def atualizar_produto():

    colecao.update_one(
        {"nome": "Mouse"},
        {"$set": {"preco": 80}}
    )

    print("\nPreço do Mouse atualizado!")

    mouse = colecao.find_one({"nome": "Mouse"})

    print("\nMouse após atualização:")
    print(mouse)


def remover_produto():

    colecao.delete_one(
        {"categoria": "Papelaria"}
    )

    print("\nProduto da categoria Papelaria removido!")

    print("\nProdutos restantes:")

    for produto in colecao.find():
        print(produto)


inserir_produtos()
consultar_produtos()
atualizar_produto()
remover_produto()