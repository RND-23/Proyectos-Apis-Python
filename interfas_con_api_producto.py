import tkinter as tk 
from tkinter import ttk, messagebox
import requests

url_api = "http://127.0.0.1:5000/prod"

def listar_productos():
    try:
        response = requests.get(url_api)
        data = response.json()
        for fila in tree.get_children():
            tree.delete(fila)
        
        for producto in data:
            tree.insert("","end", values=(
                producto["id"],
                producto["nombre"],
                producto["precio"],
                producto["stock"],
            ))
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo listar productos: {e}")

def ventana_editar():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Atencion","Seleccione un producto para editarlo")
        return
    
    valores = tree.item(selected[0])["values"]
    id_producto = valores[0]
    
    top = tk.Toplevel(root)
    top.title("Editar Producto")
    top.geometry("300x350")
    
    tk.Label(top, text="Nombre:").pack()
    nombre = tk.Entry(top)
    nombre.insert(0, valores[1])
    nombre.pack()
    
    tk.Label(top, text="Precio:").pack()
    precio = tk.Entry(top)
    precio.insert(0, valores[2])
    precio.pack()
    
    tk.Label(top, text="Stock:").pack()
    stock = tk.Entry(top)
    stock.insert(0, valores[3])
    stock.pack()
    
    def guardar_cambios():
        actualizado = {
            "nombre": nombre.get(),
            "precio": float(precio.get()),
            "stock": int(stock.get()),
        }
        try:
            requests.put(f"{url_api}/{id_producto}", json=actualizado)
            listar_productos()
            messagebox.showinfo("Exito","Alumno actualizado correctamente")
            top.destroy()
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo actualizar: {e}")
    tk.Button(top, text="Guardar cambios", command=guardar_cambios).pack(pady=10)

def eliminar_producto():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Atencion", "Seleccione un prodcuto para eliminar")
        return
    id_producto = tree.item(selected[0])["values"][0]
    try:
        requests.delete(f"{url_api}/{id_producto}")
        listar_productos()
        messagebox.showinfo("exito", "PRODUCTO ELIMINADO CORRECTAMENTE")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar: {e}")    


def ventana_agregar():
    top = tk.Toplevel(root)
    top.title("Agregar Alumno")
    top.geometry("300x350")
    
    tk.Label(top,text="Nombre:").pack()
    nombre = tk.Entry(top)
    nombre.pack()
    
    tk.Label(top,text="Precio:").pack()
    precio = tk.Entry(top)
    precio.pack()
    
    tk.Label(top,text="Stock:").pack()
    stock = tk.Entry(top)
    stock.pack()
    
    def guardar():
        nuevo = {
            "nombre": nombre.get(),
            "precio": float(precio.get()),
            "stock": int(stock.get()),
        }
        try:
            requests.post(url_api, json=nuevo)
            listar_productos()
            messagebox.showinfo("Exito","Productos agregado correctamente")
            top.destroy()
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo agregar: {e}")
    tk.Button(top, text="Guardar", command=guardar).pack(pady=10)

root = tk.Tk()
root.title("Gestion de productos")
root.geometry("650x400")

frame = tk.Frame(root)
frame.pack(pady=20)

columns = ("ID","NOMBRE","PRECIO","STOCK")

tree = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack()

tk.Button(root, text="Listar Productos", command=listar_productos).pack(pady=5)
tk.Button(root, text="Agregar Productos", command=ventana_agregar).pack(pady=5)
tk.Button(root, text="Editar Productos", command=ventana_editar).pack(pady=5)
tk.Button(root, text="Eliminar Productos", command=eliminar_producto).pack(pady=5)

listar_productos()
root.mainloop()
