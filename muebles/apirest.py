from flask import Flask, jsonify, request

app = Flask(__name__)

# Esto es un array con mis elementos a obtener
# datos es una referencia del tipo array, comienza con corchetes y dentros de los corhetes vamos agregar objetos seguidos de comas
# los objestos se encierran dentro de llaves cada uno de los objetos puede tener x cantidad de atributos, 
# # el atributo de los objetos de array datos es nombre, y "id"
datos = [
    {"id": 1, "nombre": "Boca Juniors"},
    {"id": 2, "nombre": "Xeneize"}
]

#Falta crear el array de Muebles
muebles = [
    {"id": 1, "material": "melamina", "lustrado": True, "puertas": 4, "color": "rojo", "tipo": "ropero" },
    {"id": 2, "material": "mdf", "lustrado": False, "puertas": 2, "color": "megro", "tipo": "despensero" },
    {"id": 3, "material": "plastico", "lustrado": False, "puertas": 0, "color": "verde", "tipo": "silla" },
    {"id": 4, "material": "hierro", "lustrado": False, "puertas": 0, "color": "negro", "tipo": "mesa ratona" }
]
#Este es un Array de precios
precios = [
    {"id": 1, "mueble": "silla", "precio": "$4000"},
    {"id": 2, "mueble": "mesa", "precio": "$6000"}
]
#este es un array de electrodomesticos
electrodomesticos = [
    {"id": 1, "material": "aluminio", "antioxido": True, "puerta": "vidrio", "color": "negro", "tipo": "cocina"},
    {"id": 2, "material": "aluminio", "antioxido": False, "pulgadas": 50, "color": "negro", "tipo": "smart tv"},
    {"id": 3, "material": "aluminio", "puerta": "vidrio", "antioxido": False, "color": "gris", "tipo": "pava"}
]
# este es un array de horarios
horarios = [
    {"id": 1, "dias": "lunes a viernes"},
    {"id": 2, "horarios": " de 08 hasta 20 hs"}
]

#este es un array de horarios
@app.route('/api/muebles/dias/horarios', methods=['GET'])
def obtener_dias_horarios():
    return jsonify({"horarios": horarios})


#Path para obtener todos mis elementos
@app.route('/api/items', methods=['GET'])
def obtener_items():
    return jsonify({"items": datos})

#Path para obtener todos mis elementos
@app.route('/api/muebles/precios', methods=['GET'])
def obtener_muebles_precios():
    return jsonify({"Precios": precios})  

#agregamos array de electrodomesticos
# Cambia la ruta de la segunda función a "/api/electrodomesticos"
@app.route('/api/electrodomesticos', methods=['GET'])
def obtener_electrodomesticos():
    return jsonify({"Electrodomesticos": electrodomesticos})


# se va a crear la ruta para nuestro array con objetos muebles
@app.route("/api/muebles", methods=['GET'] )
def obtener_muebles():
    return jsonify({"muebles": muebles})

# que es main?, es la funcion principal que tiene el servicio
if __name__ == '__main__':
    app.run(debug=True, port=5000)