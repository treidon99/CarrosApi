from flask import Flask, request, jsonify

app = Flask(__name__) #Crea una instancia de la aplicacion flask

@app.route('/', methods = ["GET","POST"]) #Definicion de ruta y metodos a utilizar

def carros(): #Funcion a manejar
     
     nombre_archivo = "log.txt" #Nombre del archivo de texto donde se guardara lo enviado por la solicitud POST
     method = request.method #Obtencion del metodo utilizado

     if method == "GET": 
        Atributos = [] #Arreglo de los atributos del carro
        with open(nombre_archivo, 'r') as archivo: #Lectura del archivo de texto
            for linea in archivo: #ciclo por cada linea del archivo de texto
                #conversion de cada linea en cadena y remocion del ultimo caracter ya que trae el caracter de espaciado
                cadena = linea
                cadena = cadena.split(",")
                ultimo_elemento = cadena[-1]
                cadena[-1] = ultimo_elemento[:-1]
                # Se agregan los atributos de la cadena a la lista de atributos
                Atributos.append({ "Marca" : cadena[0],"Color" : cadena[1],"Estado" : cadena[2] })

        return jsonify(Atributos) #Retrono del metodo GET, para mostrar los atributos en Json
     
     elif method == "POST": 
         
        data = request.get_json() #Obtencion de la data enviada en formato Json del Poastman

        with open(nombre_archivo, 'a+') as archivo: #Crea un archivo si no esta creado y agrega la informacion del Json
            archivo.write(data.get("Marca")+','+data.get("Color")+','+data.get("Estado")+'\n') #Data que se esta obteniendo del jason por categoria, separada por una coma

        return f'El carro y sus caracteristicas fueron agregadas' #Funcion de retorno del metodo POST

#Ejecuta la aplicacion en el puerto 5000

if __name__ == '__main__':
    app.run(debug=True)