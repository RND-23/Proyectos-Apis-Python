from flask import Flask, request, jsonify
app1 = Flask(__name__)
empleados = [
    {"id": 1, "nombre": "Empleado A", "puesto": "Desarrollador", "salario": 3000},
    {"id": 2, "nombre": "Empleado B", "puesto": "Diseñador", "salario": 2500}
]
#inicio
@app1.route('/')
def inicio():
    return "API DE EMPLEADOS"

#get todos los empleados
@app1.route('/empleados', methods=['GET'])
def obtener_empleados():
    return jsonify(empleados)

#obtener por id
@app1.route('/empleados/<int:id>', methods=['GET'])
def obtener_empleados_por_id(id):
    for empleado in empleados:
        if empleado['id'] == id:
            return jsonify(empleado)
    return jsonify({'mensaje': 'EMPLEADO NO SE A ENCONTRADO'}), 404

#agregar
@app1.route('/empleados',methods=['POST'])
def agregar_empleado():
    nuevo_empleado = request.get_json()
    nuevo_id = max([e['id'] for e in empleados], default=0) + 1
    nuevo_empleado['id'] = nuevo_id
    empleados.append(nuevo_empleado)
    return jsonify({"mensaje": "EMPLEADO AGREGADO CORRECTAMENTE", 'empleado': nuevo_empleado}), 201

#modificar
@app1.route('/empleados/<int:id>',methods=['PUT'])
def actualizar_empleado(id):
    for empleado in empleados:
        if empleado['id'] == id:
            empleado_actualizado = request.get_json()
            empleado['nombre'] =  empleado_actualizado.get('nombre',empleado['nombre'])
            empleado['puesto'] =  empleado_actualizado.get('puesto',empleado['puesto'])
            empleado['salario'] =  empleado_actualizado.get('salario',empleado['salario'])
            return jsonify({'mensaje': 'EMPLEADO ACTUALIZADO CORRECTAMENTE', 'empleado': empleado})
    return jsonify({'mensaje': 'EMPLEADO NO ENCONTRADO'}), 404

#eliminar
@app1.route('/empleados/<int:id>',methods=['DELETE'])
def eliminar_empleado(id):
    for empleado in empleados:
        if empleado['id'] == id:
            empleados.remove(empleado)
            return jsonify({'mensaje': f'EMPLEADO CON EL ID {id} ELIMINADO CORRECTAMENTE'})
    return jsonify({'mensaje': 'EMPLEADO NO ENCONTRADO'}), 404

if __name__ == '__main__':
    app1.run(debug=True)
