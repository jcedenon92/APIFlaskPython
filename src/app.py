from flask import Flask, json, request, jsonify, Response
import joblib
import numpy as np
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

#se carga los modelos entrenados y se almacena en una variable
#respectiva para prediccion de cabeza, talla y peso
model1 = joblib.load(open("src/modelo_cabeza.pkl", "rb"))
model2 = joblib.load(open("src/modelo_talla.pkl", "rb"))
model3 = joblib.load(open("src/modelo_peso.pkl", "rb"))

#funcion para hacer el llamado al modelo, con el parametro de mes para su uso
def modelCall(modelo,mes):
    x = modelo.predict(np.array(mes).reshape(1, 1))
    #print(x)
    return x

#MES
#POST
@app.route('/prediccion', methods=['GET','POST'])
def prediccionCabeza():
    parametro = request.json['parametro']
    mes = request.json['mes']    
    if(parametro == "cabeza"):
        if( mes > 0 and mes <= 216):
            resultado = modelCall(model1, mes)
            lista = resultado.tolist()
            js = json.dumps(lista)
            response = {"prediccion": js}
            #print(resultado)
            return response
        else:
            return jsonify({"message": "Ingrese un numero entre 1 y 216"})
    elif(parametro == "talla"):
        if( mes > 0 and mes <= 216):
            resultado = modelCall(model2, mes)
            lista = resultado.tolist()
            js = json.dumps(lista)
            response = {"prediccion": js}
            #print(resultado)
            return response
        else:
            return jsonify({"message": "Ingrese un numero entre 1 y 216"})
    elif(parametro == "peso"):
        if( mes > 0 and mes <= 216):
            resultado = modelCall(model3, mes)
            lista = resultado.tolist()
            js = json.dumps(lista)
            response = {"prediccion": js}
            #print(resultado)
            return response
        else:
            return jsonify({"message": "Ingrese un numero entre 1 y 216"})
    else:
        return jsonify({"message": "Opcion invalida, elija cualquiera de estas tres opciones: (peso, talla, perimetro craneal) para realizar la prediccion" })
#POST
#@app.route('/mesTalla', methods=['POST'])
# def prediccionTalla():


#POST
#@app.route('/mesPeso', methods=['POST'])
# def prediccionPeso():

if __name__ == "__main__":
    app.run(debug=True)