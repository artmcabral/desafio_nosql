from pymongo import MongoClient
import redis
import json

# MongoDB
uri = "mongodb+srv://artmcabral:Maxmots2025!@cluster0.767lktj.mongodb.net/?appName=Cluster0"

cliente_mongo = MongoClient(uri)
db = cliente_mongo["desafio_nosql"]
colecao = db["produtos"]

# Redis
r = redis.Redis(
    host="basketball-sunup-retroswift-23924.db.redis.io",
    port=12109,
    username="default",
    password="DQ9ZJoj90MbrP0PiQujrt8thqO2hCh0l",
    decode_responses=True
)

def buscar_produto(nome):
    
    chave_cache = f"produto:{nome}"

    # Verifica no Redis
    produto_cache = r.get(chave_cache)

    if produto_cache:
        print("Produto encontrado no Redis!")
        return json.loads(produto_cache)

    # Busca no MongoDB
    produto = colecao.find_one(
        {"nome": nome},
        {"_id": 0}
    )

    if produto:
        print("Produto encontrado no MongoDB!")

        r.set(
        chave_cache,
        json.dumps(produto),
        ex=60
    )

    return produto


produto = buscar_produto("Mouse")

print(produto)