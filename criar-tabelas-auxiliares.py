import os
from dotenv import load_dotenv
import psycopg2

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações de conexão PostgreSQL
HOST = os.getenv("POSTGRES_HOST", "localhost")
PORT = int(os.getenv("POSTGRES_PORT", 5432))
USER = os.getenv("POSTGRES_USER", "seu_usuario")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "sua_senha")
DATABASE = os.getenv("POSTGRES_DB", "seu_banco")

def create_tables():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS qualificacoes_de_socios (
            codigo INTEGER PRIMARY KEY,
            descricao TEXT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS naturezas_juridicas (
            codigo INTEGER PRIMARY KEY,
            descricao TEXT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS cnaes (
            codigo INTEGER PRIMARY KEY,
            descricao TEXT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS paises (
            codigo INTEGER PRIMARY KEY,
            descricao TEXT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS municipios (
            codigo INTEGER PRIMARY KEY,
            descricao TEXT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS motivos (
            codigo INTEGER PRIMARY KEY,
            descricao TEXT NOT NULL
        )
        """
    ]

    # Conexão com o banco de dados
    connection = psycopg2.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        dbname=DATABASE
    )

    cursor = connection.cursor()
    
    for command in commands:
        cursor.execute(command)

    connection.commit()
    cursor.close()
    connection.close()

# Chama a função para criar as tabelas
create_tables()
