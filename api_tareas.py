from flask import Flask,request,jsonify
app4 = Flask(__name__)
tareas = [
    {"id": 1,"nombre": "Matematica","estado":"Completado"},
    {"id": 2,"nombre": "Comunicacion","estado":"Incompleto"},
    {"id": 3,"nombre": "Ciencias","estado":"Pendiente"}
]
@app4.route("/tareas", methods=['GET'])
def obtener_datos():
    return jsonify(tareas)
@app4.route("/tareas", methods=['POST'])
def agregar_tarea():
    nueva_tarea = request.get_json()
    nuevo_id = max([a['id'] for a in tareas], default=0) + 1
    nueva_tarea['id'] = nuevo_id
    tareas.append(nueva_tarea)
    return jsonify({"mensaje": "Tarea agregado correctamente", "producto": nueva_tarea}),201

@app4.route('/tareas/<int:id>',methods=['DELETE'])
def eliminar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tareas.remove(tarea)
            return jsonify({"mensaje": f"Tarea con id {id} eliminado correctamente"})
    return  jsonify({"error":"Tarea no encontrada"}),404
@app4.route('/tareas/<int:id>', methods=['PUT'])
def editar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea_actualizada = request.get_json()
            tarea['nombre'] = tarea_actualizada.get('nombre',tarea['nombre'])
            tarea['estado'] = tarea_actualizada.get('estado',tarea['estado'])
            return jsonify({
                "mensaje":f"Tarea con id {id} actualizado correctamente",
                "tarea": tarea
            })
    return jsonify({"error":"Tarea no encontrada"}),404
if __name__ == '__main__':
    app4.run(debug=True,port=5001)