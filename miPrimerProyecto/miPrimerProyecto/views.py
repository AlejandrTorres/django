from django.http import HttpResponse
from django.template import loader
import datetime
def saludar(request):
    return HttpResponse("Hola Mundo")

def tareas(request):
    Tareas=["Aprender","HTML","CSS","PRACTICA DJANGO","APRENDER DJANGO"]
    
    doc_externo=loader.get_template("primeraPlantilla.html")
    documento=doc_externo.render({"Listado":Tareas})
    return HttpResponse(documento)

def fecha(request):
    fechaActual=datetime.datetime.now()
    documento="""<HTML>
                    <HEAD> 
                        <TITLE>Estructura básica</TITLE>
                    </HEAD>
                    <BODY>
                        <h1> Usted inicio el  %s </h1>
                    </BODY>
                    </HTML>"""%fechaActual
    return HttpResponse(documento)
def games(request):
    año=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")

    fecha="%s/%s/%s a las %s " %(dia,mes,año,hora)

    doc_externo=loader.get_template("games.html")
    documento=doc_externo.render({"fecha": fecha})
    return HttpResponse(documento)
def musica(request):
    año=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")

    fecha="%s/%s/%s a las %s " %(dia,mes,año,hora)
    doc_externo=loader.get_template("musica.html")
    documento=doc_externo.render({"fecha": fecha})
    return HttpResponse(documento)
def tecno(request):
    año=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")

    fecha="%s/%s/%s a las %s " %(dia,mes,año,hora)
    doc_externo=loader.get_template("tecnologia.html")
    documento=doc_externo.render({"fecha": fecha})
    return HttpResponse(documento)

