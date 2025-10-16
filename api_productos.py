from flask import Flask, jsonify,request
app = Flask(__name__)

#lista 
productos = [
    {"id" : 1 , "nombre" : "Collar", "Precio":1500},
    {"id" : 2 , "nombre" : "Cadena", "Precio":1800},
    {"id" : 3 , "nombre" : "Arete", "Precio":200},
    {"id" : 4 , "nombre" : "Anillo", "Precio":20.00}
]

@app.route('/productos', methods=['GET'])
def obtener_datos():
    return jsonify(productos)


@app.route('/productos',methods=['POST'])
def agregar_producto():
    nuevo_producto = request.get_json()
    
    productos.append(nuevo_producto)
    
    return jsonify({"mensaje": "Producto agregado correctamente", "producto": nuevo_producto})

@app.route('/productos/<int:id>',methods=['DELETE'])
def eliminar_producto(id):
    for producto in productos:
        if producto['id'] == id:
            productos.remove(producto)
            return jsonify({"mensaje": f"Producto con id {id} eliminado correctamente"})
    return jsonify({"error":"Producto no encontrado"}),404

@app.route('/productos/<int:id>', methods=['PUT'])
def editar_producto(id):
    for producto in productos:
        if producto['id'] ==  id:
            datos_actualizados  = request.get_json()
            producto['nombre'] = datos_actualizados.get('nombre',producto['nombre'])
            producto['Precio'] = datos_actualizados.get('Precio',producto['Precio'])
            return jsonify({
                "mensaje":f"Producto con id {id} actualizado correctamente",
                "producto" : producto
            })
    return jsonify({"error":"Producto no encontrado"}),404
if __name__ == '__main__':
    app.run(debug=True)


    
