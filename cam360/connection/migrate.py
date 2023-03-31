from connection.connect import engine
from models import Event
def migrate(): Event().metadata.create_all(engine) # Criando a tabela de eventos