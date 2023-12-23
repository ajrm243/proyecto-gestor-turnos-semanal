import tkinter as tk
from tkinter import ttk

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = tk.Tk()
        self.ventana.title("MVC con Tkinter y SQLite")

        self.label_nombre = ttk.Label(self.ventana, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre = ttk.Entry(self.ventana)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_edad = ttk.Label(self.ventana, text="Edad:")
        self.label_edad.grid(row=1, column=0, padx=10, pady=10)
        self.entry_edad = ttk.Entry(self.ventana)
        self.entry_edad.grid(row=1, column=1, padx=10, pady=10)

        self.btn_agregar = ttk.Button(self.ventana, text="Agregar Usuario", command=self.agregar_usuario)
        self.btn_agregar.grid(row=2, column=0, columnspan=2, pady=10)

        self.btn_eliminar = ttk.Button(self.ventana, text="Eliminar Usuario", command=self.eliminar_usuario)
        self.btn_eliminar.grid(row=2, column=2, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Edad"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Edad", text="Edad")
        self.tree.grid(row=3, column=0, columnspan=2, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos)

    def agregar_usuario(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        if nombre and edad:
            self.controlador.agregar_usuario(nombre, edad)
            self.actualizar_lista_usuarios()
            self.entry_nombre.delete(0, tk.END)
            self.entry_edad.delete(0, tk.END)
           

    def actualizar_lista_usuarios(self):
        usuarios = self.controlador.obtener_usuarios()
        self.tree.delete(*self.tree.get_children())
        for usuario in usuarios:
            self.tree.insert("", "end", values=usuario)

    def seleccionar_campos(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, values[1])  
            self.entry_edad.delete(0, tk.END)
            self.entry_edad.insert(0, values[2])  
    
    def eliminar_usuario(self):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            self.controlador.eliminar_usuario(values[0])  # Suponiendo que values[0] contiene el ID del usuario
            self.actualizar_lista_usuarios()

    def iniciar_aplicacion(self):
        self.ventana.mainloop()