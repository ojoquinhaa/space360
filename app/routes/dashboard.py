from flask import Blueprint, render_template
dashboardBp = Blueprint("dashboard",__name__,template_folder="../templates") # Criando o Blueprint
@dashboardBp.route("/dashboard",methods=["GET"]) # Rota / GET
def getHomePagePath(): # Função que retorna a pagina do dash board
    return render_template("dashboard.html") # Dashboard