from flask import Flask,request,jsonify
api_animales = Flask(__name__)
animales = [
    {"id":1,"nombre":"docki","raza":"chitsu"},
    {"id":2,"nombre":"sparcki","raza":"Rodwailer"}
]
@api_animales.route('/')
def inicio():
    return 'Api de Animales'

@api_animales.route('/animales',methods=['GET'])
def obtener_animales():
    
    return jsonify(animales)

@api_animales.route('/animales/<int:id>', methods=['GET'])
def obtener_id(id):
    
    for animal in animales:
        if animal['id'] == id:
            return jsonify(animal)
    return jsonify({'mensaje':'Animal no a sido encontrado'}),404

@api_animales.route('/animales', methods=['POST'])
def agregar_animal():
    nuevo_animal = request.get_json()
    nuevo_id = max([e['id']for e in animales], default=0)+ 1
    nuevo_animal['id'] = nuevo_id
    animales.append(nuevo_animal)
    return jsonify({'mensaje':'Animal agregado correctamente','animal':nuevo_animal}),201

@api_animales.route('/animales/<int:id>', methods=['PUT'])
def actualizar_animal(id):
    for animal in animales:
        if animal['id'] == id:
            animal_actualizado = request.get_json()
            animal['nombre'] = animal_actualizado.get('nombre', animal['nombre'])
            animal['raza'] = animal_actualizado.get('raza', animal['raza'])
            return jsonify({'mensaje': 'Animal actualizado correctamente', 'animal': animal})
    return jsonify({'mensaje': 'Animal no encontrado'}), 404

@api_animales.route('/animales/<int:id>',methods=['DELETE'])
def eliminar_animal(id):
    for animal in animales:
        if animal['id'] == id:
            animales.remove(animal)
            return jsonify({'mensaje':f'Animal con el id {id} eliminado correctamente'})
    return jsonify({'mensaje':'Animal no encontrado'}),404

if __name__ == '__main__':
    api_animales.run(debug=True)
    
