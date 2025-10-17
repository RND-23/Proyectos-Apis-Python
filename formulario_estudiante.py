import tkinter as tk
from tkinter import messagebox, ttk

ventana = tk.Tk()
ventana.title("FORMULARIO DE ESTUDIANTE")
ventana.geometry("900x600")

# lista para guardar los datos
estudiantes = []

lbl_nombre = tk.Label(ventana, text="NOMBRE DE ESTUDIANTE")
lbl_nombre.pack()
cam_nombre = tk.Entry(ventana)
cam_nombre.pack()

lbl_edad = tk.Label(ventana, text="EDAD DE ESTUDIANTE")
lbl_edad.pack()
cam_edad = tk.Entry(ventana)
cam_edad.pack()

lbl_carrera = tk.Label(ventana, text="CARRERA DE ESTUDIANTE")
lbl_carrera.pack()
cam_carrera = tk.Entry(ventana)
cam_carrera.pack()


#Tabla para mostrar los estudiantes
tabla = ttk.Treeview(ventana, columns=("nombre", "edad", "carrera"), show="headings")
tabla.heading("nombre", text="Nombre")
tabla.heading("edad", text="Edad")
tabla.heading("carrera", text="Carrera")
tabla.pack(pady=10)


#FUNCIONES
def agregar():
    nombre = cam_nombre.get().strip()
    edad = cam_edad.get().strip()
    carrera = cam_carrera.get().strip()
    if nombre == "" or edad == "" or carrera == "":
        messagebox.showwarning('Error', 'COMPLETE TODOS LOS CAMPOS')
        return
    
    estudiantes.append({"nombre": nombre, "edad": edad, "carrera": carrera})
    tabla.insert("", tk.END, values=(nombre, edad, carrera))
    messagebox.showinfo('Registrado', f'Estudiante {nombre}, Edad {edad}, Carrera {carrera}')
    limpiar()


def modificar():
    nombre = cam_nombre.get().strip()
    edad = cam_edad.get().strip()
    carrera = cam_carrera.get().strip()
    if nombre == "" or edad == "" or carrera == "":
        messagebox.showwarning('Error', 'COMPLETE TODOS LOS CAMPOS')
        return
    
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            estudiante["edad"] = edad
            estudiante["carrera"] = carrera
            actualizar_tabla()
            messagebox.showinfo("Éxito", f"Se modificó el estudiante {nombre}")
            limpiar()
            return
    
    messagebox.showwarning("Error", "NO SE ENCONTRÓ NINGÚN ESTUDIANTE CON ESE NOMBRE")


def eliminar():
    nombre = cam_nombre.get().strip()
    if nombre == "":
        messagebox.showwarning('Error', 'INGRESE EL NOMBRE DEL ESTUDIANTE A ELIMINAR')
        return
    
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            estudiantes.remove(estudiante)
            actualizar_tabla()
            messagebox.showinfo("Eliminado", f"EL ESTUDIANTE {nombre} FUE ELIMINADO CORRECTAMENTE")
            limpiar()
            return

    messagebox.showwarning("Error", "NO SE ENCONTRÓ NINGÚN ESTUDIANTE CON ESE NOMBRE")


def actualizar_tabla():
    # Limpia y vuelve a llenarla
    for fila in tabla.get_children():
        tabla.delete(fila)
    for est in estudiantes:
        tabla.insert("", tk.END, values=(est["nombre"], est["edad"], est["carrera"]))


def limpiar():
    cam_nombre.delete(0, tk.END)
    cam_edad.delete(0, tk.END)
    cam_carrera.delete(0, tk.END)


#BOTONES
tk.Button(ventana, text="REGISTRAR", command=agregar, bg="#00bfff", fg="white", width=20).pack(pady=3)
tk.Button(ventana, text="EDITAR", command=modificar, bg="#ffa500", fg="white", width=20).pack(pady=3)
tk.Button(ventana, text="ELIMINAR", command=eliminar, bg="#ff6347", fg="white", width=20).pack(pady=3)

ventana.mainloop()
