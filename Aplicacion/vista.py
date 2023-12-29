import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        #Ventana Login
        self.ventana_login = tk.Tk()
        self.ventana_login.title("Login")

        self.ventana_login.geometry('500x370')
        self.ventana_login.resizable(width=False, height=False)

        self.crear_boton(self.ventana_login, x=170, y=80, text="Inicio Admin", command= self.abrir_menuPrincipal)
        self.crear_boton(self.ventana_login, x=170, y=130, text="Inicio Usuario")

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
        boton.place(x=x, y=y, width=150, height=35)
        return boton
    
    #Ventana Menú Principal
    def abrir_menuPrincipal(self):
        self.ventana_login.withdraw()
        self.ventana_menuPrincipal = tk.Tk()
        self.ventana_menuPrincipal.title("Menú Principal")

        self.ventana_menuPrincipal.geometry('500x370')
        self.ventana_menuPrincipal.resizable(width=False, height=False)

        self.crear_boton(self.ventana_menuPrincipal, x=170, y=80, text="Opciones de Colaborador", command=self.abrir_ventana_opcionesColaborador)
        self.crear_boton(self.ventana_menuPrincipal, x=170, y=130, text="Opciones de Horario")
        self.crear_boton(self.ventana_menuPrincipal, x=170, y=180, text="Opciones de Usuario", command=self.abrir_ventana_usuarios)
    
    #Ventana opciones de colaborador
    def abrir_ventana_opcionesColaborador(self):
        self.ventana_menuPrincipal.withdraw()
        self.ventana_opcionesColaborador = tk.Tk()
        self.ventana_opcionesColaborador.title("Ventana Inicial")

        self.ventana_opcionesColaborador.geometry('500x370')
        self.ventana_opcionesColaborador.resizable(width=False, height=False)

        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=80, text="Colaboradores", command=self.abrir_ventana_colaboradores)
        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=130, text="Roles", command=self.abrir_ventana_roles)
        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=180, text="Turnos", command=self.abrir_ventana_turnos)
        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=230, text="Disponibilidades", command=self.abrir_ventana_disponibilidades)
        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=280, text="Cargar Colaboradores", command=self.abrir_ventana_explorador_archivos)

