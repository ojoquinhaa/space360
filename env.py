import os
from dotenv import load_dotenv

load_dotenv() # carregando o dotenv

DB_URL = os.getenv("DB_URL") # SALVANDO A URL
