from flask import Request
from app.models.event import Event
from app.utils.StaticManager import StaticManager
from random import randint
from PIL import Image
class EventValidation:
    def __init__(self, request) -> None:
        self.request: Request = request # Request
        self.body = self.request.form # Body para ser validado
        self.files = self.request.files # Arquivos passados no body
        self.invalid: str = "" # String de errros
        self.filenames = []

    def isValid(self) -> bool:
        # Nome requerido e no maximo 100
        if not self.body.get("name") or len(self.body.get("name")) <= 0 or len(self.body.get("name")) > 100:
            self.invalid = "O nome do evento" # Retornando o erro
            return False
        
        # Configuração da velocidade requerido maximo 5
        if (not self.body.get("speedSet") or not self.body.get("speedSet").isdigit() 
        or int(self.body.get("speedSet")) < 1 or int(self.body.get("speedSet")) > 5):
            self.invalid = "A configuração de velocidade" # Retornando o erro
            return False
        
        # Configuração do tempo de reprodução de 5 a 60
        if (not self.body.get("recordingTime") or not self.body.get("recordingTime").isdigit() 
        or int(self.body.get("recordingTime")) < 5 or int(self.body.get("recordingTime")) > 60):
            self.invalid = "A configuração de tempo de reprodução" # Retornando o erro
            return False
        
        # Dono requerido
        if not self.body.get("owner") or self.body.get("owner") == None or self.body.get("owner") == "":
            self.invalid = "O token de login" # Retornando o erro
            return False
        
        # Reverse 
        if not self.body.get("reverse") or self.body.get("reverse") == None or self.body.get("reverse") == "":
            self.invalid = "O campo de reversão" # Retornando o erro
            return False
        
        return True # Caso tudo passe
    
    # Função que pega todos os valores já validados
    def getValues(self) -> Event:
        return {
            "name": self.request.form.get("name"),
            "speedSet": int(self.request.form.get("speedSet")),
            "recordingTime": int(self.request.form.get("recordingTime")),
            "owner": int(self.request.form.get("owner")),
            "reverse": bool(self.request.form.get("reverse"))
        }
    
    def imageValidation(self, file: str) -> None:
        f = self.files.get(file) # pegando o arquivo
        if f:
            randomNumber: int = randint(1000000000,9999999999) # Gerando um numero aleatorio
            folder = f"{self.body.get('name')}{randomNumber}" # Gerando um nome unico para o evento
            staticManager = StaticManager(folder=folder,type="/events/") # Gerenciamento do conteudo statico
            staticManager.createFolder() # Criando uma pasta
            folder = staticManager.folder # Atualizando o caminho para o folder
            fp = folder+"/"+f.filename # caminho para o arquivo mais o nome do arquivo
            if not f.content_type.startswith("image"): # Vendo se é uma imagem
                self.invalid = file # Definindo como invalido
                staticManager.deleteFolder()
                return # retornando
            else: 
                f.save(fp) # Salvando arquivo
                with Image.open(fp) as img:
                    w, h = img.size # Dimensões 
                    
                    # Se as dimensões não forem as minimas
                    if (w < 1080 or h < 1920):
                        staticManager.deleteFolder(folder)
                        self.invalid = file
                        return
                    
                    img.resize((1080,1920)) # Redimensionando imagem
                    img.save(format="png",optimize=True,
                    fp=fp,quality=80) # Salvando imagem e optimizando
                    self.filenames.append(fp) # Salvando nomes
        else:
            self.filenames.append("") # Salvando nomes
            return # retornando caso não tenha arquivo
    
    def audioValidation(self, file: str) -> None:
        f = self.files.get(file) # pegando o arquivo
        if f:
            randomNumber: int = randint(1000000000,9999999999) # Gerando um numero aleatorio
            folder = f"{self.body.get('name')}{randomNumber}" # Gerando um nome unico para o evento
            staticManager = StaticManager(folder=folder,type="/events/") # Gerenciamento do conteudo statico
            staticManager.createFolder() # Criando uma pasta
            folder = staticManager.folder # Atualizando o caminho para o folder
            fp = folder+f.filename # caminho para o arquivo mais o nome do arquivo
            if not f.content_type.startswith("audio"): # Caso não seja um arquivo e seja do tipo audio
                self.invalid = file # Invalidando
                return # retornando
            else:
                f.save(fp) # Salvando a musica
                self.filenames.append(fp) # Salvando nomes
        else:
            self.filenames.append("") # Salvando nomes
            return
    
    def filesIsValid(self) -> bool:
        self.imageValidation("frame") # Verificando o frame
        self.audioValidation("music") # Verificando a musica
        self.imageValidation("iniImage") # Verificando a imagem inicial
        self.imageValidation("finImage") # Verificando a imagem final
        if len(self.invalid) > 0: # Vendo se não há nenhum arquivo invalido
            return False # Retornando false caso sim
        else:
            return True # Retornando true caso não
                


                
                
                

        