#--------USUARIOS----------
        
    def abrir_ventana_usuarios(self):
        self.ventana_menuPrincipal.withdraw()

        self.ventana_usuarios = tk.Tk()
        self.ventana_usuarios.title("Opciones de Usuario")
        self.ventana_usuarios.geometry('800x530')
        self.ventana_usuarios.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana_usuarios, text="Id:")
        self.label_id.place(x=120, y=50)
        self.label_info_id = ttk.Label(self.ventana_usuarios, text="")
        self.label_info_id.place(x=230, y=50)

        self.label_username = ttk.Label(self.ventana_usuarios, text="Username:")
        self.label_username.place(x=120, y=90)
        self.entry_username = ttk.Entry(self.ventana_usuarios)
        self.entry_username.place(x=230, y=90)

        self.label_password = ttk.Label(self.ventana_usuarios, text="Password:")
        self.label_password.place(x=120, y=130)
        self.entry_password = ttk.Entry(self.ventana_usuarios)
        self.entry_password.place(x=230, y=130)

        self.crear_boton(self.ventana_usuarios, x=480, y=20, text="Agregar Usuario", command=self.agregar_usuario)
        self.crear_boton(self.ventana_usuarios, x=480, y=60, text="Actualizar Usuario", command=self.actualizar_usuario)
        self.crear_boton(self.ventana_usuarios, x=480, y=100, text="Eliminar Usuario", command=self.eliminar_usuario)
        self.crear_boton(self.ventana_usuarios, x=480, y=140, text="Limpiar Datos", command=self.limpiar_datos_usuario)
        self.crear_boton(self.ventana_usuarios, x=330, y=470, text="Regresar", command=self.regresar_usuarios)

        self.tree = ttk.Treeview(self.ventana_usuarios, columns=("ID", "Username", "Password"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.place(x=100, y=210)

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

    def limpiar_datos_usuario(self):     
        self.label_info_id.config(text="")
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)   

    def regresar_usuarios(self):
        self.ventana_usuarios.destroy()
        self.ventana_menuPrincipal.deiconify()    

#--------ROLES----------
            
    def abrir_ventana_roles(self):
        self.ventana_opcionesColaborador.withdraw()

        self.ventana_roles = tk.Tk()
        self.ventana_roles.title("Opciones de Roles")
        self.ventana_roles.geometry('780x470')
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
        self.ventana_opcionesColaborador.deiconify()  

#--------DISPONIBILIDADES----------
            
    def abrir_ventana_disponibilidades(self):
        self.ventana_opcionesColaborador.withdraw()

        self.ventana_disponibilidades = tk.Tk()
        self.ventana_disponibilidades.title("Opciones de Disponibilidades")
        self.ventana_disponibilidades.geometry('780x470')
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
        self.ventana_opcionesColaborador.deiconify()      

#--------TURNOS-----------------  

    def abrir_ventana_turnos(self):
        self.ventana_opcionesColaborador.withdraw()

        self.ventana_turnos = tk.Tk()
        self.ventana_turnos.title("Opciones de Turnos")
        self.ventana_turnos.geometry('1000x670+{}+{}'.format((self.ventana_turnos.winfo_screenwidth() - 500) // 2,
                                                      (self.ventana_turnos.winfo_screenheight() - 370) // 2))
        self.ventana_turnos.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana_turnos, text="Id:")
        self.label_id.place(x=120, y=20)
        self.label_info_id = ttk.Label(self.ventana_turnos, text="")
        self.label_info_id.place(x=230, y=20)

        self.label_nombre = ttk.Label(self.ventana_turnos, text="Nombre:")
        self.label_nombre.place(x=120, y=60)
        self.entry_nombre = ttk.Entry(self.ventana_turnos)
        self.entry_nombre.place(x=230, y=60)

        self.label_lunes = ttk.Label(self.ventana_turnos, text=f"Lunes:")
        self.label_lunes.place(x=120, y=100) 
        self.entry_lunes_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_lunes_ingreso.place(x=230, y=100)
        self.entry_lunes_salida = ttk.Entry(self.ventana_turnos)
        self.entry_lunes_salida.place(x=350, y=100)

        self.label_martes = ttk.Label(self.ventana_turnos, text="Martes:")
        self.label_martes.place(x=120, y=140) 
        self.entry_martes_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_martes_ingreso.place(x=230, y=140)
        self.entry_martes_salida = ttk.Entry(self.ventana_turnos)
        self.entry_martes_salida.place(x=350, y=140)

        self.label_miercoles = ttk.Label(self.ventana_turnos, text="Miércoles:")
        self.label_miercoles.place(x=120, y=180) 
        self.entry_miercoles_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_miercoles_ingreso.place(x=230, y=180)
        self.entry_miercoles_salida = ttk.Entry(self.ventana_turnos)
        self.entry_miercoles_salida.place(x=350, y=180)

        self.label_jueves = ttk.Label(self.ventana_turnos, text="Jueves:")
        self.label_jueves.place(x=120, y=220) 
        self.entry_jueves_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_jueves_ingreso.place(x=230, y=220)
        self.entry_jueves_salida = ttk.Entry(self.ventana_turnos)
        self.entry_jueves_salida.place(x=350, y=220)

        self.label_viernes = ttk.Label(self.ventana_turnos, text="Viernes:")
        self.label_viernes.place(x=120, y=260) 
        self.entry_viernes_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_viernes_ingreso.place(x=230, y=260)
        self.entry_viernes_salida = ttk.Entry(self.ventana_turnos)
        self.entry_viernes_salida.place(x=350, y=260)

        self.label_sabado = ttk.Label(self.ventana_turnos, text="Sábado:")
        self.label_sabado.place(x=120, y=300) 
        self.entry_sabado_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_sabado_ingreso.place(x=230, y=300)
        self.entry_sabado_salida = ttk.Entry(self.ventana_turnos)
        self.entry_sabado_salida.place(x=350, y=300)

        self.label_domingo = ttk.Label(self.ventana_turnos, text="Domingo:")
        self.label_domingo.place(x=120, y=340) 
        self.entry_domingo_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_domingo_ingreso.place(x=230, y=340)
        self.entry_domingo_salida = ttk.Entry(self.ventana_turnos)
        self.entry_domingo_salida.place(x=350, y=340)

        self.crear_boton(self.ventana_turnos, x=480, y=10, text="Agregar Turno", command=self.agregar_turno)
        self.crear_boton(self.ventana_turnos, x=480, y=50, text="Actualizar Turno", command=self.actualizar_turno)
        self.crear_boton(self.ventana_turnos, x=480, y=90, text="Eliminar Turno", command=self.eliminar_turno)
        self.crear_boton(self.ventana_turnos, x=330, y=610, text="Regresar", command=self.regresar_turnos)


        self.tree = ttk.Treeview(self.ventana_turnos, columns=("ID", "Nombre", "Lunes Ingreso", "Lunes Salida", "Martes Ingreso", "Martes Salida", "Miércoles Ingreso", "Miércoles Salida", "Jueves Ingreso", "Jueves Salida", "Viernes Ingreso", "Viernes Salida", "Sábado Ingreso", "Sábado Salida", "Domingo Ingreso", "Domingo Salida"), show="headings")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.heading("ID", text="ID")
        
        self.tree.column("Nombre", width=115, anchor="center")
        self.tree.heading("Nombre", text="Nombre")
        
        self.tree.column("Lunes Ingreso", width=115, anchor="center")
        self.tree.heading("Lunes Ingreso", text="Lunes Ingreso")
        
        self.tree.column("Lunes Salida", width=80, anchor="center")
        self.tree.heading("Lunes Salida", text="Lunes Salida")
        
        self.tree.column("Martes Ingreso", width=50, anchor="center")
        self.tree.heading("Martes Ingreso", text="Martes Ingreso")
        
        self.tree.column("Martes Salida", width=50, anchor="center")
        self.tree.heading("Martes Salida", text="Martes Salida")
        
        self.tree.column("Miércoles Ingreso", width=90, anchor="center")
        self.tree.heading("Miércoles Ingreso", text="Miércoles Ingreso")
        
        self.tree.column("Miércoles Salida", width=90, anchor="center")
        self.tree.heading("Miércoles Salida", text="Miércoles Salida")

        self.tree.column("Jueves Ingreso", width=90, anchor="center")
        self.tree.heading("Jueves Ingreso", text="Jueves Ingreso")

        self.tree.column("Jueves Salida", width=90, anchor="center")
        self.tree.heading("Jueves Salida", text="Jueves Salida")

        self.tree.column("Viernes Ingreso", width=90, anchor="center")
        self.tree.heading("Viernes Ingreso", text="Viernes Ingreso")

        self.tree.column("Viernes Salida", width=90, anchor="center")
        self.tree.heading("Viernes Salida", text="Viernes Salida")

        self.tree.column("Sábado Ingreso", width=90, anchor="center")
        self.tree.heading("Sábado Ingreso", text="Sábado Ingreso")

        self.tree.column("Sábado Salida", width=90, anchor="center")
        self.tree.heading("Sábado Salida", text="Sábado Salida")

        self.tree.column("Domingo Ingreso", width=90, anchor="center")
        self.tree.heading("Domingo Ingreso", text="Domingo Ingreso")

        self.tree.column("Domingo Salida", width=90, anchor="center")
        self.tree.heading("Domingo Salida", text="Domingo Salida")
        
        self.tree.place(x=50, y=310, width=640, height=200)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos_turnos)
        self.tree.tag_configure("par", background="#E3E4F3", foreground="black")
        self.tree.tag_configure("impar", background="white", foreground="black")

        self.actualizar_lista_turnos()
        self.ventana_turnos.mainloop()

    def agregar_turno(self):
        nombre = self.entry_nombre.get()
        lunes_ingreso = self.entry_lunes_ingreso.get()
        lunes_salida = self.entry_lunes_salida.get()
        martes_ingreso = self.entry_martes_ingreso.get()
        martes_salida = self.entry_martes_salida.get()
        miercoles_ingreso = self.entry_miercoles_ingreso.get()
        miercoles_salida = self.entry_miercoles_salida.get()
        jueves_ingreso = self.entry_jueves_ingreso.get()
        jueves_salida = self.entry_jueves_salida.get()
        viernes_ingreso = self.entry_viernes_ingreso.get()
        viernes_salida = self.entry_viernes_salida.get()
        sabado_ingreso = self.entry_sabado_ingreso.get()
        sabado_salida = self.entry_sabado_salida.get()
        domingo_ingreso = self.entry_domingo_ingreso.get()
        domingo_salida = self.entry_domingo_salida.get()
        label_values = (nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida)
        print("Get values:", label_values)
        if nombre:
            print("pase el if de los label!")
            self.controlador.agregar_turno(
                nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida
            )
            self.actualizar_lista_turnos()
            self.entry_nombre.delete(0, tk.END)
            self.entry_lunes_ingreso.delete(0, tk.END)
            self.entry_lunes_salida.delete(0, tk.END)
            self.entry_martes_ingreso.delete(0, tk.END)
            self.entry_martes_salida.delete(0, tk.END)
            self.entry_miercoles_ingreso.delete(0, tk.END)
            self.entry_miercoles_salida.delete(0, tk.END)
            self.entry_jueves_ingreso.delete(0, tk.END)
            self.entry_jueves_salida.delete(0, tk.END)
            self.entry_viernes_ingreso.delete(0, tk.END)
            self.entry_viernes_salida.delete(0, tk.END)
            self.entry_sabado_ingreso.delete(0, tk.END)
            self.entry_sabado_salida.delete(0, tk.END)
            self.entry_domingo_ingreso.delete(0, tk.END)
            self.entry_domingo_salida.delete(0, tk.END)

    def actualizar_lista_turnos(self):
        turnos = self.controlador.obtener_turnos()
        self.tree.delete(*self.tree.get_children())
        for i, turno in enumerate(turnos):
            etiqueta_estilo = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", values=turno, tags=(etiqueta_estilo,))

    def seleccionar_campos_turnos(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            self.label_info_id.config(text = values[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, values[1])
            self.entry_lunes_ingreso.delete(0, tk.END)
            self.entry_lunes_ingreso.insert(0, values[2])
            self.entry_lunes_salida.delete(0, tk.END)
            self.entry_lunes_salida.insert(0, values[3])
            self.entry_martes_ingreso.delete(0, tk.END)
            self.entry_martes_ingreso.insert(0, values[4])
            self.entry_martes_salida.delete(0, tk.END)
            self.entry_martes_salida.insert(0, values[5])
            self.entry_miercoles_ingreso.delete(0, tk.END)
            self.entry_miercoles_ingreso.insert(0, values[6])
            self.entry_miercoles_salida.delete(0, tk.END)
            self.entry_miercoles_salida.insert(0, values[7])
            self.entry_jueves_ingreso.delete(0, tk.END)
            self.entry_jueves_ingreso.insert(0, values[8])
            self.entry_jueves_salida.delete(0, tk.END)
            self.entry_jueves_salida.insert(0, values[9])
            self.entry_viernes_ingreso.delete(0, tk.END)
            self.entry_viernes_ingreso.insert(0, values[10])
            self.entry_viernes_salida.delete(0, tk.END)
            self.entry_viernes_salida.insert(0, values[11])
            self.entry_sabado_ingreso.delete(0, tk.END)
            self.entry_sabado_ingreso.insert(0, values[12])
            self.entry_sabado_salida.delete(0, tk.END)
            self.entry_sabado_salida.insert(0, values[13])
            self.entry_domingo_ingreso.delete(0, tk.END)
            self.entry_domingo_ingreso.insert(0, values[14])
            self.entry_domingo_salida.delete(0, tk.END)
            self.entry_domingo_salida.insert(0, values[15])
            
    def eliminar_turno(self):
        id_turno = self.label_info_id.cget("text")
        if id_turno:
            self.controlador.eliminar_turno(id_turno)
            self.actualizar_lista_turnos()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_lunes_ingreso.delete(0, tk.END)
            self.entry_lunes_salida.delete(0, tk.END)
            self.entry_martes_ingreso.delete(0, tk.END)
            self.entry_martes_salida.delete(0, tk.END)
            self.entry_miercoles_ingreso.delete(0, tk.END)
            self.entry_miercoles_salida.delete(0, tk.END)
            self.entry_jueves_ingreso.delete(0, tk.END)
            self.entry_jueves_salida.delete(0, tk.END)
            self.entry_viernes_ingreso.delete(0, tk.END)
            self.entry_viernes_salida.delete(0, tk.END)
            self.entry_sabado_ingreso.delete(0, tk.END)
            self.entry_sabado_salida.delete(0, tk.END)
            self.entry_domingo_ingreso.delete(0, tk.END)
            self.entry_domingo_salida.delete(0, tk.END)

    def actualizar_turno(self):
        id_turno = self.label_info_id.cget("text")
        nombre = self.entry_nombre.get()
        lunes_ingreso = self.entry_lunes_ingreso.get()
        lunes_salida = self.entry_lunes_salida.get()
        martes_ingreso = self.entry_martes_ingreso.get()
        martes_salida = self.entry_martes_salida.get()
        miercoles_ingreso = self.entry_miercoles_ingreso.get()
        miercoles_salida = self.entry_miercoles_salida.get()
        jueves_ingreso = self.entry_jueves_ingreso.get()
        jueves_salida = self.entry_jueves_salida.get()
        viernes_ingreso = self.entry_viernes_ingreso.get()
        viernes_salida = self.entry_viernes_salida.get()
        sabado_ingreso = self.entry_sabado_ingreso.get()
        sabado_salida = self.entry_sabado_salida.get()
        domingo_ingreso = self.entry_domingo_ingreso.get()
        domingo_salida = self.entry_domingo_salida.get()
        if id_turno:
            self.controlador.actualizar_turno(
                nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida, id_turno
            )
            self.actualizar_lista_turnos()
            self.label_info_id.config(text="")
            self.entry_nombre.delete(0, tk.END)
            self.entry_lunes_ingreso.delete(0, tk.END)
            self.entry_lunes_salida.delete(0, tk.END)
            self.entry_martes_ingreso.delete(0, tk.END)
            self.entry_martes_salida.delete(0, tk.END)
            self.entry_miercoles_ingreso.delete(0, tk.END)
            self.entry_miercoles_salida.delete(0, tk.END)
            self.entry_jueves_ingreso.delete(0, tk.END)
            self.entry_jueves_salida.delete(0, tk.END)
            self.entry_viernes_ingreso.delete(0, tk.END)
            self.entry_viernes_salida.delete(0, tk.END)
            self.entry_sabado_ingreso.delete(0, tk.END)
            self.entry_sabado_salida.delete(0, tk.END)
            self.entry_domingo_ingreso.delete(0, tk.END)
            self.entry_domingo_salida.delete(0, tk.END)

    def regresar_turnos(self):
        self.ventana_turnos.destroy()
        self.ventana_opcionesColaborador.deiconify()        

#--------COLABORADORES----------
    def abrir_ventana_colaboradores(self):
        self.ventana_opcionesColaborador.withdraw()

        self.ventana_colaboradores = tk.Tk()
        self.ventana_colaboradores.title("Opciones de Colaborador")
        self.ventana_colaboradores.geometry('780x670')
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
        self.crear_boton(self.ventana_colaboradores, x=330, y=610, text="Regresar", command=self.regresar_colaboradores)


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
        self.ventana_opcionesColaborador.deiconify()    

#-------OTROS-----------

    def iniciar_aplicacion(self):
        self.ventana_login.mainloop()
    
    def abrir_ventana_explorador_archivos(self):
        tk.Tk().withdraw()
        filename = askopenfilename()
        print("Filename:",filename)
        self.controlador.cargar_lista_colaboradores(filename)
