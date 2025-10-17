from flask import Flask,request,jsonify
evento = Flask(__name__)

eventos = [
    {"id":1,"nombre":"Fiesta","fecha":"22/10/25"}
]

@evento.route("/")
def inicio():
    return 'Api de Eventos'

@evento.route("/eventos", methods=['GET'])
def obtener_datos():
    return jsonify(eventos)

@evento.route("/eventos/<int:id>",methods=['GET'])
def obtener_id(id):
    for evento in eventos:
        if evento['id'] == id:
            return jsonify(evento)
    return jsonify({'mensaje':'Evento no se a encontrado'}),404

@evento.route("/eventos",methods=['POST'])
def agregar_evento():
    nuevo_evento = request.get_json()
    nuevo_id = max([e['id'] for e in eventos], default=0)+ 1
    nuevo_evento['id'] = nuevo_id
    eventos.append(nuevo_evento)
    return jsonify({'mensaje':'Evento agregado correctamente', 'evento':nuevo_evento}),201

@evento.route('/eventos/<int:id>',methods=['PUT'])
def modificar_evento(id):
    for evento in eventos:
        if evento['id'] == id:
            evento_actualizado = request.get_json()
            evento['nombre'] = evento_actualizado.get('nombre', evento['nombre'])
            evento['fecha'] = evento_actualizado.get('fecha', evento['fecha'])
            return jsonify({'mensaje': f'Evento con el id {id} a sido modificado correctamente'})
    return jsonify({'mensaje':'Evento no encontrado'}),404

@evento.route('/eventos/<int:id>',methods=['DELETE'])
def eliminar_evento(id):
    for evento in eventos:
        if evento['id'] == id:
            eventos.remove(evento)
            return jsonify({'mensaje': f'Evento con el id {id} a sido eliminado correctamente'})
    return jsonify({'mensaje':'Evento no encontrado'}),404

if __name__ == '__main__':
    evento.run(debug=True)
