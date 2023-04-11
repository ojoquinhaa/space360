from os import getcwd, path, makedirs
from shutil import rmtree
class StaticManager:
    def __init__(self,folder:str,type:str='/')->None:
        self.folder = f"{getcwd()}/app/static{type}{folder}"
    def createFolder(self):
        # verifique se o diretório de destino existe, caso contrário, crie-o
        if not path.exists(self.folder):
            makedirs(self.folder)
    def deleteFolder(self):
        if path.exists(self.folder):
            rmtree(self.folder)