from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from config.config import USER_NAME, PASSWORD, HOST, PORT, DATABASE


engine = create_engine(f'postgresql+psycopg2://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()



class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, autoincrement=True, primary_key=True)
    sarlavha = Column(String(70), nullable=False)
    muallif = Column(String(30), nullable=False)
    janra = Column(String(30), nullable=False)


    def save(self, session):
        session.add(self)
        session.commit()
