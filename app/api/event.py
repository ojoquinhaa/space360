from app.models.event import Event
from app.config import Session

class EventFunc(Event):
    def __init__(self) -> None:
        self.conn = Session()
    # Função para pegar todos os eventos
    def getAll(self): 
        self.conn.expunge_all()
        e = self.conn.query(Event).all() # todos os eventos
        events = [] # todos eventos em uma array

        # Organizando a array
        for x in e:
            events.append({
                "id": x.name,
                "speedSet": x.speedSet,
                "recordingTime": x.recordingTime,
                "frame": x.frame,
                "music": x.music,
                "reverse": x.reverse,
                "iniImage": x.iniImage,
                "finImage": x.finImage,
                "owner": x.owner
            })

        return events # Retornando todos os eventos
    
    def create(self,name:str,speedSet:int,recordingTime:int,
    frame:str,music:str,reverse:bool,iniImage:str,finImage:str,owner:str):
        # Criando o objeto evento
        event = Event(name=name,speedSet=speedSet,recordingTime=recordingTime
                    ,frame=frame,music=music,reverse=reverse,
                    iniImage=iniImage,finImage=finImage,owner=owner)
        
        self.conn.expunge_all()
        self.conn.add(event) # Adicionando evento
        self.conn.commit() # Fazendo o commit

        # Retornando todo o evento criado
        return {
            'name': event.name,
            'speedSet': event.speedSet,
            'recordingTime': event.recordingTime,
            'frame': event.frame,
            'music': event.music,
            'reverse': event.reverse,
            'iniImage': event.iniImage,
            'finImage': event.finImage,
            'owner': event.owner,
        }