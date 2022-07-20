
from sqlalchemy import Column, Integer, TEXT, Numeric
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RestCountries(Base):
    __tablename__ = 'restcountries'

    id = Column(Integer, primary_key=True)
    index = Column(Integer)
    name = Column(TEXT)
    region = Column(TEXT)
    lenguage = Column(TEXT)
    time = Column(Numeric)    

def do_conection():
    engine = create_engine('sqlite:///db.sqlite3', echo=True)
    conn = engine.connect()
    return conn

engine = do_conection()

class ManageSession:
    def manage_session(self):
        Session = sessionmaker(engine)
        session = Session()
        return session


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    
