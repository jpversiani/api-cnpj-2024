import json
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, String, Integer, Numeric, Date, Text
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import redis
import settings

# FastAPI
app = FastAPI(title='API-CNPJ-2024', description="API para consulta de dados de CNPJ, incluindo empresas, estabelecimentos, sócios, naturezas jurídicas, CNAEs, países e municípios.")

# Redis
cache = redis.StrictRedis(host=settings.CACHE_HOST, port=settings.CACHE_PORT, decode_responses=True)

# SQLAlchemy
engine = create_engine(settings.DATABASE_URL, pool_size=settings.DATABASE_MAX_CONNECTIONS)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelos das tabelas
class QualificacaoSocio(Base):
    __tablename__ = 'qualificacoes_de_socios'
    codigo = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)

class NaturezaJuridica(Base):
    __tablename__ = 'naturezas_juridicas'
    codigo = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)

class CNAE(Base):
    __tablename__ = 'cnaes'
    codigo = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)

class Pais(Base):
    __tablename__ = 'paises'
    codigo = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)

class Municipio(Base):
    __tablename__ = 'municipios'
    codigo = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)

class Motivo(Base):
    __tablename__ = 'motivos'
    codigo = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)

class Simples(Base):
    __tablename__ = 'simples'
    cnpj_basico = Column(String, primary_key=True, index=True)
    opcao_simples = Column(String)
    data_opcao_simples = Column(Date)
    data_exclusao_simples = Column(Date)
    opcao_mei = Column(String)
    data_opcao_mei = Column(Date)
    data_exclusao_mei = Column(Date)

class Estabelecimento(Base):
    __tablename__ = 'estabelecimentos'
    cnpj_basico = Column(String, primary_key=True, index=True)
    cnpj_ordem = Column(String)
    cnpj_dv = Column(String)
    identificador_matriz_filial = Column(Integer)
    nome_fantasia = Column(String)
    situacao_cadastral = Column(Integer)
    data_situacao_cadastral = Column(Date)
    motivo_situacao_cadastral = Column(Integer)
    nome_cidade_exterior = Column(String)
    pais = Column(Integer)
    data_inicio_atividade = Column(Date)
    cnae_fiscal_principal = Column(Integer)
    cnae_fiscal_secundaria = Column(Text)
    tipo_logradouro = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    complemento = Column(String)
    bairro = Column(String)
    cep = Column(String)
    uf = Column(String)
    municipio = Column(Integer)
    ddd_1 = Column(String)
    telefone_1 = Column(String)
    ddd_2 = Column(String)
    telefone_2 = Column(String)
    ddd_fax = Column(String)
    fax = Column(String)
    correio_eletronico = Column(String)
    situacao_especial = Column(String)
    data_situacao_especial = Column(Date)

class Empresa(Base):
    __tablename__ = 'empresas'
    cnpj_basico = Column(Text, primary_key=True, index=True)
    razao_social = Column(Text)
    capital_social = Column(Numeric)
    ente_federativo_responsavel = Column(Text)
    qualificacao_responsavel = Column(Integer)
    natureza_juridica = Column(Integer)
    porte_empresa = Column(Integer)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(req: Request, exc: RequestValidationError):
    details = exc.errors()
    if any(detail['type'] == 'string_type' and isinstance(detail['input'], int) for detail in details):
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder({'detail': details}),
        )    
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({'detail': details}),
    )

def serialize(data):
    return json.dumps(data, default=str)

def deserialize(data):
    return json.loads(data)

@app.get("/qualificacoes_de_socios")
async def get_qualificacoes_de_socios(session: Session = Depends(get_session)):
    """
    Obtém todas as qualificações de sócios.

    Retorna:
        Uma lista de todas as qualificações de sócios e seus respectivos códigos.
    """
    result = session.query(QualificacaoSocio).all()
    return JSONResponse(content=jsonable_encoder(result))

@app.get("/naturezas_juridicas")
async def get_naturezas_juridicas(session: Session = Depends(get_session)):
    """
    Obtém todas as naturezas jurídicas.

    Retorna:
        Uma lista de todas as naturezas jurídicas e seus respectivos códigos.
    """
    result = session.query(NaturezaJuridica).all()
    return JSONResponse(content=jsonable_encoder(result))

