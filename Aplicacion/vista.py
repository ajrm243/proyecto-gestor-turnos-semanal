import tkinter as tk
from tkinter import ttk


class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana_inicial = tk.Tk()
        self.ventana_inicial.title("Ventana Inicial")

        self.ventana_inicial.geometry('500x370+{}+{}'.format((self.ventana_inicial.winfo_screenwidth() - 500) // 2,
                                                              (self.ventana_inicial.winfo_screenheight() - 370) // 2))
        self.ventana_inicial.resizable(width=False, height=False)

        self.crear_boton(self.ventana_inicial, x=190, y=80, text="Colaboradores", command=self.abrir_ventana_principal)
        self.crear_boton(self.ventana_inicial, x=190, y=130, text="Roles")
        self.crear_boton(self.ventana_inicial, x=190, y=180, text="Turnos")
        self.crear_boton(self.ventana_inicial, x=190, y=230, text="Disponibilidades")
        self.crear_boton(self.ventana_inicial, x=190, y=280, text="Cargar Colaboradores")

    def crear_boton(self, ventana, x, y, text, command=None):
        boton = tk.Button(
            ventana,
            bg="#4E5485",
            fg="#e9e4e4",
            justify="center",
            text=text,
            command=command
        )
        boton.place(x=x, y=y, width=120, height=35)
        return boton

    def abrir_ventana_principal(self):
        self.ventana_inicial.withdraw()

        self.ventana = tk.Tk()
        self.ventana.title("Opciones de Usuario")
        self.ventana.geometry('780x470+{}+{}'.format((self.ventana.winfo_screenwidth() - 500) // 2,
                                                      (self.ventana.winfo_screenheight() - 370) // 2))
        self.ventana.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana, text="Id:")
        self.label_id.place(x=120, y=20)
        self.label_info_id = ttk.Label(self.ventana, text="")
        self.label_info_id.place(x=230, y=20)

        self.label_nombre = ttk.Label(self.ventana, text="Nombre:")
        self.label_nombre.place(x=120, y=60)
        self.entry_nombre = ttk.Entry(self.ventana)
        self.entry_nombre.place(x=230, y=60)

        self.label_edad = ttk.Label(self.ventana, text="Edad:")
        self.label_edad.place(x=120, y=100)
        self.entry_edad = ttk.Entry(self.ventana)
        self.entry_edad.place(x=230, y=100)

        self.crear_boton(self.ventana, x=480, y=10, text="Agregar Usuario", command=self.agregar_usuario)
        self.crear_boton(self.ventana, x=480, y=50, text="Actualizar Usuario", command=self.actualizar_usuario)
        self.crear_boton(self.ventana, x=480, y=90, text="Eliminar Usuario", command=self.eliminar_usuario)
        self.crear_boton(self.ventana, x=330, y=400, text="Regresar", command=self.regresar_a_ventana_inicial)

        self.tree = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Edad"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Edad", text="Edad")
        self.tree.place(x=100, y=150)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos)
        self.tree.tag_configure("par", background="#E3E4F3", foreground="black")
        self.tree.tag_configure("impar", background="white", foreground="black")

        self.actualizar_lista_usuarios()
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
        for i, usuario in enumerate(usuarios):
            etiqueta_estilo = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", values=usuario, tags=(etiqueta_estilo,))

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
