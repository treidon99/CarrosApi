from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])

def carros():
     
     nombre_archivo = "log.txt"
     name = request.headers.get('User-name')
     method = request.method

     if method == "GET":
        usuarios = []
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                cadena = linea
                cadena = cadena.split(",")
                usuarios.append({ "Marca" : cadena[0] })
                usuarios.append({ "Color" : cadena[1] })
                usuarios.append({ "Estado" : cadena[2] })

        return jsonify(usuarios)
     
     elif method == "POST":
         
        data = request.get_json()

        with open(nombre_archivo, 'a+') as archivo:
            archivo.write(data.get("Marca")+','+data.get("Color")+','+data.get("Estado")+'\n')

        return f'El carro y sus caracteristicas fueron agregadas'

if __name__ == '__main__':
    app.run(debug=True)