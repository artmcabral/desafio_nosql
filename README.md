# Atividade NoSQL - MongoDB e Redis

## Tecnologias Utilizadas

* Python 3
* MongoDB Atlas
* Redis Cloud
* PyMongo
* Redis-Py

---

## Instalação das Dependências

Instale as bibliotecas necessárias:

```bash
python -m pip install pymongo
python -m pip install redis
```

---

## Estrutura do Projeto

```text
mongodb.py
redis_teste.py
cache.py
README.md
```

### mongodb.py

Responsável pelas operações CRUD no MongoDB:

* Inserção de produtos
* Consulta de produtos
* Atualização de produtos
* Remoção de produtos

### redis_teste.py

Responsável pelos testes de funcionalidades do Redis:

* String
* Hash
* Lista
* Leitura de dados

### cache.py

Responsável pela integração entre MongoDB e Redis através de cache com tempo de expiração.

---

## MongoDB

Foi criado o banco de dados:

```text
desafio_nosql
```

Coleção:

```text
produtos
```

Cada produto possui os seguintes atributos:

* nome
* preco
* categoria

### Operações Implementadas

#### Inserção

Adiciona produtos na coleção.

#### Consulta

Busca produtos com preço maior que 10.

#### Atualização

Atualiza o preço de um produto específico.

#### Remoção

Remove um produto de determinada categoria.

---

## Redis

Foram implementadas as seguintes estruturas:

### String

```text
mensagem:inicio
```

Armazena uma mensagem de boas-vindas.

### Hash

```text
usuario:1
```

Armazena informações de um usuário:

* nome
* email

### Lista

```text
logs
```

Armazena registros de ações realizadas pelo sistema.

---

## Cache MongoDB + Redis

Foi implementado um mecanismo de cache para consultas de produtos.

Funcionamento:

1. O sistema verifica se o produto está armazenado no Redis.
2. Caso esteja, retorna os dados diretamente do cache.
3. Caso não esteja, consulta o MongoDB.
4. O resultado é armazenado no Redis.
5. O cache possui TTL (Time To Live) de 60 segundos.

## Execução

### MongoDB

```bash
python mongodb.py
```

### Redis

```bash
python redis_teste.py
```

### Cache

```bash
python cache.py
```

---

## Autor

Artur Murada Cabral
