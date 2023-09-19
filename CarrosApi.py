from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])

def carros():
     name = request.headers.get('User-name')
     method = request.method

     if method == "GET":
        return f'Tu nombre es {name}'
     elif method == "POST":
         data = request.get()
         print("Hemos reciido u usario")
         print("Su nombre es ", data.get("nombre"))

if __name__ == '__main__':
    app.run(debug=True)