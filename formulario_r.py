import tkinter as tk
from tkinter import messagebox, ttk

ventana = tk.Tk()
ventana.title("REGISTRO DE ANIMALES")
ventana.geometry("500x400")
ventana.resizable(False, False)
# Lista de animales
animales = []
# Funciones
def actualizar_tabla():
    """Actualiza los datos en la tabla."""
    for fila in tabla.get_children():
        tabla.delete(fila)
    for i, animal in enumerate(animales, start=1):
        tabla.insert("", "end", values=(i, animal["nombre"], animal["rasa"]))
def limpiar_campos():
    """Limpia las entradas de texto."""
    camp_nombre.delete(0, tk.END)
    camp_rasa.delete(0, tk.END)
def agregar():
    """Agrega un nuevo animal a la lista."""
    nombre = camp_nombre.get().strip()
    rasa = camp_rasa.get().strip()
    if nombre == "" or rasa == "":
        messagebox.showwarning("Atención", "Completa todos los campos")
        return
    animales.append({"nombre": nombre, "rasa": rasa})
    actualizar_tabla()
    limpiar_campos()
    messagebox.showinfo("Éxito", f"Animal registrado:\nNombre: {nombre}\nRaza: {rasa}")
def seleccionar_animal(event):
    """Carga los datos del animal seleccionado en las entradas."""
    seleccion = tabla.selection()
    if seleccion:
        item = tabla.item(seleccion[0])
        valores = item["values"]
        limpiar_campos()
        camp_nombre.insert(0, valores[1])
        camp_rasa.insert(0, valores[2])
def modificar():
    """Modifica el animal seleccionado."""
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Error", "Selecciona un animal para modificar")
        return
    nombre = camp_nombre.get().strip()
    rasa = camp_rasa.get().strip()
    if nombre == "" or rasa == "":
        messagebox.showerror("Error", "Completa todos los campos para modificar")
        return
    index = tabla.index(seleccion[0])
    animales[index] = {"nombre": nombre, "rasa": rasa}
    actualizar_tabla()
    limpiar_campos()
    messagebox.showinfo("Modificación", "Animal modificado correctamente")
def eliminar():
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Error", "Selecciona un animal para eliminar")
        return
    index = tabla.index(seleccion[0])
    animal = animales[index]
    confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar animal?\nNombre: {animal['nombre']}\nRaza: {animal['rasa']}")
    if confirmar:
        animales.pop(index)
        actualizar_tabla()
        limpiar_campos()
        messagebox.showinfo("Eliminado", "Animal eliminado correctamente")
# Widgets del formulario
frm_form = tk.Frame(ventana)
frm_form.pack(pady=10)
lbl_nombre = tk.Label(frm_form, text="NOMBRE:")
lbl_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
camp_nombre = tk.Entry(frm_form, width=25)
camp_nombre.grid(row=0, column=1, padx=5, pady=5)
lbl_rasa = tk.Label(frm_form, text="RAZA:")
lbl_rasa.grid(row=1, column=0, padx=5, pady=5, sticky="e")
camp_rasa = tk.Entry(frm_form, width=25)
camp_rasa.grid(row=1, column=1, padx=5, pady=5)
# Botones
frm_botones = tk.Frame(ventana)
frm_botones.pack(pady=5)
btn_agregar = tk.Button(frm_botones, text="Agregar", command=agregar, width=12, bg="#4CAF50", fg="white")
btn_agregar.grid(row=0, column=0, padx=5)
btn_modificar = tk.Button(frm_botones, text="Modificar", command=modificar, width=12, bg="#2196F3", fg="white")
btn_modificar.grid(row=0, column=1, padx=5)
btn_eliminar = tk.Button(frm_botones, text="Eliminar", command=eliminar, width=12, bg="#f44336", fg="white")
btn_eliminar.grid(row=0, column=2, padx=5)
btn_limpiar = tk.Button(frm_botones, text="Limpiar", command=limpiar_campos, width=12, bg="#9E9E9E", fg="white")
btn_limpiar.grid(row=0, column=3, padx=5)
# Tabla (Treeview)
tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Raza"), show="headings", height=10)
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Raza", text="Raza")
tabla.column("ID", width=50, anchor="center")
tabla.column("Nombre", width=150)
tabla.column("Raza", width=150)
tabla.pack(pady=10, fill="x")
tabla.bind("<ButtonRelease-1>", seleccionar_animal)


ventana.mainloop()
