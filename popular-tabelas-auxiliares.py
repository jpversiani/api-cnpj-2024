# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:41:48 2024

@author: joaop
"""

import csv
import os
import chardet
import psycopg2
from psycopg2 import sql

# Configurações de conexão PostgreSQL
HOST = os.getenv("POSTGRES_HOST", "localhost")
PORT = int(os.getenv("POSTGRES_PORT", 5432))
USER = os.getenv("POSTGRES_USER", "seu_usuario")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "sua_senha")
DATABASE = os.getenv("POSTGRES_DB", "seu_banco")

def detect_encoding(file_path):
    # Detecta a codificação do arquivo lendo uma amostra do início do arquivo
    with open(file_path, 'rb') as f:
        raw_data = f.read(1024)
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    return encoding

def clear_table(table_name):
    # Conexão com o banco de dados
    connection = psycopg2.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        dbname=DATABASE
    )
    
    cursor = connection.cursor()
    
    # Limpa a tabela
    cursor.execute(sql.SQL("DELETE FROM {}").format(sql.Identifier(table_name)))
    
    connection.commit()
    cursor.close()
    connection.close()

def populate_table(table_name, file_path):
    # Detecta a codificação do arquivo
    encoding = detect_encoding(file_path)

    # Conexão com o banco de dados
    connection = psycopg2.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        dbname=DATABASE
    )
    
    cursor = connection.cursor()

    with open(file_path, 'r', encoding=encoding) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            cursor.execute(
                sql.SQL("INSERT INTO {} (codigo, descricao) VALUES (%s, %s)").format(sql.Identifier(table_name)),
                (int(row[0]), row[1])
            )

    connection.commit()
    cursor.close()
    connection.close()

# Diretório dos arquivos CSV
extract_dir = 'C:/Users/joaop/Downloads/CNPJ - Empresas/Descompactados10'

# Mapeamento dos arquivos para as tabelas correspondentes
files_to_tables = {
    "Qualificacoes.csv": "qualificacoes_de_socios",
    "Naturezas.csv": "naturezas_juridicas",
    "Cnaes.csv": "cnaes",
    "Paises.csv": "paises",
    "Municipios.csv": "municipios",
    "Motivos.csv": "motivos"
}

# Limpa as tabelas antes de reimportar os dados
for file_name, table_name in files_to_tables.items():
    print(f"Limpando dados da tabela {table_name}")
    clear_table(table_name)

# Reimporta os dados nas tabelas
for file_name, table_name in files_to_tables.items():
    file_path = os.path.join(extract_dir, file_name)
    print(f"Populando tabela {table_name} com dados de {file_path}")
    populate_table(table_name, file_path)

