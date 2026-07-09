from flask import Flask

app = Flask(__name__) # este es el constructor del servidos flask

@app.route("/") # esta es la raiz de la web
def inicio():
    return "<h1> Hola estudiantes </h1>" \
           "<p> primera web usando flask </p>"
#programa principal utiliza el servidor
app.run()