@app.get("/cnaes")
async def get_cnaes(session: Session = Depends(get_session)):
    """
    Obtém todos os CNAEs.

    Retorna:
        Uma lista de todos os CNAEs e seus respectivos códigos.
    """
    result = session.query(CNAE).all()
    return JSONResponse(content=jsonable_encoder(result))

@app.get("/paises")
async def get_paises(session: Session = Depends(get_session)):
    """
    Obtém todos os países.

    Retorna:
        Uma lista de todos os países e seus respectivos códigos.
    """
    result = session.query(Pais).all()
    return JSONResponse(content=jsonable_encoder(result))

@app.get("/municipios")
async def get_municipios(session: Session = Depends(get_session)):
    """
    Obtém todos os municípios.

    Retorna:
        Uma lista de todos os municípios e seus respectivos códigos.
    """
    result = session.query(Municipio).all()
    return JSONResponse(content=jsonable_encoder(result))

@app.get("/motivos")
async def get_motivos(session: Session = Depends(get_session)):
    """
    Obtém todos os motivos.

    Retorna:
        Uma lista de todos os motivos e seus respectivos códigos.
    """
    result = session.query(Motivo).all()
    return JSONResponse(content=jsonable_encoder(result))

@app.get("/simples")
async def get_simples(cnpj_basico: str, session: Session = Depends(get_session)):
    """
    Obtém os dados do Simples Nacional para um determinado CNPJ básico.

    Parâmetros:
        cnpj_basico: O CNPJ básico a ser consultado. Apenas caracteres numéricos, sem uso de ponto ou hífen (Ex: 04967910).  

    Retorna:
        Dados do Simples Nacional correspondentes ao CNPJ básico fornecido.
    """
    result = session.query(Simples).filter(Simples.cnpj_basico == cnpj_basico).all()
    if not result:
        raise HTTPException(status_code=404, detail="CNPJ básico não encontrado")
    return JSONResponse(content=jsonable_encoder(result))

@app.get("/estabelecimentos")
async def get_estabelecimentos(cnpj_basico: str, cnpj_ordem: str = None, cnpj_dv: str = None, session: Session = Depends(get_session)):
    """
    Obtém os dados de estabelecimentos para um determinado CNPJ básico.

    Parâmetros:
        cnpj_basico: O CNPJ básico a ser consultado. Apenas caracteres numéricos, sem uso de ponto ou hífen (Ex: 04967910).   
        cnpj_ordem: (Opcional) A ordem do CNPJ para consulta específica (Ex: 0001).   
        cnpj_dv: (Opcional) O dígito verificador do CNPJ para consulta específica (Ex: 10).   

    Retorna:
        Dados dos estabelecimentos correspondentes aos parâmetros fornecidos.
    """
    query = session.query(Estabelecimento).filter(Estabelecimento.cnpj_basico == cnpj_basico)
    if cnpj_ordem:
        query = query.filter(Estabelecimento.cnpj_ordem == cnpj_ordem)
    if cnpj_dv:
        query = query.filter(Estabelecimento.cnpj_dv == cnpj_dv)
    result = query.all()
    if not result:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")
    return JSONResponse(content=jsonable_encoder(result))

@app.get("/empresas")
async def get_empresas(cnpj_basico: str, session: Session = Depends(get_session)):
    """
    Obtém os dados de empresas para um determinado CNPJ básico.

    Parâmetros:
        cnpj_basico: O CNPJ básico a ser consultado. Apenas caracteres numéricos, sem uso de ponto ou hífen (Ex: 04967910).  

    Retorna:
        Dados das empresas correspondentes ao CNPJ básico fornecido.
    """
    result = session.query(Empresa).filter(Empresa.cnpj_basico == cnpj_basico).all()
    if not result:
        raise HTTPException(status_code=404, detail="CNPJ básico não encontrado")
    return JSONResponse(content=jsonable_encoder(result))
