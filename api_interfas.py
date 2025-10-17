import tkinter as tk
from tkinter import messagebox,ttk
import requests

url_api = "http://127.0.0.1:5000/animales"

def actualizar_tabla():
    try:
        response = requests.get(url_api)
        animales = response.json()
        
        for fila in tabla.get_children():
            tabla.delete(fila)
        for animal in animales:
            tabla.insert("", tk.END, values=(animal["id"], animal["nombre"],animal["raza"]))
    except Exception as e:
        messagebox.showerror("Error",f"No se pudo conectar la Api:{e}")

def agregar():
    nombre = cam_nombre.get().strip()
    raza = cam_raza.get().strip()
    if nombre == "" or raza == "":
        messagebox.showwarning('Error', 'COMPLETE TODOS LOS CAMPOS')
        return
    #diccionario - se manda en formato json
    datos = {"nombre":nombre,"raza":raza}
    
    try:
        response = requests.post(url_api, json=datos)
        if response.status_code == 201:
            messagebox.showinfo("Exito","Animal agregado correctamente")
            actualizar_tabla()
            limpiar()
        else:
            messagebox.showerror("Error", f"No se puedo registrar: {response.text}")
    except Exception as e:
        messagebox.showerror("Error",f"Error al conectar con la Api: {e}")
        
def modificar():
    id_animal = cam_id.get().strip()
    if id_animal == "":
        messagebox.showwarning("Error","Ingrese el id del animal a modificar")
        return
    nombre = cam_nombre.get().strip()
    raza = cam_raza.get().strip()
    if nombre == "" or raza == "":
        messagebox.showwarning('Error', 'COMPLETE TODOS LOS CAMPOS')
        return
    
    datos = {"nombre":nombre,"raza":raza}
    
    try:
        response = requests.put(f"{url_api}/{id_animal}",json=datos)
        if response.status_code == 200:
            messagebox.showinfo("Exito","Animal modificado correctamente")
            actualizar_tabla()
            limpiar()
        else:
            messagebox.showerror("Error", f"No se puedo modificar: {response.text}")
    except Exception as e:
        messagebox.showerror("Error",f"Error al conectar con la Api: {e}")
def eliminar():
    id_animal = cam_id.get().strip()
    if id_animal == "":
        messagebox.showwarning("Error", "Ingrese el id del animal a eliminar")
        return
    try:
        response = requests.delete(f"{url_api}/{id_animal}")
        if response.status_code == 200:
            messagebox.showinfo("EXITO","Animal eliminado correctamente")
            actualizar_tabla()
            limpiar()
        else:
            messagebox.showerror("Error",f"No se puedo eliminar:{response.text}")
    except Exception as e:
        messagebox.showerror("Error",f"Error al conectar con la Api: {e}")
        

def limpiar():
    cam_id.delete(0, tk.END)
    cam_nombre.delete(0, tk.END)
    cam_raza.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("FORMULARIO DE ANIMALES")
ventana.geometry("900x600")

lbl_id = tk.Label(ventana, text="ID DEL ANIMAL")
lbl_id.pack()
cam_id = tk.Entry(ventana)
cam_id.pack()

lbl_nombre= tk.Label(ventana, text="NOMBRE DEL ANIMAL")
lbl_nombre.pack()
cam_nombre = tk.Entry(ventana)
cam_nombre.pack()

lbl_raza = tk.Label(ventana, text="RAZA DEL ANIMAL")
lbl_raza.pack()
cam_raza = tk.Entry(ventana)
cam_raza.pack()

#Tabla para mostrar los estudiantes
tabla = ttk.Treeview(ventana, columns=("id","nombre", "raza"), show="headings")
tabla.heading("id", text="ID")
tabla.heading("nombre", text="Nombre")
tabla.heading("raza", text="Raza")
tabla.pack(pady=10)

tk.Button(ventana, text="LISTAR", command=actualizar_tabla, bg="#808080", fg="white", width=20).pack(pady=3)
tk.Button(ventana, text="REGISTRAR", command=agregar, bg="#00bfff", fg="white", width=20).pack(pady=3)
tk.Button(ventana, text="EDITAR", command=modificar, bg="#ffa500", fg="white", width=20).pack(pady=3)
tk.Button(ventana, text="ELIMINAR", command=eliminar, bg="#ff6347", fg="white", width=20).pack(pady=3)
tk.Button(ventana, text="LIMPIAR CAMPOS", command=limpiar, bg="#808000", fg="white", width=20).pack(pady=3)

ventana.mainloop()