import tkinter as tk
from tkinter import ttk

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = None
        self.ventana_inicial = tk.Tk()
        self.ventana_inicial.title("Ventana Inicial")

        self.btn_abrir_ventana_principal = ttk.Button(self.ventana_inicial, text="Abrir Ventana Principal", command=self.abrir_ventana_principal)
        self.btn_abrir_ventana_principal.pack(padx=10, pady=10)

    def abrir_ventana_principal(self):
        self.ventana_inicial.withdraw()

        self.ventana = tk.Tk()
        self.ventana.title("MVC con Tkinter y SQLite")

        self.label_id = ttk.Label(self.ventana, text="Id:")
        self.label_id.grid(row=0, column=0, padx=10, pady=10)
        self.label_info_id = ttk.Label(self.ventana, text="")
        self.label_info_id.grid(row=0, column=1, padx=10, pady=10)

        self.label_nombre = ttk.Label(self.ventana, text="Nombre:")
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nombre = ttk.Entry(self.ventana)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.label_edad = ttk.Label(self.ventana, text="Edad:")
        self.label_edad.grid(row=2, column=0, padx=10, pady=10)
        self.entry_edad = ttk.Entry(self.ventana)
        self.entry_edad.grid(row=2, column=1, padx=10, pady=10)

        self.btn_agregar = ttk.Button(self.ventana, text="Agregar Usuario", command=self.agregar_usuario)
        self.btn_agregar.grid(row=3, column=0,  pady=10)

        self.btn_actualizar = ttk.Button(self.ventana, text="Actualizar Usuario", command=self.actualizar_usuario)
        self.btn_actualizar.grid(row=3, column=1,  pady=10)

        self.btn_eliminar = ttk.Button(self.ventana, text="Eliminar Usuario", command=self.eliminar_usuario)
        self.btn_eliminar.grid(row=3, column=2,  pady=10)

        self.btn_regresar = ttk.Button(self.ventana, text="Regresar a Ventana Inicial", command=self.regresar_a_ventana_inicial)
        self.btn_regresar.grid(row=5, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Edad"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Edad", text="Edad")
        self.tree.grid(row=4, column=0, columnspan=2, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos)
        self.ventana.mainloop()

    def agregar_usuario(self):
        nombre = self.entry_nombre.get()
        edad = int(self.entry_edad.get())
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
            self.label_info_id.config(text = values[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, values[1])  
            self.entry_edad.delete(0, tk.END)
            self.entry_edad.insert(0, values[2])  
    
    def eliminar_usuario(self):
        id_usuario = self.label_info_id.cget("text")
        if id_usuario:
            self.controlador.eliminar_usuario(id_usuario)
            self.actualizar_lista_usuarios()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_edad.delete(0, tk.END)

    def actualizar_usuario(self):
        id_usuario = self.label_info_id.cget("text")
        nombre = self.entry_nombre.get()
        edad = int(self.entry_edad.get())
        if id_usuario:
            self.controlador.actualizar_usuario(id_usuario,nombre,edad)
            self.actualizar_lista_usuarios()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_edad.delete(0, tk.END)

    def regresar_a_ventana_inicial(self):
        self.ventana.destroy()
        self.ventana_inicial.deiconify()    

    def iniciar_aplicacion(self):
        self.ventana_inicial.mainloop()
