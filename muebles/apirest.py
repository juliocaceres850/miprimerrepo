from flask import Flask, jsonify, request

app = Flask(__name__)

# Esto es un array con mis elementos a obtener
# datos es una referencia del tipo array, comienza con corchetes y dentros de los corhetes vamos agregar objetos seguidos de comas
# los objestos se encierran dentro de llaves cada uno de los objetos puede tener x cantidad de atributos, 
# # el atributo de los objetos de array datos es nombre, y id
datos = [
    {"id": 1, "nombre": "Boca Juniors"},
    {"id": 2, "nombre": "Xeneize"}
]

#Falta crear el array de Muebles
muebles = [
    {"id": 1, "material": "melamina", "lustrado": True, "puertas": 4, "color": "rojo", "tipo": "ropero" },
    {"id": 2, "material": "mdf", "lustrado": False, "puertas": 2, "color": "megro", "tipo": "despensero" },
    {"id": 1, "material": "plastico", "lustrado": False, "puertas": 0, "color": "verde", "tipo": "silla" },
    {"id": 1, "material": "hierro", "lustrado": False, "puertas": 0, "color": "negro", "tipo": "mesa ratona" }
]
#Este es un Array de precios
precios = [
    {"id": 1, "mueble": "silla", "precio": "$4000"},
    {"id": 2, "mueble": "mesa", "precio": "$6000"}
]



#Path para obtener todos mis elementos
@app.route('/api/items', methods=['GET'])
def obtener_items():
    return jsonify({"items": datos})

#Path para obtener todos mis elementos
@app.route('/api/muebles/precios', methods=['GET'])
def obtener_muebles_precios():
    return jsonify({"Precios": precios})  

# se va a crear la ruta para nuestro array con objetos muebles
@app.route("/api/muebles", methods=['GET'] )
def obtener_muebles():
    return jsonify({"muebles": muebles})
# que es main?, es la funcion principal que tiene el servicio
if __name__ == '__main__':
    app.run(debug=True, port=5000)