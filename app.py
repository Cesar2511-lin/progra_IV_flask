# primer laboratorio de flask

from flask import Flask 
 
app = Flask(__name__) # constructor de servidor flask
 
@app.route('/') # ruta raiz
def inicio(): 
    return '<h1> Nombre propio Mi Flask </h1><p>Laboratorio S07b - Programación IV</p>' 
 
@app.route('/acerca') # ruta / acerca
def acerca(): 
    return '<h1>Acerca del estudiante</h1>' \
           '<p>quiero aprender a desarollar paginas interrativas</p>' \
           '<p>Nombre: Julio cesar Garcia s.</p>' 

@app.route('/contacto') # ruta / contacto
def contacto(): 
    return '<h1>Contacto</h1>' \
           '<p>Correo: julio.cesar.garcia.s@example.com</p>' \
           '<p>Teléfono: 123-456-7890</p>' 

if __name__ == '__main__': 
    app.run(debug=True) 