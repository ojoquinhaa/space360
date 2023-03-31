from flask import Blueprint, jsonify, request
from app.api.event import EventFunc
eventBp = Blueprint("event",__name__,template_folder="../templates") # Criando o Blueprint
@eventBp.route("/api/event",methods=["GET","POST"]) # Rota / GET
def Events(): # Função que retorna a pagina do dash board
    if request.method == "GET": # Metodo GET
        events = EventFunc().getAll() # Pega todos os eventos
        
        # Caso não tenha nenhum evento
        if not events:
            return jsonify({"error":"Não foi encontrado nenhum evento"}), 200 
        
        return jsonify({"events": events}) # Retornando todos os eventos
    
    if request.method == "POST":
        body = request.json # Pegando o body

        # Validando os valores do evento
        if EventFunc().validate(body=body):
            return jsonify({"msg":"Credenciáis Inválidas."}), 400
        
        # Separando todos os valores de criação de um evento
        name = body.get("name")
        speedSet = body.get("speedSet")
        recordingTime = body.get("recordingTime")
        frame = body.get("frame") or ""
        music = body.get("music") or ""
        reverse = body.get("reverse")
        iniImage = body.get("iniImage") or ""
        finImage = body.get("finImage") or ""
        owner = body.get("owner")

        # Chamando a função que cria um evento
        event = EventFunc().create(name,speedSet=speedSet,recordingTime=recordingTime,frame=frame,music=music,reverse=reverse,iniImage=iniImage,finImage=finImage,owner=owner)

        return jsonify({"event":event}), 201 # Retornando um evento
