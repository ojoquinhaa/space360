from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import getenv
load_dotenv() # Carregando o .env
URL = getenv("DB_URL") # Pegando a URL da database do .env
engine = create_engine(url=URL,echo=True) # Criando conexão
Session = sessionmaker(bind=engine) # Criando engine