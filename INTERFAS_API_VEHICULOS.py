import tkinter as tk
from tkinter import ttk,messagebox
import requests

url_api="http://127.0.0.1:5000/vehiculos"

#funciones
def actualizar():
    try:
        response = requests.get(url_api)
        vehiculos = response.json()
        
        for fila in tabla.get_children():
            tabla.delete(fila)
            
        for vehi in vehiculos:
            tabla.insert("",tk.END, values=(vehi["id"], vehi["marca"], vehi["precio"], vehi["año"]))
    except Exception as e:
        messagebox.showerror("Error",f"NO SE PUEDO CONECTAR CON LA API:{e}")

def agregar():
    marca = camp_marca.get().strip()
    precio = camp_precio.get().strip()
    anio = camp_año.get().strip()
    
    if marca == "" or precio == "" or anio == "":
        messagebox.showwarning('Error','COMPLETE TODOS LOS CAMPOS')
        return
    #crea un diccionario que luego se manda en formato json
    datos = {"marca": marca,"precio":precio,"año":anio}
    
    try:
        response = requests.post(url_api,json=datos)
        if response.status_code==201:
            messagebox.showinfo("Exito","Vehiculos agregado correctamente")
            actualizar()
            limpiar()
        else:
            messagebox.showerror("Error",f"No se pudo agregar:{response.text}")
    except Exception as e:
        messagebox.showerror("Error",f"No se puedo conectar con la API: {e}")

def modificar():
    id_vehiculo = camp_id.get().strip()
    if id_vehiculo == "":
        messagebox.showwarning("Error","Ingrese el id del vehiculo para modificar")
        return
    marca = camp_marca.get().strip()
    precio = camp_precio.get().strip()
    anio = camp_año.get().strip()
    if marca == "" or precio == "" or anio == "":
        messagebox.showwarning('Error','Complete todos los campos')
        return
    datos = {"marca": marca,"precio":precio,"año":anio}
    
    try:
        response = requests.put(f"{url_api}/{id_vehiculo}",json=datos)
        if response.status_code == 200:
            messagebox.showinfo("Exito","Vehiculos Modificado correctamente")
            actualizar()
            limpiar()
        else:
            messagebox.showerror("Error",f"NO SE PUDO MODFICAR: {response.text}")
    except Exception as e:
        messagebox.showerror("Error",f"No se puedo conectar con la API: {e}")
        

def eliminar():
    id_vehiculo = camp_id.get().strip()
    if id_vehiculo == "":
        messagebox.showwarning('Error','Ingrese el id del vehiculo para eliminar')
        return
    try:
        response = requests.delete(f"{url_api}/{id_vehiculo}")
        if response.status_code == 200:
            messagebox.showinfo("Exito","Vehiculo eliminado correctamente")
            actualizar()
            limpiar()
        else:
            messagebox.showerror("Error",f"NO SE PUDO ELIMINAR: {response.text}")
    except Exception as e:
        messagebox.showerror("Error",f"No se puedo conectar con la API: {e}")

#limpiar los campos
def limpiar():
    camp_id.delete(0, tk.END)
    camp_marca.delete(0, tk.END)
    camp_precio.delete(0, tk.END)
    camp_año.delete(0, tk.END)

#ventana

ventana = tk.Tk()
ventana.title("FORMULARIO DE VEHICULOS")
ventana.geometry("900x600")

lbl_id = tk.Label(ventana, text="INGRESE EL ID")
lbl_id.pack()
camp_id = tk.Entry(ventana)
camp_id.pack()

lbl_marca = tk.Label(ventana, text="INGRESE LA MARCA")
lbl_marca.pack()
camp_marca = tk.Entry(ventana)
camp_marca.pack()

lbl_precio = tk.Label(ventana, text="INGRESE EL PRECIO DEL VEHICULO")
lbl_precio.pack()
camp_precio = tk.Entry(ventana)
camp_precio.pack()

lbl_año = tk.Label(ventana, text="INGRESE EL AÑO DEL VEHICULO")
lbl_año.pack()
camp_año = tk.Entry(ventana)
camp_año.pack()

#tabla
tabla = ttk.Treeview(ventana, columns=("id","marca","precio","año"), show="headings")
tabla.heading("id", text="ID")
tabla.heading("marca", text="MARCA")
tabla.heading("precio", text="PRECIO")
tabla.heading("año", text="AÑO")
tabla.pack(pady=10)
#botones

botonagregar = tk.Button(ventana, text="AGREGAR", command=agregar).pack()
botoneliminar = tk.Button(ventana, text="ELIMINAR", command=eliminar).pack()
botonmodificar = tk.Button(ventana, text="EDITAR", command=modificar).pack()
botonlimpiar = tk.Button(ventana, text="LIMPIAR CAMPOS", command=limpiar).pack()
botonlistar = tk.Button(ventana, text="LISTAR", command=actualizar).pack()

ventana.mainloop()
