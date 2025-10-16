from flask import Flask, jsonify,request
app3 = Flask(__name__)
prod = [
    {"id": 1, "nombre": "Laptop Lenovo", "precio": 3200.50, "stock": 10},
    {"id": 2, "nombre": "Mouse Logitech", "precio": 120.99, "stock": 50}
]
@app3.route('/prod', methods=['GET'])
def obtener_datos():
    return jsonify(prod)

@app3.route('/prod',methods=['POST'])
def agregar_productos():
    nuevo_producto = request.get_json()
    nuevo_id = max([a['id'] for a in prod], default=0) + 1
    nuevo_producto['id'] = nuevo_id
    prod.append(nuevo_producto)
    return jsonify({"mensaje": "Producto agregado correctamente", "producto": nuevo_producto}),201

@app3.route('/prod/<int:id>',methods=['DELETE'])
def eliminar_producto(id):
    for producto in prod:
        if producto['id'] == id:
            prod.remove(producto)
            return jsonify({"mensaje": f"Producto con id {id} eliminado correctamente"})
    return jsonify({"error":"Producto no encontrado"}),404

@app3.route('/prod/<int:id>',methods=['PUT'])
def editar_producto(id):
    for producto in prod:
        if producto['id'] == id:
            producto_actualizado = request.get_json()
            producto['nombre'] = producto_actualizado.get('nombre',producto['nombre'])
            producto['precio'] = producto_actualizado.get('precio',producto['precio'])
            producto['stock'] = producto_actualizado.get('stock',producto['stock'])
            return jsonify({
                "mensaje":f"Producto con id {id} actualizado correctamente",
                "producto" : producto
            })
    return jsonify({"error":"Producto no encontrado"}),404
if __name__ == '__main__':
    app3.run(debug=True)