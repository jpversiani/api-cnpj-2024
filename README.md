## SlimAPI - API-CNPJ-2024

- Python
- FastAPI (REST API)
- Gunicorn (WSGI HTTP Server)
- Docker / Docker Compose (Container Orchestration)
- Nginx (Load Balancer)
- Postgres (Database)
- Redis (Distributed Cache)

## Atualizar lista de pacotes e instalar o Git

```bash
sudo apt update
sudo apt install git
```

# Clonar o repositório
```bash
git clone https://github.com/jpversiani/api-cnpj-2024.git
```
# Navegar para o diretório do projeto
```bash
cd api-cnpj-2024
```
# Necessário criar um arquivo .env com variáveis de ambiente sensíveis
```bash
nano .env
```
Ou use outro editor de texto.

# Adicionar as variáveis no arquivo .env
```bash

DATABASE_URL=postgresql://<username>:<password>@<host>/<database>;

DATABASE_MAX_CONNECTIONS=200;

CACHE_HOST=cache-redis;

GUNICORN_BIND=0.0.0.0:8000;

GUNICORN_WORKERS=2;

GUNICORN_KEEPALIVE=4;

GUNICORN_FORWARDED_ALLOW_IPS=*;

POSTGRES_USER=seu_usuario;

POSTGRES_PASSWORD=sua_senha;

POSTGRES_DB=NomedoseuBanco;

POSTGRES_HOST=localhost;

POSTGRES_PORT=5432;
```
# Iniciar os serviços com Docker Compose
```bash
docker-compose up -d
```
# Ver os logs dos serviços
```bash
docker-compose logs -f
```
## Rodando localmente

> Necessário Docker

```bash
sh run.sh
```

API disponível em: [localhost:9999](http://localhost:9999)

Para parar:
```bash
sh stop.sh
```
