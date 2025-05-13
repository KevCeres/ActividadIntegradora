from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Conectar a MongoDB local (localhost)
client = MongoClient('mongodb://localhost:27017/')
db = client['mi_base_de_datos']  # Puedes cambiar el nombre de la base de datos
collection = db['mi_coleccion']  # Puedes cambiar el nombre de la colección

@app.route('/agregar', methods=['POST'])
def agregar_dato():
    # Obtener datos de la solicitud
    data = request.json
    # Insertar en MongoDB
    collection.insert_one(data)
    return jsonify({"mensaje": "Datos guardados exitosamente!"}), 201

@app.route('/ver', methods=['GET'])
def ver_datos():
    # Obtener todos los documentos de la colección
    datos = collection.find()
    # Convertir los documentos a una lista
    result = [str(dato) for dato in datos]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
