from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
from typing import Optional

# Chamando a classe base
class Base(DeclarativeBase):
    pass

# Criando a tabela de eventos
class Event(Base):
    __tablename__ = "Event"
    id: Mapped[int] = mapped_column(primary_key=True) # Adicionando Indentificador
    name: Mapped[str] = mapped_column(String(100)) # Nome 
    speedSet: Mapped[int] = mapped_column(Integer()) # Configurações de velocidade do video
    recordingTime: Mapped[int] = mapped_column(Integer()) # Tempo de gravação
    frame: Mapped[Optional[str]] = mapped_column(String(100)) # Caminho para Moldura opcional
    music: Mapped[Optional[str]] = mapped_column(String(100)) # Caminho para Musica opcional
    reverse: Mapped[bool] = mapped_column(Boolean()) # Video em formato boomerang
    iniImage: Mapped[Optional[str]] = mapped_column(String(100)) # Imagem de inicio opcional
    finImage: Mapped[Optional[str]] = mapped_column(String(100)) # Imagem de fim opcional
    owner: Mapped[int] = mapped_column(Integer()) # Dono
