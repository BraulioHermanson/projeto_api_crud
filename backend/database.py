from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

#Cria o motor do banco de dados - faz a conexao com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessao do banco de dados, que ira executar as queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base para os modelos declarativos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()