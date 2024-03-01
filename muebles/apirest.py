from flask import Flask, jsonify, request

app = Flask(__name__)

# Esto es un array con mis elementos a obtener
datos = [
    {"id": 1, "nombre": "Boca Juniors"},
    {"id": 2, "nombre": "Xeneize"}
]

#Falta crear el array de Muebles

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)