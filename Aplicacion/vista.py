import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        #Ventana Login
        self.ventana_login = tk.Tk()
        self.ventana_login.title("Login")

        self.ventana_login.geometry('500x370+{}+{}'.format((self.ventana_login.winfo_screenwidth() - 500) // 2,
                                                              (self.ventana_login.winfo_screenheight() - 370) // 2))
        self.ventana_login.resizable(width=False, height=False)

        self.crear_boton(self.ventana_login, x=190, y=80, text="Inicio Admin", command=self.abrir_menuPrincipal)
        self.crear_boton(self.ventana_login, x=190, y=130, text="Inicio Usuario")

    #Crear boton   
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
    
    #Ventana Menú Principal
    def abrir_menuPrincipal(self):
        self.ventana_login.withdraw()
        self.ventana_menuPrincipal = tk.Tk()
        self.ventana_menuPrincipal.title("Menú Principal")

        self.ventana_menuPrincipal.geometry('500x370+{}+{}'.format((self.ventana_menuPrincipal.winfo_screenwidth() - 500) // 2,
                                                              (self.ventana_menuPrincipal.winfo_screenheight() - 370) // 2))
        self.ventana_menuPrincipal.resizable(width=False, height=False)

        self.crear_boton(self.ventana_menuPrincipal, x=190, y=80, text="Opciones de Colaborador", command=self.abrir_ventana_opcionesColaborador)
        self.crear_boton(self.ventana_menuPrincipal, x=190, y=130, text="Opciones de Horario")
        self.crear_boton(self.ventana_menuPrincipal, x=190, y=180, text="Opciones de Usuario", command=self.abrir_ventana_usuarios)
    
    #Ventana opciones de colaborador
    def abrir_ventana_opcionesColaborador(self):
        self.ventana_menuPrincipal.withdraw()
        self.ventana_opcionesColaborador = tk.Tk()
        self.ventana_opcionesColaborador.title("Ventana Inicial")

        self.ventana_opcionesColaborador.geometry('500x370+{}+{}'.format((self.ventana_opcionesColaborador.winfo_screenwidth() - 500) // 2,
                                                              (self.ventana_opcionesColaborador.winfo_screenheight() - 370) // 2))
        self.ventana_opcionesColaborador.resizable(width=False, height=False)

        self.crear_boton(self.ventana_opcionesColaborador, x=190, y=80, text="Colaboradores", command=self.abrir_ventana_colaboradores)
        self.crear_boton(self.ventana_opcionesColaborador, x=190, y=130, text="Roles", command=self.abrir_ventana_roles)
        self.crear_boton(self.ventana_opcionesColaborador, x=190, y=180, text="Turnos")
        self.crear_boton(self.ventana_opcionesColaborador, x=190, y=230, text="Disponibilidades", command=self.abrir_ventana_disponibilidades)
        self.crear_boton(self.ventana_opcionesColaborador, x=190, y=280, text="Cargar Colaboradores", command=self.abrir_ventana_explorador_archivos)

#--------USUARIOS----------
    def abrir_ventana_usuarios(self):
        self.ventana_menuPrincipal.withdraw()

        self.ventana_usuarios = tk.Tk()
        self.ventana_usuarios.title("Opciones de Usuario")
        self.ventana_usuarios.geometry('780x470+{}+{}'.format((self.ventana_usuarios.winfo_screenwidth() - 500) // 2,
                                                      (self.ventana_usuarios.winfo_screenheight() - 370) // 2))
        self.ventana_usuarios.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana_usuarios, text="Id:")
        self.label_id.place(x=120, y=20)
        self.label_info_id = ttk.Label(self.ventana_usuarios, text="")
        self.label_info_id.place(x=230, y=20)

        self.label_username = ttk.Label(self.ventana_usuarios, text="Username:")
        self.label_username.place(x=120, y=60)
        self.entry_username = ttk.Entry(self.ventana_usuarios)
        self.entry_username.place(x=230, y=60)

        self.label_password = ttk.Label(self.ventana_usuarios, text="Password:")
        self.label_password.place(x=120, y=100)
        self.entry_password = ttk.Entry(self.ventana_usuarios)
        self.entry_password.place(x=230, y=100)

        self.crear_boton(self.ventana_usuarios, x=480, y=10, text="Agregar Usuario", command=self.agregar_usuario)
        self.crear_boton(self.ventana_usuarios, x=480, y=50, text="Actualizar Usuario", command=self.actualizar_usuario)
        self.crear_boton(self.ventana_usuarios, x=480, y=90, text="Eliminar Usuario", command=self.eliminar_usuario)
        self.crear_boton(self.ventana_usuarios, x=330, y=400, text="Regresar", command=self.regresar_usuarios)

        self.tree = ttk.Treeview(self.ventana_usuarios, columns=("ID", "Username", "Password"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.place(x=100, y=150)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos_usuarios)
        self.tree.tag_configure("par", background="#E3E4F3", foreground="black")
        self.tree.tag_configure("impar", background="white", foreground="black")

        self.actualizar_lista_usuarios()
        self.ventana_usuarios.mainloop()

    def agregar_usuario(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username and password:
            self.controlador.agregar_usuario(username, password)
            self.actualizar_lista_usuarios()
            self.entry_username.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
           

    def actualizar_lista_usuarios(self):
        usuarios = self.controlador.obtener_usuarios()
        self.tree.delete(*self.tree.get_children())
        for i, usuario in enumerate(usuarios):
            etiqueta_estilo = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", values=usuario, tags=(etiqueta_estilo,))

    def seleccionar_campos_usuarios(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            self.label_info_id.config(text = values[0])
            self.entry_username.delete(0, tk.END)
            self.entry_username.insert(0, values[1])  
            self.entry_password.delete(0, tk.END)
            self.entry_password.insert(0, values[2])  
    
    def eliminar_usuario(self):
        id_usuario = self.label_info_id.cget("text")
        if id_usuario:
            self.controlador.eliminar_usuario(id_usuario)
            self.actualizar_lista_usuarios()
            self.label_info_id.config(text="")
            self.entry_username.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)

    def actualizar_usuario(self):
        id_usuario = self.label_info_id.cget("text")
        username = self.entry_username.get()
        password = self.entry_password.get()
        if id_usuario:
            self.controlador.actualizar_usuario(id_usuario,username,password)
            self.actualizar_lista_usuarios()
            self.label_info_id.config(text="")
            self.entry_username.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)

    def regresar_usuarios(self):
        self.ventana_usuarios.destroy()
        self.ventana_menuPrincipal.deiconify()    

#--------ROLES----------
            
    def abrir_ventana_roles(self):
        self.ventana_menuPrincipal.withdraw()

        self.ventana_roles = tk.Tk()
        self.ventana_roles.title("Opciones de Roles")
        self.ventana_roles.geometry('780x470+{}+{}'.format((self.ventana_roles.winfo_screenwidth() - 500) // 2,
                                                      (self.ventana_roles.winfo_screenheight() - 370) // 2))
        self.ventana_roles.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana_roles, text="Id:")
        self.label_id.place(x=120, y=20)
        self.label_info_id = ttk.Label(self.ventana_roles, text="")
        self.label_info_id.place(x=230, y=20)

        self.label_nombre = ttk.Label(self.ventana_roles, text="Nombre:")
        self.label_nombre.place(x=120, y=60)
        self.entry_nombre = ttk.Entry(self.ventana_roles)
        self.entry_nombre.place(x=230, y=60)

        self.label_descripcion = ttk.Label(self.ventana_roles, text="Descripcion:")
        self.label_descripcion.place(x=120, y=100)
        self.entry_descripcion = ttk.Entry(self.ventana_roles)
        self.entry_descripcion.place(x=230, y=100)

        self.crear_boton(self.ventana_roles, x=480, y=10, text="Agregar Rol", command=self.agregar_rol)
        self.crear_boton(self.ventana_roles, x=480, y=50, text="Actualizar Rol", command=self.actualizar_rol)
        self.crear_boton(self.ventana_roles, x=480, y=90, text="Eliminar Rol", command=self.eliminar_rol)
        self.crear_boton(self.ventana_roles, x=330, y=400, text="Regresar", command=self.regresar_roles)

        self.tree = ttk.Treeview(self.ventana_roles, columns=("ID", "Nombre", "Descripcion"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripcion", text="Descripcion")
        self.tree.place(x=100, y=150)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos_roles)
        self.tree.tag_configure("par", background="#E3E4F3", foreground="black")
        self.tree.tag_configure("impar", background="white", foreground="black")

        self.actualizar_lista_roles()
        self.ventana_roles.mainloop()

    def agregar_rol(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        if nombre and descripcion:
            self.controlador.agregar_rol(nombre, descripcion)
            self.actualizar_lista_roles()
            self.entry_nombre.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)
           
    def actualizar_lista_roles(self):
        roles = self.controlador.obtener_roles()
        self.tree.delete(*self.tree.get_children())
        for i, rol in enumerate(roles):
            etiqueta_estilo = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", values=rol, tags=(etiqueta_estilo,))

    def seleccionar_campos_roles(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            self.label_info_id.config(text = values[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, values[1])  
            self.entry_descripcion.delete(0, tk.END)
            self.entry_descripcion.insert(0, values[2])  
    
    def eliminar_rol(self):
        id_rol = self.label_info_id.cget("text")
        if id_rol:
            self.controlador.eliminar_rol(id_rol)
            self.actualizar_lista_roles()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)

    def actualizar_rol(self):
        id_rol = self.label_info_id.cget("text")
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        if id_rol:
            self.controlador.actualizar_rol(id_rol,nombre,descripcion)
            self.actualizar_lista_roles()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)

    def regresar_roles(self):
        self.ventana_roles.destroy()
        self.ventana_menuPrincipal.deiconify()  

#--------DISPONIBILIDADES----------
            
    def abrir_ventana_disponibilidades(self):
        self.ventana_menuPrincipal.withdraw()

        self.ventana_disponibilidades = tk.Tk()
        self.ventana_disponibilidades.title("Opciones de Disponibilidades")
        self.ventana_disponibilidades.geometry('780x470+{}+{}'.format((self.ventana_disponibilidades.winfo_screenwidth() - 500) // 2,
                                                      (self.ventana_disponibilidades.winfo_screenheight() - 370) // 2))
        self.ventana_disponibilidades.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana_disponibilidades, text="Id:")
        self.label_id.place(x=120, y=20)
        self.label_info_id = ttk.Label(self.ventana_disponibilidades, text="")
        self.label_info_id.place(x=230, y=20)

        self.label_nombre = ttk.Label(self.ventana_disponibilidades, text="Nombre:")
        self.label_nombre.place(x=120, y=60)
        self.entry_nombre = ttk.Entry(self.ventana_disponibilidades)
        self.entry_nombre.place(x=230, y=60)

        self.label_descripcion = ttk.Label(self.ventana_disponibilidades, text="Descripcion:")
        self.label_descripcion.place(x=120, y=100)
        self.entry_descripcion = ttk.Entry(self.ventana_disponibilidades)
        self.entry_descripcion.place(x=230, y=100)

        self.crear_boton(self.ventana_disponibilidades, x=480, y=10, text="Agregar Disponibilidad", command=self.agregar_disponibilidad)
        self.crear_boton(self.ventana_disponibilidades, x=480, y=50, text="Actualizar Disponibilidad", command=self.actualizar_disponibilidad)
        self.crear_boton(self.ventana_disponibilidades, x=480, y=90, text="Eliminar Disponibilidad", command=self.eliminar_disponibilidad)
        self.crear_boton(self.ventana_disponibilidades, x=330, y=400, text="Regresar", command=self.regresar_disponibilidades)

        self.tree = ttk.Treeview(self.ventana_disponibilidades, columns=("ID", "Nombre", "Descripcion"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripcion", text="Descripcion")
        self.tree.place(x=100, y=150)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos_disponibilidades)
        self.tree.tag_configure("par", background="#E3E4F3", foreground="black")
        self.tree.tag_configure("impar", background="white", foreground="black")

        self.actualizar_lista_disponibilidades()
        self.ventana_disponibilidades.mainloop()

    def agregar_disponibilidad(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        if nombre and descripcion:
            self.controlador.agregar_disponibilidad(nombre, descripcion)
            self.actualizar_lista_disponibilidades()
            self.entry_nombre.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)
           
    def actualizar_lista_disponibilidades(self):
        disponibilidades = self.controlador.obtener_disponibilidades()
        self.tree.delete(*self.tree.get_children())
        for i, rol in enumerate(disponibilidades):
            etiqueta_estilo = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", values=rol, tags=(etiqueta_estilo,))

    def seleccionar_campos_disponibilidades(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            self.label_info_id.config(text = values[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, values[1])  
            self.entry_descripcion.delete(0, tk.END)
            self.entry_descripcion.insert(0, values[2])  
    
    def eliminar_disponibilidad(self):
        id_disponibilidad = self.label_info_id.cget("text")
        if id_disponibilidad:
            self.controlador.eliminar_disponibilidad(id_disponibilidad)
            self.actualizar_lista_disponibilidades()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)

    def actualizar_disponibilidad(self):
        id_disponibilidad = self.label_info_id.cget("text")
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        if id_disponibilidad:
            self.controlador.actualizar_disponibilidad(id_disponibilidad,nombre,descripcion)
            self.actualizar_lista_disponibilidades()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)

    def regresar_disponibilidades(self):
        self.ventana_disponibilidades.destroy()
        self.ventana_menuPrincipal.deiconify()            

#--------COLABORADORES----------
    def abrir_ventana_colaboradores(self):
        self.ventana_menuPrincipal.withdraw()

        self.ventana_colaboradores = tk.Tk()
        self.ventana_colaboradores.title("Opciones de Colaborador")
        self.ventana_colaboradores.geometry('780x470+{}+{}'.format((self.ventana_colaboradores.winfo_screenwidth() - 500) // 2,
                                                      (self.ventana_colaboradores.winfo_screenheight() - 370) // 2))
        self.ventana_colaboradores.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana_colaboradores, text="Id:")
        self.label_id.place(x=120, y=20)
        self.label_info_id = ttk.Label(self.ventana_colaboradores, text="")
        self.label_info_id.place(x=230, y=20)

        self.label_nombre = ttk.Label(self.ventana_colaboradores, text="Nombre:")
        self.label_nombre.place(x=120, y=60)
        self.entry_nombre = ttk.Entry(self.ventana_colaboradores)
        self.entry_nombre.place(x=230, y=60)

        self.label_correo = ttk.Label(self.ventana_colaboradores, text="Correo:")
        self.label_correo.place(x=120, y=100)
        self.entry_correo = ttk.Entry(self.ventana_colaboradores)
        self.entry_correo.place(x=230, y=100)
        
        self.label_telefono = ttk.Label(self.ventana_colaboradores, text="Telefono:")
        self.label_telefono.place(x=120, y=140)
        self.entry_telefono = ttk.Entry(self.ventana_colaboradores)
        self.entry_telefono.place(x=230, y=140)
        
        self.label_id_rol = ttk.Label(self.ventana_colaboradores, text="Rol:")
        self.label_id_rol.place(x=120, y=180)
        self.entry_id_rol = ttk.Entry(self.ventana_colaboradores)
        self.entry_id_rol.place(x=230, y=180)
        
        self.label_id_turno = ttk.Label(self.ventana_colaboradores, text="Turno:")
        self.label_id_turno.place(x=120, y=220)
        self.entry_id_turno = ttk.Entry(self.ventana_colaboradores)
        self.entry_id_turno.place(x=230, y=220)
        
        self.label_id_disponibilidad = ttk.Label(self.ventana_colaboradores, text="Disponibilidad:")
        self.label_id_disponibilidad.place(x=120, y=220)
        self.entry_id_disponibilidad = ttk.Entry(self.ventana_colaboradores)
        self.entry_id_disponibilidad.place(x=230, y=220)
        
        self.label_modalidad = ttk.Label(self.ventana_colaboradores, text="Modalidad:")
        self.label_modalidad.place(x=120, y=260)
        self.entry_modalidad = ttk.Entry(self.ventana_colaboradores)
        self.entry_modalidad.place(x=230, y=260)

        self.crear_boton(self.ventana_colaboradores, x=480, y=10, text="Agregar Colaborador", command=self.agregar_colaborador)
        self.crear_boton(self.ventana_colaboradores, x=480, y=50, text="Actualizar Colaborador", command=self.actualizar_colaborador)
        self.crear_boton(self.ventana_colaboradores, x=480, y=90, text="Eliminar Colaborador", command=self.eliminar_colaborador)
        self.crear_boton(self.ventana_colaboradores, x=330, y=400, text="Regresar", command=self.regresar_colaboradores)


        self.tree = ttk.Treeview(self.ventana_colaboradores, columns=("ID", "Nombre", "Correo", "Telefono", "Rol", "Turno", "Disponibilidad", "Modalidad"), show="headings")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.heading("ID", text="ID")
        
        self.tree.column("Nombre", width=115, anchor="center")
        self.tree.heading("Nombre", text="Nombre")
        
        self.tree.column("Correo", width=115, anchor="center")
        self.tree.heading("Correo", text="Correo")
        
        self.tree.column("Telefono", width=80, anchor="center")
        self.tree.heading("Telefono", text="Telefono")
        
        self.tree.column("Rol", width=50, anchor="center")
        self.tree.heading("Rol", text="Rol")
        
        self.tree.column("Turno", width=50, anchor="center")
        self.tree.heading("Turno", text="Turno")
        
        self.tree.column("Disponibilidad", width=90, anchor="center")
        self.tree.heading("Disponibilidad", text="Disponibilidad")
        
        self.tree.column("Modalidad", width=90, anchor="center")
        self.tree.heading("Modalidad", text="Modalidad")
        
        self.tree.place(x=50, y=310, width=640, height=200)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos_colaboradores)
        self.tree.tag_configure("par", background="#E3E4F3", foreground="black")
        self.tree.tag_configure("impar", background="white", foreground="black")

        self.actualizar_lista_colaboradores()
        self.ventana_colaboradores.mainloop()

    def agregar_colaborador(self):
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        telefono = self.entry_telefono.get()
        rol = self.entry_id_rol.get()
        turno = self.entry_id_turno.get()
        disponibilidad = self.entry_id_disponibilidad.get()
        modalidad = self.entry_modalidad.get()
        label_values = (nombre, correo, telefono, rol, turno, disponibilidad, modalidad)
        print("Get values:", label_values)
        if nombre and correo and telefono and rol and turno and disponibilidad and modalidad:
            print("pase el if de los label!")
            self.controlador.agregar_colaborador(
                nombre, correo, telefono, rol, turno, disponibilidad, modalidad
            )
            self.actualizar_lista_colaboradores()
            self.entry_nombre.delete(0, tk.END)
            self.entry_correo.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.entry_id_rol.delete(0, tk.END)
            self.entry_id_turno.delete(0, tk.END)
            self.entry_id_disponibilidad.delete(0, tk.END)
            self.entry_modalidad.delete(0, tk.END)
           

    def actualizar_lista_colaboradores(self):
        colaboradores = self.controlador.obtener_colaboradores()
        print(colaboradores)
        self.tree.delete(*self.tree.get_children())
        for i, colaborador in enumerate(colaboradores):
            etiqueta_estilo = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", values=colaborador, tags=(etiqueta_estilo,))

    def seleccionar_campos_colaboradores(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            self.label_info_id.config(text = values[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, values[1])
            self.entry_correo.delete(0, tk.END)
            self.entry_correo.insert(0, values[2])
            self.entry_telefono.delete(0, tk.END)
            self.entry_telefono.insert(0, values[3])
            self.entry_id_rol.delete(0, tk.END)
            self.entry_id_rol.insert(0, values[4])
            self.entry_id_turno.delete(0, tk.END)
            self.entry_id_turno.insert(0, values[5])
            self.entry_id_disponibilidad.delete(0, tk.END)
            self.entry_id_disponibilidad.insert(0, values[6])
            self.entry_modalidad.delete(0, tk.END)
            self.entry_modalidad.insert(0, values[7])
            
    def eliminar_colaborador(self):
        id_colaborador = self.label_info_id.cget("text")
        if id_colaborador:
            self.controlador.eliminar_colaborador(id_colaborador)
            self.actualizar_lista_colaboradores()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_correo.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.entry_id_rol.delete(0, tk.END)
            self.entry_id_turno.delete(0, tk.END)
            self.entry_id_disponibilidad.delete(0, tk.END)
            self.entry_modalidad.delete(0, tk.END)

    def actualizar_colaborador(self):
        id_colaborador = self.label_info_id.cget("text")
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        telefono = self.entry_telefono.get()
        rol = self.entry_id_rol.get()
        turno = self.entry_id_turno.get()
        disponibilidad = self.entry_id_disponibilidad.get()
        modalidad = self.entry_modalidad.get()
        if id_colaborador:
            self.controlador.agregar_colaborador(
                nombre, correo, telefono, rol, turno, disponibilidad, modalidad, id_colaborador
            )
            self.actualizar_lista_colaboradores()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_correo.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.entry_id_rol.delete(0, tk.END)
            self.entry_id_turno.delete(0, tk.END)
            self.entry_id_disponibilidad.delete(0, tk.END)
            self.entry_modalidad.delete(0, tk.END)

    def regresar_colaboradores(self):
        self.ventana_colaboradores.destroy()
        self.ventana_menuPrincipal.deiconify()    

#-------OTROS-----------

    def iniciar_aplicacion(self):
        self.ventana_login.mainloop()
    
    def abrir_ventana_explorador_archivos(self):
        tk.Tk().withdraw()
        filename = askopenfilename()
        print("Filename:",filename)
        self.controlador.cargar_lista_colaboradores(filename)
