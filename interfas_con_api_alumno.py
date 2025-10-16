
import tkinter as tk                    
from tkinter import ttk, messagebox     
import requests                        

URL_API = "http://127.0.0.1:5000/alumnos"  


def listar_alumnos():
    """
    Esta función obtiene la lista de alumnos desde la API (GET)
    y los muestra en la tabla (Treeview).
    """
    try:
        response = requests.get(URL_API)

        data = response.json()

        for fila in tree.get_children():
            tree.delete(fila)

        for alumno in data:
            tree.insert("", "end", values=(
                alumno["id"],         
                alumno["nombre"],     
                alumno["edad"],       
                alumno["Nota1"],      
                alumno["Nota2"],      
                alumno["Nota3"]       
            ))
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo listar alumnos: {e}")

def ventana_editar():
    """
    Abre una ventana emergente (Toplevel) con los datos del alumno seleccionado,
    permitiendo modificar y actualizar su información mediante PUT.
    """
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Atención", "Selecciona un alumno para editar.")
        return

    valores = tree.item(selected[0])["values"]
    id_alumno = valores[0] 

    top = tk.Toplevel(root)
    top.title("Editar Alumno")
    top.geometry("300x350")

    tk.Label(top, text="Nombre:").pack()
    nombre = tk.Entry(top)
    nombre.insert(0, valores[1]) 
    nombre.pack()

    tk.Label(top, text="Edad:").pack()
    edad = tk.Entry(top)
    edad.insert(0, valores[2])
    edad.pack()

    tk.Label(top, text="Nota1:").pack()
    nota1 = tk.Entry(top)
    nota1.insert(0, valores[3])
    nota1.pack()

    tk.Label(top, text="Nota2:").pack()
    nota2 = tk.Entry(top)
    nota2.insert(0, valores[4])
    nota2.pack()

    tk.Label(top, text="Nota3:").pack()
    nota3 = tk.Entry(top)
    nota3.insert(0, valores[5])
    nota3.pack()

   
    def guardar_cambios():
        
        actualizado = {
            "nombre": nombre.get(),
            "edad": int(edad.get()),
            "Nota1": float(nota1.get()),
            "Nota2": float(nota2.get()),
            "Nota3": float(nota3.get())
        }
        try:
           
            requests.put(f"{URL_API}/{id_alumno}", json=actualizado)

            listar_alumnos()

            messagebox.showinfo("Éxitoo", "Alumno actualizado correctamente.")
            top.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar: {e}")

    tk.Button(top, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)


def eliminar_alumno():
    """
    Elimina al alumno seleccionado de la tabla y de la base de datos (API).
    """
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Atención", "Selecciona un alumno para eliminar.")
        return

    id_alumno = tree.item(selected[0])["values"][0]
    try:
        requests.delete(f"{URL_API}/{id_alumno}")

        listar_alumnos()

        messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar: {e}")


def ventana_agregar():
    """
    Abre una ventana emergente para registrar un nuevo alumno
    y lo envía al servidor mediante POST.
    """
    top = tk.Toplevel(root)
    top.title("Agregar Alumno")
    top.geometry("300x350")

    tk.Label(top, text="Nombre:").pack()
    nombre = tk.Entry(top)
    nombre.pack()

    tk.Label(top, text="Edad:").pack()
    edad = tk.Entry(top)
    edad.pack()

    tk.Label(top, text="Nota1:").pack()
    nota1 = tk.Entry(top)
    nota1.pack()

    tk.Label(top, text="Nota2:").pack()
    nota2 = tk.Entry(top)
    nota2.pack()

    tk.Label(top, text="Nota3:").pack()
    nota3 = tk.Entry(top)
    nota3.pack()


    def guardar():
        nuevo = {
            "nombre": nombre.get(),
            "edad": int(edad.get()),
            "Nota1": float(nota1.get()),
            "Nota2": float(nota2.get()),
            "Nota3": float(nota3.get())
        }
        try:
            requests.post(URL_API, json=nuevo)

            listar_alumnos()

            messagebox.showinfo("Éxito", "Alumno agregado correctamente.")
            top.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar: {e}")

    tk.Button(top, text="Guardar", command=guardar).pack(pady=10)

root = tk.Tk()
root.title("Gestión de Alumnos")
root.geometry("650x400")  

frame = tk.Frame(root)
frame.pack(pady=20)

columns = ("ID", "Nombre", "Edad", "Nota1", "Nota2", "Nota3")

tree = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack()

tk.Button(root, text="Listar Alumnos", command=listar_alumnos).pack(pady=5)
tk.Button(root, text="Agregar Alumno", command=ventana_agregar).pack(pady=5)
tk.Button(root, text="Editar Alumno", command=ventana_editar).pack(pady=5)
tk.Button(root, text="Eliminar Alumno", command=eliminar_alumno).pack(pady=5)

listar_alumnos()
root.mainloop()
