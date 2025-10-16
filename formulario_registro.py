import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("REGISTRAR ALUMNOD")
ventana.geometry("400x300")

lbl_nombre = tk.Label(ventana, text="Nombre:").pack()
camp_nombre = tk.Entry(ventana)
camp_nombre.pack()

lbl_correo = tk.Label(ventana, text="Correo:").pack()
camp_correo = tk.Entry(ventana)
camp_correo.pack()

lbl_edad = tk.Label(ventana, text="Edad:").pack()
camp_edad = tk.Entry(ventana)
camp_edad.pack()

#funciones para registrar y limpiar
def registrar():
    nombre = camp_nombre.get()
    correo = camp_correo.get()
    edad = camp_edad.get()
    if nombre and correo and edad:
        messagebox.showinfo('Registrado', f'Alumno {nombre}, correo {correo}, edad {edad} registrado con éxito.')
        limpiar() 
    else:
        messagebox.showwarning('Error', 'Por favor complete todos los campos')
def limpiar():
    camp_nombre.delete(0, tk.END)
    camp_correo.delete(0, tk.END)
    camp_edad.delete(0, tk.END)

#botonoes
btn_registrar = tk.Button(ventana, text='Registrar', command=registrar).pack()
btn_limpiar = tk.Button(ventana, text='Limpiar', command=limpiar).pack()
ventana.mainloop()