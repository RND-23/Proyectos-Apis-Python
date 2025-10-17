import tkinter as tk
from tkinter import messagebox,ttk
import requests

url_api = "http://127.0.0.1:5000/eventos"

def actualizar_tabla():
    try:
        response = requests.get(url_api)
        eventos = response.json()
        
        for fila in tabla.get_children():
            tabla.delete(fila)
            
        for evento in eventos:
            tabla.insert("",tk.END, values=(evento["id"], evento['nombre'],evento['fecha']))
    except Exception as e:
        messagebox.showerror("Error",f"No se puedo conectar la APIS: {e}")
    
def agregar():
    nombre = cam_nombre.get().strip()
    fecha = cam_fecha.get().strip()
    if nombre == "" or fecha == "":
        messagebox.showwarning("Error", "Complete todos los campos")
        return

    datos = {"nombre":nombre,"fecha":fecha}
    
    try:
        response = requests.post(url_api,json=datos)
        if response.status_code == 201:
            messagebox.showinfo("Extio","Evento agregado correctamente")
            actualizar_tabla()
            limpiar()
        else:
            messagebox.showerror("Error",f"No se puedo registrar: {response.text}")
    except Exception as e:
        messagebox.showerror("Error",f"No se pudo conectar con la API: {e}")
  
def modificar():
    id_evento = cam_id.get().strip()
    if id_evento == "":
        messagebox.showwarning("Error", "Ingrese el id del evento a modificar")
        return
    nombre = cam_nombre.get().strip()
    fecha = cam_fecha.get().strip()
    if nombre == "" or fecha == "":
        messagebox.showwarning("Error", "Complete todos los campos")
        return
    datos = {"nombre":nombre,"fecha":fecha}
    try:
        response = requests.put(f"{url_api}/{id_evento}",json=datos)
        if response.status_code == 200:
            messagebox.showerror("Extio","Evento modificado correctamente")
            actualizar_tabla()
            limpiar()
        else:
            messagebox.showerror("Error",f"No se puedo modificar: {response.text}")
    except Exception as e:
        messagebox.showerror("Error",f"No se pudo conectar con la API: {e}")

def eliminar():
    id_evento = cam_id.get().strip()
    if id_evento == "":
        messagebox.showwarning("Error", "Ingrese el id del evento a eliminar")
        return
    try:
        response = requests.delete(f"{url_api}/{id_evento}")
        if response.status_code == 200:
            messagebox.showerror("Extio","Evento eliminado correctamente")
            actualizar_tabla()
            limpiar()
        else:
            messagebox.showerror("Error",f"No se puedo eliminar: {response.text}")
    except Exception as e:
        messagebox.showerror("Error",f"No se pudo conectar con la API: {e}")

def limpiar():
    cam_id.delete(0,tk.END)
    cam_nombre.delete(0,tk.END)
    cam_fecha.delete(0,tk.END)

ventana = tk.Tk()
ventana.title("INTERFAS DE EVENTO CON APIS")
ventana.geometry("900x600")

lbl_id = tk.Label(ventana, text="INGRESE EL ID DEL EVENTO: SOLO PARA ELIMINAR O MODIFCAR")
lbl_id.pack()
cam_id = tk.Entry(ventana)
cam_id.pack()

lbl_nombre = tk.Label(ventana, text="INGRESE EL NOMBRE DEL EVENTO")
lbl_nombre.pack()
cam_nombre = tk.Entry(ventana)
cam_nombre.pack()

lbl_fecha = tk.Label(ventana, text="INGRESE LA FECHA DEL EVENTO")
lbl_fecha.pack()
cam_fecha = tk.Entry(ventana)
cam_fecha.pack()

tabla = ttk.Treeview(ventana,columns=("id","nombre","fecha"), show="headings")
tabla.heading("id", text="ID")
tabla.heading("nombre", text="Nombre")
tabla.heading("fecha", text="Fecha")
tabla.pack(pady=10)


buttonagregar = tk.Button(ventana, text="AGREGAR",command=agregar).pack(pady=10)
buttonactualizar = tk.Button(ventana, text="EDITAR",command=modificar).pack(pady=10)
buttoneliminar = tk.Button(ventana, text="ELIMINAR",command=eliminar).pack(pady=10)
buttonlimpiar = tk.Button(ventana, text="LIMPIAR CAMPOS",command=limpiar).pack(pady=10)
buttonlistar = tk.Button(ventana, text="LISTAR DATOS",command=actualizar_tabla).pack(pady=10)

ventana.mainloop()