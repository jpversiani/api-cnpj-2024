-- Script SQL para criar tabelas no banco Postgres-CNPJ

-- Tabela simples
CREATE TABLE simples (
    cnpj_basico VARCHAR(8) PRIMARY KEY,
    opcao_simples CHAR(1),
    data_opcao_simples DATE,
    data_exclusao_simples DATE,
    opcao_mei CHAR(1),
    data_opcao_mei DATE,
    data_exclusao_mei DATE
);

-- Tabela estabelecimentos
CREATE TABLE estabelecimentos (
    cnpj_basico VARCHAR(8),
    cnpj_ordem VARCHAR(4),
    cnpj_dv VARCHAR(2),
    identificador_matriz_filial INTEGER,
    nome_fantasia VARCHAR(255),
    situacao_cadastral INTEGER,
    data_situacao_cadastral DATE,
    motivo_situacao_cadastral INTEGER,
    nome_cidade_exterior VARCHAR(255),
    pais INTEGER,
    data_inicio_atividade DATE,
    cnae_fiscal_principal INTEGER,
    cnae_fiscal_secundaria TEXT,
    tipo_logradouro VARCHAR(50),
    logradouro VARCHAR(255),
    numero VARCHAR(50),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cep VARCHAR(8),
    uf VARCHAR(2),
    municipio INTEGER,
    ddd_1 VARCHAR(4),
    telefone_1 VARCHAR(15),
    ddd_2 VARCHAR(4),
    telefone_2 VARCHAR(15),
    ddd_fax VARCHAR(4),
    fax VARCHAR(15),
    correio_eletronico VARCHAR(255),
    situacao_especial VARCHAR(50),
    data_situacao_especial DATE,
    PRIMARY KEY (cnpj_basico, cnpj_ordem, cnpj_dv)
);

-- Tabela empresas
CREATE TABLE empresas (
    cnpj_basico TEXT PRIMARY KEY,
    razao_social TEXT,
    capital_social NUMERIC,
    ente_federativo_responsavel TEXT,
    qualificacao_responsavel INTEGER,
    natureza_juridica INTEGER,
    porte_empresa INTEGER
);




-- Tabela estabelecimentos
CREATE TABLE estabelecimentos4 (
    cnpj_basico VARCHAR(8),
    cnpj_ordem VARCHAR(4),
    cnpj_dv VARCHAR(2),
    identificador_matriz_filial INTEGER,
    nome_fantasia VARCHAR(255),
    situacao_cadastral INTEGER,
    data_situacao_cadastral VARCHAR(10),
    motivo_situacao_cadastral INTEGER,
    nome_cidade_exterior VARCHAR(255),
    pais INTEGER,
    data_inicio_atividade VARCHAR(10),
    cnae_fiscal_principal INTEGER,
    cnae_fiscal_secundaria TEXT,
    tipo_logradouro VARCHAR(50),
    logradouro VARCHAR(255),
    numero VARCHAR(50),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cep VARCHAR(8),
    uf VARCHAR(2),
    municipio INTEGER,
    ddd_1 VARCHAR(4),
    telefone_1 VARCHAR(15),
    ddd_2 VARCHAR(4),
    telefone_2 VARCHAR(15),
    ddd_fax VARCHAR(4),
    fax VARCHAR(15),
    correio_eletronico VARCHAR(255),
    situacao_especial VARCHAR(50),
    data_situacao_especial VARCHAR(10),
    PRIMARY KEY (cnpj_basico, cnpj_ordem, cnpj_dv)
);



