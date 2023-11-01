from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from aula import Palavras 


engine = create_engine('sqlite:///trabalho.db')
Session = sessionmaker(bind=engine)
Session = Session()


#Inserindo registros

palavra1 = Palavras(codigo=1, nome='casa')
palavra2 = Palavras(codigo=2, nome='carro')
Session.add(palavra1)
Session.add(palavra2)
Session.commit()

listapalavras = Session.query(Palavras).all()
for palavra in listapalavras:
    print(palavra.nome)
