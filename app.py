from flask import Flask, request, jsonify

app= Flask(__name__)

productos = [
    {"id": 1, "nombre": "Producto A", "precio": 100},
    {"id": 2, "nombre": "Producto B", "precio": 200}
]

@app.route('/productos',methods=['GET'])
def obtener_productos():
    return jsonify(productos)

@app.route('/productos',methods=['POST'])
def agregar_producto():
    nuevo_producto = request.get_json()
    nuevo_id = max([p['id'] for p in productos] , default=0) + 1
    nuevo_producto['id'] = nuevo_id
    productos.append(nuevo_producto)
    return jsonify({"mensaje": "PRODUCTO AGREGADO CORRECTAMENTE", 'producto': nuevo_producto}), 201

app.route('/productos/<int:id>',methods=['PUT'])
def actualizar_producto(id):
    for producto in productos:
        if producto['id'] == id:
            producto_actualizado = request.get_json()
            producto['nombre'] =  producto_actualizado.get('nombre',producto['nombre'])
            producto['precio'] =  producto_actualizado.get('precio',producto['precio'])
            return jsonify({'mensaje': 'PRODUCTO ACTUALIZADO CORRECTAMENTE', 'producto': producto})
    return jsonify({'mensaje': 'PRODUCTO NO ENCONTRADO'}), 404

app.route('/productos/<int:id>',methods=['DELETE'])
def eliminar_producto(id):
    for producto in productos:
        if producto['id'] == id:
            productos.remove(producto)
            return jsonify({'mensaje': 'PRODUCTO ELIMINADO CORRECTAMENTE'})
    return jsonify({'mensaje': 'PRODUCTO NO ENCONTRADO'}), 404

if __name__ == '__main__':
    app.run(debug=True)
    