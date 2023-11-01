from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

class Palavras(Base):
    __tablename__ = 'palavras'
    codigo = Column(Integer, primary_key = True )
    nome = Column(String(100), nullble=False)

engine = create_engine('sqlite:///trabalho.db')
Base.metadata.create_all(engine)