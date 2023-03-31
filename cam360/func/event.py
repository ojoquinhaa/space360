from connection.models import Event
from connection.connect import conn
class EventFunc(Event):
    # Função para pegar todos os eventos
    def getAll(self): 
        e = conn.query(Event).all() # todos os eventos
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
        
        conn.add(event) # Adicionando evento
        conn.commit() # Fazendo o commit
        conn.close() # Fechando a sessão

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
    
    def isInvalid(self,value,type,min,max):
        # Função que analisa os valores do evento
        if type == 0:
            if value == None or value == "" or len(value) > max:
                return True
        if type == 1:
            if value == None or value == 0 or value > max or value < min:
                return True
        return False

    def validate(self,body):
        # Validando os valores do evento
        if (self.isInvalid(body.get("name"),0,0,100) or
        self.isInvalid(body.get("speedSet"),1,0,3) or
        self.isInvalid(body.get("recordingTime"),1,5,60) or
        self.isInvalid(body.get("owner"),1,0,99999999) or
        body.get("reverse") == None):
            return "Credenciáis inválidas."
        return False