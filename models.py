
from sqlalchemy import Column, Integer, TEXT, DATE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RestCountries(Base):
    __tablename__ = 'restcountries'

    id = Column(Integer, primary_key=True)
    index = Column(Integer)    
    region = Column(TEXT)
    city_name = Column(TEXT)
    lenguage = Column(TEXT)
    time = Column(DATE)    

def do_conection():
    engine = create_engine('sqlite:///test.sqlite3', echo=True)
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
    # info = RestCountries(index=0, region='region', city_name='city_name', lenguage='lenguage', time=datetime.utcnow())
    # Session = sessionmaker(engine)
    # session = Session()
    # session.add(info)
    # session.commit()
    
