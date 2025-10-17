#creacion de apis de vehiculos
from flask import Flask, request,jsonify
api_vehiculos = Flask(__name__)
#lista de vehiculos
vehiculos = [
    {"id":1,"marca":"Toyota","precio":1545.00,"año":"20/10/1998"},
    {"id":2,"marca":"Nissan","precio":9745.00,"año":"16/05/2015"},
    {"id":3,"marca":"Corola","precio":4565.00,"año":"18/12/2000"}
]

@api_vehiculos.route("/")
def inicio():
    return 'APIS CON VEHICULOS'

#GET
@api_vehiculos.route("/vehiculos",methods=['GET'])
def obtener_vehiculos():
   return jsonify(vehiculos)

#get por id
@api_vehiculos.route("/vehiculos/<int:id>",methods=['GET'])
def obtener_id(id):
    for vehi in vehiculos:
        if vehi['id'] == id:
            return jsonify(vehi)
    return jsonify ({'mensaje': 'Vehiculo no a sido encontrado'}),404

#POST
@api_vehiculos.route("/vehiculos", methods=['POST'])
def agregar_vehiculos():
    nuevo_vehiculos = request.get_json()
    nuevo_id = max([e['id']for e in vehiculos],default=0) + 1
    nuevo_vehiculos['id'] = nuevo_id
    vehiculos.append(nuevo_vehiculos)
    return jsonify({'mensaje':'Vehiculo agregado correctamente','vehi': nuevo_vehiculos}),201

#PUT - EDITAR
@api_vehiculos.route("/vehiculos/<int:id>",methods=['PUT'])
def editar_vehiculo(id):
    for vehi in vehiculos:
        if vehi['id'] == id:
            vehiculo_actualizado = request.get_json()
            vehi['marca'] = vehiculo_actualizado.get('marca',vehi['marca'])
            vehi['precio'] = vehiculo_actualizado.get('precio',vehi['precio'])
            vehi['año'] = vehiculo_actualizado.get('año',vehi['año'])
            return jsonify({'mensaje':'Vehiculo modficado correctamente','vehi': vehi})
    return jsonify({'mensaje':'VEHICULO NO ENCOTRADO'}),404

#delete
@api_vehiculos.route("/vehiculos/<int:id>",methods=['DELETE'])
def eliminar_vehiculo(id):
    for vehi in vehiculos:
        if vehi['id'] == id:
            vehiculos.remove(vehi)
            return jsonify({'mensaje':f'Vehiculo con el id {id} eliminado correctamente'}) 
    return jsonify({'mensaje':'VEHICULO NO ENCOTRADO'}),404

#arrancamos el archivo
if __name__ == '__main__':
    api_vehiculos.run(debug=True)
    
