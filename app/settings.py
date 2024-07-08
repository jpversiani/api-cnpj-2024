import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a URL do banco de dados do arquivo .env ou usar um valor padrão seguro
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://<username>:<password>@<host>/<database>')
DATABASE_MAX_CONNECTIONS = int(os.getenv('DATABASE_MAX_CONNECTIONS', 10))

# Obter configurações de cache do arquivo .env ou usar valores padrão seguros
CACHE_HOST = os.getenv('CACHE_HOST', 'localhost')
CACHE_PORT = int(os.getenv('CACHE_PORT', 6379))

# Configurações do Gunicorn obtidas do arquivo .env ou usando valores padrão
GUNICORN_BIND = os.getenv('GUNICORN_BIND', 'localhost:8000')
GUNICORN_WORKERS = int(os.getenv('GUNICORN_WORKERS', 1))
GUNICORN_KEEPALIVE = int(os.getenv('GUNICORN_KEEPALIVE', 2))
GUNICORN_FORWARDED_ALLOW_IPS = os.getenv('GUNICORN_FORWARDED_ALLOW_IPS', '*')
