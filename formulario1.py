#registrar formulario
import tkinter as tk
from tkinter import messagebox

ventana=tk.Tk()
ventana.title("REGISTRO DE USUARIO")
ventana.geometry("400x300")

lbl_nombre = tk.Label(ventana, text="INGRESE SU NOMBRE").pack()
camp_nombre = tk.Entry(ventana)
camp_nombre.pack()

lbl_correo = tk.Label(ventana, text="INGRESE SU CORREO").pack()
camp_correo = tk.Entry(ventana)
camp_correo.pack()

lbl_edad = tk.Label(ventana, text="INGRESE SU EDAD").pack()
camp_edad = tk.Entry(ventana)
camp_edad.pack()

#funcion registrar
def registrar():
    nombre = camp_nombre.get().strip() 
    correo = camp_correo.get().strip()
    edad = camp_edad.get().strip()
    
    if nombre == "" or correo == "" or edad == "":
        messagebox.showerror("ERROR",'COMPLETAR TODOS LOS CAMPOS')
    else:
        mensaje = f"Nombre:{nombre},correo:{correo},edad{edad}"
        messagebox.showinfo("REGISTRO EXITOSO",mensaje)

boton = tk.Button(ventana, text="REGISTRAR", command=registrar)
boton.pack()
ventana.mainloop()

