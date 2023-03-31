from flask import Flask, Blueprint
from app.routes.dashboard import dashboardBp
from app.api import eventBp
def register_bp(app:Flask,blueprint:Blueprint) -> None: # Criando função para registrar o blueprint
    app.register_blueprint(blueprint=blueprint) # Registrando o blueprint
def create_app() -> Flask: # Função para criar a aplicação
    app = Flask(__name__) # Criando app
    register_bp(app,dashboardBp) # Registrando dashboard
    register_bp(app,eventBp) # Registrando eventos
    return app # Retornando app