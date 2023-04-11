from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from env import DB_URL
engine = create_engine(url=DB_URL,echo=True) # Criando conexão
Session = sessionmaker(bind=engine) # Criando engine