from flask import Flask, jsonify,request
app1 = Flask(__name__)

#listar alumno
alumnos = [
    {"id" :1,"nombre":'Juan','edad': 18,'Nota1':15,'Nota2':18,'Nota3':17},
    {"id" :2,"nombre":'Rosa','edad':19,'Nota1':18,'Nota2':14,'Nota3':14},
    {"id" :3,"nombre":'Ronald','edad':20,'Nota1':12,'Nota2':11,'Nota3':15}
]
#GET
@app1.route('/alumnos', methods=['GET'])
def obtener_datos():
    return jsonify(alumnos)

#POST
@app1.route('/alumnos',methods=['POST'])
def agregar_datos():
    nuevo_alumno= request.get_json()
    nuevo_id = max([a['id'] for a in alumnos], default=0) + 1
    nuevo_alumno['id'] = nuevo_id
    alumnos.append(nuevo_alumno)
    return jsonify({"mensaje": "ALUMNO AGREGADO CORRECTAMENTE","alumno": nuevo_alumno}),201

#PUT 
@app1.route('/alumnos/<int:id>', methods=['PUT'])
def editar_alumno(id):
    for alumno in alumnos:
        if alumno['id'] == id:
            datos_actualizados = request.get_json()
            alumno['nombre'] = datos_actualizados.get('nombre',alumno['nombre'])
            alumno['edad'] = datos_actualizados.get('edad',alumno['edad'])
            alumno['Nota1'] = datos_actualizados.get('Nota1',alumno['Nota1'])
            alumno['Nota2'] = datos_actualizados.get('Nota2',alumno['Nota2'])
            alumno['Nota3'] = datos_actualizados.get('Nota3',alumno['Nota3'])
            return jsonify({
                "mensaje":f"Alumno con id {id} actualizados correctamente","alumno":alumno})
    return jsonify({"error":"Alumo no encontrado"}),404

#DELETE
@app1.route('/alumnos/<int:id>', methods=['DELETE'])
def eliminar_alumno(id):
    for alumno in alumnos:
        if alumno['id'] == id:
            alumnos.remove(alumno)
            return jsonify({"mensaje": f"Alumno con id {id} eliminado correctamente"})
    return jsonify({"error": "Alumno no encontrado"}),404

def calcular_promedio(alumno):
    return (alumno["Nota1"] + alumno["Nota2"]+ alumno["Nota3"])/3

@app1.route('/alumnos/mejor_promedio',methods=['GET'])
def prom_alumno():
    if not alumnos:
        return jsonify({"error": "No hay alumnos"}),404
    mejor = max(alumnos, key=calcular_promedio)
    promedio = calcular_promedio(mejor)
    return jsonify({"mejor_alumno": mejor,"promedio":promedio})

if __name__ == '__main__':
    app1.run(debug=True)
    
