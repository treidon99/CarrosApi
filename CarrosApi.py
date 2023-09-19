from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])

def carros():
     name = request.headers.get('User-name')
     method = request.method
     nombre_archivo = "log.txt"

     if method == "GET":
        usuarios = []
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                usuarios.append({"nombre" : linea})

        return 
     
     elif method == "POST":
         
        data = request.get_json()

        with open(nombre_archivo, 'a+') as archivo:
            archivo.write(data.get("nombre")+'\n')

        return f'El usiario fue agregado'

if __name__ == '__main__':
    app.run(debug=True)