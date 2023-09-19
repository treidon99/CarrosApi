from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])

def carros():
     name = request.headers.get('User-name')
     method = request.method

     if method == "GET":

        return f'Tu nombre es {name}'
     
     elif method == "POST":
         
        data = request.get_json()
        nombre_archivo = "log.txt"

        with open(nombre_archivo, 'a+') as archivo:
            archivo.write(data.get("nombre")+'\n')

        return f'El usiario fue agregado'

if __name__ == '__main__':
    app.run(debug=True)