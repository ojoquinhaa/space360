from flask import Blueprint, jsonify, request
from app.api.event import EventFunc
from app.validations.event import EventValidation
eventBp = Blueprint("event",__name__,template_folder="../templates") # Criando o Blueprint

@eventBp.route("/api/event",methods=["GET","POST"]) # Rota / GET
def Events(): # Função que retorna a pagina do dash board
    if request.method == "GET": # Metodo GET
        events = EventFunc().getAll() # Pega todos os eventos
        
        # Caso não tenha nenhum evento
        if not events:
            return jsonify({"error":"Não foi encontrado nenhum evento"}), 200 
        
        return jsonify(events), 200 # Retornando todos os eventos
    
    if request.method == "POST":
        validation = EventValidation(request=request) # Criando a validação de eventos
        
        if not validation.isValid():
            return jsonify({"error": f"{validation.invalid} está invalido"})
        
        body = validation.getValues() # Pegando o formulario validado
            
        # Separando todos os valores de criação de um evento
        name = body['name']
        speedSet = body['speedSet']
        recordingTime = body['recordingTime']
        reverse = body['reverse']
        owner = body['owner']

        if not validation.filesIsValid():
            return jsonify({"error":f"O {validation.invalid} está inválido."}), 400

        # Separando os arquivos de criação de evento
        frame = validation.filenames[0]
        music = validation.filenames[1]
        iniImage = validation.filenames[2]
        finImage = validation.filenames[3]

        # Chamando a função que cria um evento
        event = EventFunc().create(name,speedSet=speedSet,recordingTime=recordingTime,frame=frame,music=music,reverse=reverse,iniImage=iniImage,finImage=finImage,owner=owner)

        return jsonify({"event":event}), 201 # Retornando um evento
