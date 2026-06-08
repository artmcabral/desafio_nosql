import redis

r = redis.Redis(
    host="basketball-sunup-retroswift-23924.db.redis.io",
    port=12109,
    username="default",
    password="DQ9ZJoj90MbrP0PiQujrt8thqO2hCh0l",
    decode_responses=True
)

try:
    r.ping()
    print("Conectado ao Redis!")

    r.set("mensagem:inicio", "Bem-vindo ao Redis!")

    print(r.get("mensagem:inicio"))

except Exception as e:
    print("Erro:", e)

r.hset(
    "usuario:1",
    mapping={
        "nome": "Artur",
        "email": "artur@email.com"
    }
)

print(r.hgetall("usuario:1"))


from datetime import datetime

r.rpush(
    "logs",
    f"{datetime.now()} - Sistema iniciado"
)

r.rpush(
    "logs",
    f"{datetime.now()} - Produto consultado"
)

print("\nLogs:")

for log in r.lrange("logs", 0, -1):
    print(log)