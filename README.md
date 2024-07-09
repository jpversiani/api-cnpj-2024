# SlimAPI - API-CNPJ-2024

# Atualizar lista de pacotes e instalar o Git
sudo apt update
sudo apt install git

# Clonar o repositório
git clone https://github.com/jpversiani/api-cnpj-2024.git

# Navegar para o diretório do projeto
cd api-cnpj-2024

# Necessário criar um arquivo .env com variáveis de ambiente sensíveis
nano .env
Ou use outro editor de texto.

# Adicionar as variáveis no arquivo .env

DATABASE_URL=postgresql://<username>:<password>@<host>/<database>
DATABASE_MAX_CONNECTIONS=200
CACHE_HOST=cache-redis
GUNICORN_BIND=0.0.0.0:8000
GUNICORN_WORKERS=2
GUNICORN_KEEPALIVE=4
GUNICORN_FORWARDED_ALLOW_IPS=*
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=NomedoseuBanco
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Iniciar os serviços com Docker Compose
docker-compose up -d

# Ver os logs dos serviços
docker-compose logs -f

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
