import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
import re #para validacion de datos


class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        #Ventana Login
        self.ventana_login = tk.Tk()
        self.ventana_login.title("Login")

        self.ventana_login.geometry('500x370')
        self.ventana_login.resizable(width=False, height=False)

        self.label_nombre = ttk.Label(self.ventana_login, text="Usuario:")
        self.label_nombre.place(x=100, y=90)
        self.entry_nombre = ttk.Entry(self.ventana_login)
        self.entry_nombre.place(x=180, y=90, width=200)

        self.label_password = ttk.Label(self.ventana_login, text="Password:")
        self.label_password.place(x=100, y=130)
        self.entry_password = ttk.Entry(self.ventana_login,show="*")
        self.entry_password.place(x=180, y=130, width=200)

        self.crear_boton(self.ventana_login, x=190, y=200, text="Inicio Admin", command= self.inicio_admin)
        self.crear_boton(self.ventana_login, x=190, y=250, text="Inicio Usuario", command=self.inicio_usuario)

#--------LOGIN--------------
    def inicio_usuario(self):
        usuario = self.entry_nombre.get()
        password = self.entry_password.get()
        self.controlador.inicio_usuario(usuario, password)

    def procesar_inicio_usuario(self, resultado):
        if resultado:
            self.abrir_ventana_horario("usuario") #cambiar a la ventana de usuario cuando esté lista
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def inicio_admin(self):
        usuario = self.entry_nombre.get()
        password = self.entry_password.get()
        self.controlador.inicio_admin(usuario, password)

    def procesar_inicio_admin(self, resultado):
        if resultado:
            self.abrir_menuPrincipal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
        
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

        self.crear_boton(self.ventana_menuPrincipal, x=170, y=110, text="Opciones de Colaborador", command=self.abrir_ventana_opcionesColaborador)
        self.crear_boton(self.ventana_menuPrincipal, x=170, y=160, text="Opciones de Horario", command=self.abrir_ventana_opcionesHorario)
        self.crear_boton(self.ventana_menuPrincipal, x=170, y=210, text="Opciones de Usuario", command=self.abrir_ventana_usuarios)
        self.crear_boton(self.ventana_menuPrincipal, x=170, y=260, text="Salir", command=self.salir_aplicacion)
    
    def salir_aplicacion(self):
        self.ventana_menuPrincipal.destroy()
        
    #Ventana opciones de colaborador
    def abrir_ventana_opcionesColaborador(self):
        self.ventana_menuPrincipal.withdraw()
        self.ventana_opcionesColaborador = tk.Tk()
        self.ventana_opcionesColaborador.title("Ventana Inicial")

        self.ventana_opcionesColaborador.geometry('500x370')
        self.ventana_opcionesColaborador.resizable(width=False, height=False)

        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=60, text="Colaboradores", command=self.abrir_ventana_colaboradores)
        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=110, text="Roles", command=self.abrir_ventana_roles)
        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=160, text="Turnos", command=self.abrir_ventana_turnos)
        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=210, text="Disponibilidades", command=self.abrir_ventana_disponibilidades)
        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=260, text="Cargar Colaboradores", command=self.abrir_ventana_explorador_archivos)
        self.crear_boton(self.ventana_opcionesColaborador, x=170, y=310, text="Regresar", command=self.regresar_opcionesColaborador)
        
    def regresar_opcionesColaborador(self):
        self.ventana_opcionesColaborador.destroy()
        self.ventana_menuPrincipal.deiconify()
    

    def abrir_ventana_opcionesHorario(self):
        self.ventana_menuPrincipal.withdraw()
        self.ventana_opcionesHorario = tk.Tk()
        self.ventana_opcionesHorario.title("Opciones Horario")

        self.ventana_opcionesHorario.geometry('500x370')
        self.ventana_opcionesHorario.resizable(width=False, height=False)

        self.crear_boton(self.ventana_opcionesHorario, x=170, y=110, text="Generar Horario", command=self.obtener_colaboradores_disponibles)
        self.crear_boton(self.ventana_opcionesHorario, x=170, y=160, text="Visualizar Horario", command=lambda: self.abrir_ventana_horario("administrador"))
        self.crear_boton(self.ventana_opcionesHorario, x=170, y=210, text="Regresar", command=self.regresar_menuPrincipal)

    def regresar_menuPrincipal(self):
        self.ventana_opcionesHorario.destroy()
        self.ventana_menuPrincipal.deiconify()

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
            estado_consulta = self.controlador.agregar_usuario(username, password)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Usuario agregado con éxito")
                self.actualizar_lista_usuarios()
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Hubo un problema al agregar el usuario")
        else:
            messagebox.showerror("Error", "Debe rellenar todos los campos")
           
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
            estado_consulta = self.controlador.eliminar_usuario(id_usuario)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Usuario eliminado con éxito")
                self.actualizar_lista_usuarios()
                self.label_info_id.config(text="")
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Hubo un problema al eliminar el usuario")
        else:
            messagebox.showerror("Error", "Debe seleccionar un usuario")

    def actualizar_usuario(self):
        id_usuario = self.label_info_id.cget("text")
        username = self.entry_username.get()
        password = self.entry_password.get()
        if id_usuario:
            estado_consulta = self.controlador.actualizar_usuario(id_usuario, username, password)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Usuario actualizado con éxito")
                self.actualizar_lista_usuarios()
                self.label_info_id.config(text="")
                self.entry_username.delete(0, tk.END)
                self.entry_password.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar el usuario")
        else:
            messagebox.showerror("Error", "Debe seleccionar un usuario")

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
        self.ventana_roles.geometry('800x530')
        self.ventana_roles.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana_roles, text="Id:")
        self.label_id.place(x=120, y=50)
        self.label_info_id = ttk.Label(self.ventana_roles, text="")
        self.label_info_id.place(x=230, y=50)

        self.label_nombre = ttk.Label(self.ventana_roles, text="Nombre:")
        self.label_nombre.place(x=120, y=90)
        self.entry_nombre = ttk.Entry(self.ventana_roles)
        self.entry_nombre.place(x=230, y=90)

        self.label_descripcion = ttk.Label(self.ventana_roles, text="Descripción:")
        self.label_descripcion.place(x=120, y=130)
        self.entry_descripcion = ttk.Entry(self.ventana_roles)
        self.entry_descripcion.place(x=230, y=130)

        self.crear_boton(self.ventana_roles, x=480, y=20, text="Agregar Rol", command=self.agregar_rol)
        self.crear_boton(self.ventana_roles, x=480, y=60, text="Actualizar Rol", command=self.actualizar_rol)
        self.crear_boton(self.ventana_roles, x=480, y=100, text="Eliminar Rol", command=self.eliminar_rol)
        self.crear_boton(self.ventana_roles, x=480, y=140, text="Limpiar Datos", command=self.limpiar_datos_rol)
        self.crear_boton(self.ventana_roles, x=330, y=470, text="Regresar", command=self.regresar_roles)

        self.tree = ttk.Treeview(self.ventana_roles, columns=("ID", "Nombre", "Descripción"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.place(x=100, y=210)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos_roles)
        self.tree.tag_configure("par", background="#E3E4F3", foreground="black")
        self.tree.tag_configure("impar", background="white", foreground="black")

        self.actualizar_lista_roles()
        self.ventana_roles.mainloop()

    def agregar_rol(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        if nombre:
            res_comprobacion_rol = self.controlador.comprobar_nombre_rol(nombre)
            if not res_comprobacion_rol:
                estado_consulta = self.controlador.agregar_rol(nombre, descripcion)
                if estado_consulta:
                    messagebox.showinfo("Éxito", "Rol agregado con éxito")
                    self.actualizar_lista_roles()
                    self.entry_nombre.delete(0, tk.END)
                    self.entry_descripcion.delete(0, tk.END)
                else: 
                    messagebox.showerror("Error", "Hubo un problema al agregar el rol")
            else:
                messagebox.showerror("Error", "Ya hay un rol con ese nombre")
        else:
            messagebox.showerror("Error", "Debe rellenar todos los campos")
           
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
        nombre = self.entry_nombre.get()

        if id_rol and nombre not in ["A3", "A1", "A2"]:
            estado_consulta = self.controlador.eliminar_rol(id_rol)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Rol eliminado con éxito")
                self.actualizar_lista_roles()
                self.label_info_id.config(text="")
                self.entry_nombre.delete(0, tk.END)
                self.entry_descripcion.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Hubo un problema al eliminando el rol")
        else:
            messagebox.showerror("Error", "Debe seleccionar un rol válido")

    def actualizar_rol(self):
        id_rol = self.label_info_id.cget("text")
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()

        if id_rol and nombre not in ["A3", "A1", "A2"]:
            estado_consulta = self.controlador.actualizar_rol(id_rol, nombre, descripcion)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Rol actualizado con éxito")
                self.actualizar_lista_roles()
                self.label_info_id.config(text="")
                self.entry_nombre.delete(0, tk.END)
                self.entry_descripcion.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar el rol")
        else:
            messagebox.showerror("Error", "Debe seleccionar un rol válido")

    def limpiar_datos_rol(self):     
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
        self.ventana_disponibilidades.geometry('800x530')
        self.ventana_disponibilidades.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana_disponibilidades, text="Id:")
        self.label_id.place(x=120, y=50)
        self.label_info_id = ttk.Label(self.ventana_disponibilidades, text="")
        self.label_info_id.place(x=230, y=50)

        self.label_nombre = ttk.Label(self.ventana_disponibilidades, text="Nombre:")
        self.label_nombre.place(x=120, y=90)
        self.entry_nombre = ttk.Entry(self.ventana_disponibilidades)
        self.entry_nombre.place(x=230, y=90)

        self.label_descripcion = ttk.Label(self.ventana_disponibilidades, text="Descripción:")
        self.label_descripcion.place(x=120, y=130)
        self.entry_descripcion = ttk.Entry(self.ventana_disponibilidades)
        self.entry_descripcion.place(x=230, y=130)

        self.crear_boton(self.ventana_disponibilidades, x=480, y=20, text="Agregar Disponibilidad", command=self.agregar_disponibilidad)
        self.crear_boton(self.ventana_disponibilidades, x=480, y=60, text="Actualizar Disponibilidad", command=self.actualizar_disponibilidad)
        self.crear_boton(self.ventana_disponibilidades, x=480, y=100, text="Eliminar Disponibilidad", command=self.eliminar_disponibilidad)
        self.crear_boton(self.ventana_disponibilidades, x=480, y=140, text="Limpiar Datos", command=self.limpiar_datos_rol)
        self.crear_boton(self.ventana_disponibilidades, x=330, y=470, text="Regresar", command=self.regresar_disponibilidades)

        self.tree = ttk.Treeview(self.ventana_disponibilidades, columns=("ID", "Nombre", "Descripción"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.place(x=100, y=210)

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos_disponibilidades)
        self.tree.tag_configure("par", background="#E3E4F3", foreground="black")
        self.tree.tag_configure("impar", background="white", foreground="black")

        self.actualizar_lista_disponibilidades()
        self.ventana_disponibilidades.mainloop()

    def agregar_disponibilidad(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        if nombre:
            res_comprobacion_disponibilidad = self.controlador.comprobar_nombre_disponibilidad(nombre)
            if not res_comprobacion_disponibilidad:
                estado_consulta= self.controlador.agregar_disponibilidad(nombre, descripcion)
                if estado_consulta:
                    messagebox.showinfo("Éxito", "Disponibilidad agregada con éxito")
                    self.actualizar_lista_disponibilidades()
                    self.entry_nombre.delete(0, tk.END)
                    self.entry_descripcion.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Hubo un problema al agregar disponibilidad")
            else:
                messagebox.showerror("Error", "Ya hay una disponibilidad con ese nombre")
        else:
            messagebox.showerror("Error", "Debe rellenar todos los campos")
           
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
        nombre = self.entry_nombre.get()
        if id_disponibilidad and nombre != "Disponible":
            estado_consulta = self.controlador.eliminar_disponibilidad(id_disponibilidad)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Disponibilidad elimindada con éxito")
                self.actualizar_lista_disponibilidades()
                self.label_info_id.config(text="")
                self.entry_nombre.delete(0, tk.END)
                self.entry_descripcion.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Hubo un problema al eliminar disponibilidad")
        else:
            messagebox.showerror("Error", "Debe seleccionar una disponibilidad válida")

    def actualizar_disponibilidad(self):
        id_disponibilidad = self.label_info_id.cget("text")
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        if id_disponibilidad and nombre != "Disponible":
            estado_consulta = self.controlador.actualizar_disponibilidad(id_disponibilidad,nombre,descripcion)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Disponibilidad actualizada con éxito")
                self.actualizar_lista_disponibilidades()
                self.label_info_id.config(text="")
                self.entry_nombre.delete(0, tk.END)
                self.entry_descripcion.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar disponibilidad")
        else:
            messagebox.showerror("Error", "Debe seleccionar una disponibilidad válida")

    def limpiar_datos_disponibilidad(self):     
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
        self.ventana_turnos.geometry('1450x900')
        self.ventana_turnos.resizable(width=False, height=False)

        self.label_id = ttk.Label(self.ventana_turnos, text="Id:")
        self.label_id.place(x=120, y=10)
        self.label_info_id = ttk.Label(self.ventana_turnos, text="")
        self.label_info_id.place(x=230, y=10)

        self.label_nombre = ttk.Label(self.ventana_turnos, text="Nombre:")
        self.label_nombre.place(x=270, y=10)
        self.entry_nombre = ttk.Entry(self.ventana_turnos)
        self.entry_nombre.place(x=370, y=10)

        self.label_ingreso = ttk.Label(self.ventana_turnos, text="Ingreso")
        self.label_ingreso.place(x=275, y=55) 
        self.label_salida = ttk.Label(self.ventana_turnos, text="Salida")
        self.label_salida.place(x=415, y=55) 

        self.label_lunes = ttk.Label(self.ventana_turnos, text="Lunes:")
        self.label_lunes.place(x=120, y=80) 
        self.entry_lunes_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_lunes_ingreso.place(x=230, y=80)
        self.entry_lunes_salida = ttk.Entry(self.ventana_turnos)
        self.entry_lunes_salida.place(x=370, y=80)

        self.label_martes = ttk.Label(self.ventana_turnos, text="Martes:")
        self.label_martes.place(x=120, y=120) 
        self.entry_martes_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_martes_ingreso.place(x=230, y=120)
        self.entry_martes_salida = ttk.Entry(self.ventana_turnos)
        self.entry_martes_salida.place(x=370, y=120)

        self.label_miercoles = ttk.Label(self.ventana_turnos, text="Miércoles:")
        self.label_miercoles.place(x=120, y=160) 
        self.entry_miercoles_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_miercoles_ingreso.place(x=230, y=160)
        self.entry_miercoles_salida = ttk.Entry(self.ventana_turnos)
        self.entry_miercoles_salida.place(x=370, y=160)

        self.label_jueves = ttk.Label(self.ventana_turnos, text="Jueves:")
        self.label_jueves.place(x=120, y=200) 
        self.entry_jueves_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_jueves_ingreso.place(x=230, y=200)
        self.entry_jueves_salida = ttk.Entry(self.ventana_turnos)
        self.entry_jueves_salida.place(x=370, y=200)

        self.label_viernes = ttk.Label(self.ventana_turnos, text="Viernes:")
        self.label_viernes.place(x=120, y=240) 
        self.entry_viernes_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_viernes_ingreso.place(x=230, y=240)
        self.entry_viernes_salida = ttk.Entry(self.ventana_turnos)
        self.entry_viernes_salida.place(x=370, y=240)

        self.label_sabado = ttk.Label(self.ventana_turnos, text="Sábado:")
        self.label_sabado.place(x=120, y=280) 
        self.entry_sabado_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_sabado_ingreso.place(x=230, y=280)
        self.entry_sabado_salida = ttk.Entry(self.ventana_turnos)
        self.entry_sabado_salida.place(x=370, y=280)

        self.label_domingo = ttk.Label(self.ventana_turnos, text="Domingo:")
        self.label_domingo.place(x=120, y=320) 
        self.entry_domingo_ingreso = ttk.Entry(self.ventana_turnos)
        self.entry_domingo_ingreso.place(x=230, y=320)
        self.entry_domingo_salida = ttk.Entry(self.ventana_turnos)
        self.entry_domingo_salida.place(x=370, y=320)

        self.crear_boton(self.ventana_turnos, x=650, y=90, text="Agregar Turno", command=self.agregar_turno)
        self.crear_boton(self.ventana_turnos, x=650, y=130, text="Actualizar Turno", command=self.actualizar_turno)
        self.crear_boton(self.ventana_turnos, x=650, y=170, text="Eliminar Turno", command=self.eliminar_turno)
        self.crear_boton(self.ventana_turnos, x=650, y=210, text="Limpiar Datos", command=self.limpiar_datos_turno)
        self.crear_boton(self.ventana_turnos, x=400, y=570, text="Regresar", command=self.regresar_turnos)


        self.tree = ttk.Treeview(self.ventana_turnos, columns=("ID", "Nombre", "Lunes Ingreso", "Lunes Salida", "Martes Ingreso", "Martes Salida", "Miércoles Ingreso", "Miércoles Salida", "Jueves Ingreso", "Jueves Salida", "Viernes Ingreso", "Viernes Salida", "Sábado Ingreso", "Sábado Salida", "Domingo Ingreso", "Domingo Salida"), show="headings")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.heading("ID", text="ID")
        
        self.tree.column("Nombre", width=90, anchor="center")
        self.tree.heading("Nombre", text="Nombre")
        
        self.tree.column("Lunes Ingreso", width=90, anchor="center")
        self.tree.heading("Lunes Ingreso", text="Lun Ingreso")
        
        self.tree.column("Lunes Salida", width=90, anchor="center")
        self.tree.heading("Lunes Salida", text="Lun Salida")
        
        self.tree.column("Martes Ingreso", width=90, anchor="center")
        self.tree.heading("Martes Ingreso", text="Mar Ingreso")
        
        self.tree.column("Martes Salida", width=90, anchor="center")
        self.tree.heading("Martes Salida", text="Mar Salida")
        
        self.tree.column("Miércoles Ingreso", width=90, anchor="center")
        self.tree.heading("Miércoles Ingreso", text="Mié Ingreso")
        
        self.tree.column("Miércoles Salida", width=90, anchor="center")
        self.tree.heading("Miércoles Salida", text="Mié Salida")

        self.tree.column("Jueves Ingreso", width=90, anchor="center")
        self.tree.heading("Jueves Ingreso", text="Jue Ingreso")

        self.tree.column("Jueves Salida", width=90, anchor="center")
        self.tree.heading("Jueves Salida", text="Jue Salida")

        self.tree.column("Viernes Ingreso", width=90, anchor="center")
        self.tree.heading("Viernes Ingreso", text="Vie Ingreso")

        self.tree.column("Viernes Salida", width=90, anchor="center")
        self.tree.heading("Viernes Salida", text="Vie Salida")

        self.tree.column("Sábado Ingreso", width=90, anchor="center")
        self.tree.heading("Sábado Ingreso", text="Sáb Ingreso")

        self.tree.column("Sábado Salida", width=90, anchor="center")
        self.tree.heading("Sábado Salida", text="Sáb Salida")

        self.tree.column("Domingo Ingreso", width=90, anchor="center")
        self.tree.heading("Domingo Ingreso", text="Dom Ingreso")

        self.tree.column("Domingo Salida", width=90, anchor="center")
        self.tree.heading("Domingo Salida", text="Dom Salida")
        
        self.tree.place(x=40, y=380, width=1400, height=170)
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
        if nombre:
            res_comprobacion_turno = self.controlador.comprobar_nombre_turno(nombre)
            if not res_comprobacion_turno:
                estado_consulta = self.controlador.agregar_turno(
                    nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida
                )
                if estado_consulta:
                    messagebox.showinfo("Éxito", "Turno agregado con éxito")
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
                else:
                    messagebox.showerror("Error", "Hubo un problema al agregar turno")
            else:
                messagebox.showerror("Error", "Ya hay un turno con ese nombre")
        else:
            messagebox.showerror("Error", "Debe ingresar un nombre para el turno")

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
        nombre = self.entry_nombre.get()
        turnos_fijos = ["T1_F","T2_F","T3_F","T4_F","T5_F","T6_F",
                        "TF1_FF","TF2_FN","TF3_FN","TF4_FN","TF7_FM",
                        "TF8_FM","TF9_FM","TF10_FM","TF12_MN","TF13_MN",
                        "TF14_FF","T1_M","T2_M","T3_M","T4_M","T5_M","T6_M",
                        "HFC1","HFC2","HFC3","HFC4","HFC5"
                        ]
        if id_turno and nombre not in turnos_fijos:
            estado_consulta =  self.controlador.eliminar_turno(id_turno)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Turno eliminado con éxito")
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
            else:
                messagebox.showerror("Error", "Hubo un problema al aliminar el turno")
        else:
            messagebox.showerror("Error", "Debe seleccionar un turno válido")

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
            estado_consulta= self.controlador.actualizar_turno(
                nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida, id_turno
            )
            if estado_consulta:
                messagebox.showinfo("Éxito", "Turno actualizado con éxito")
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
            else: 
                messagebox.showerror("Error", "Hubo un problema al actualizar el turno")
        else:
            messagebox.showerror("Error", "Debe seleccionar un turno")

    def limpiar_datos_turno(self):
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
        self.ventana_colaboradores.geometry('780x620')
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
        
        self.label_telefono = ttk.Label(self.ventana_colaboradores, text="Teléfono:")
        self.label_telefono.place(x=120, y=140)
        self.entry_telefono = ttk.Entry(self.ventana_colaboradores)
        self.entry_telefono.place(x=230, y=140)

        nombre_roles = self.controlador.obtener_nombre_roles()
        roles_values = self.controlador.obtener_roles()
        #print("roles", roles_values)
        dict_roles = {tup[0] : tup[1] for tup in roles_values}
        
        self.label_id_rol = ttk.Label(self.ventana_colaboradores, text="Rol:")
        self.label_id_rol.place(x=120, y=180)
        self.combobox_id_rol = ttk.Combobox(self.ventana_colaboradores, state="readonly")
        self.combobox_id_rol['values'] = list(dict_roles.values())
        self.combobox_id_rol.place(x=230, y=180)
        
        nombre_turnos = self.controlador.obtener_nombre_turnos()
        turnos_values = self.controlador.obtener_turnos()
        #print("turnos", turnos_values)
        dict_turnos = {tup[0] : tup[1] for tup in turnos_values}

        self.label_id_turno = ttk.Label(self.ventana_colaboradores, text="Turno:")
        self.label_id_turno.place(x=120, y=220)
        self.combobox_id_turno = ttk.Combobox(self.ventana_colaboradores, state="readonly")
        self.combobox_id_turno['values'] = list(dict_turnos.values())
        self.combobox_id_turno.place(x=230, y=220)
        
        nombre_disponibilidades = self.controlador.obtener_nombre_disponibilidades()
        disponibilidades_values = self.controlador.obtener_disponibilidades()
        #print("disponibilidades", disponibilidades_values)
        dict_disponibilidades = {tup[0] : tup[1] for tup in disponibilidades_values}
        
        self.label_id_disponibilidad = ttk.Label(self.ventana_colaboradores, text="Disponibilidad:")
        self.label_id_disponibilidad.place(x=120, y=260)
        self.combobox_id_disponibilidad = ttk.Combobox(self.ventana_colaboradores, state="readonly")
        self.combobox_id_disponibilidad['values'] = list(dict_disponibilidades.values())
        self.combobox_id_disponibilidad.place(x=230, y=260)
        
        self.label_modalidad = ttk.Label(self.ventana_colaboradores, text="Modalidad:")
        self.label_modalidad.place(x=120, y=300)
        self.combobox_modalidad = ttk.Combobox(self.ventana_colaboradores, state="readonly")
        self.combobox_modalidad['values'] = ("Presencial", "Virtual") # hard wired porque solo consideramos presencial y virtual (wfh)
        self.combobox_modalidad.place(x=230, y=300)
        #self.entry_modalidad = ttk.Entry(self.ventana_colaboradores)
        #self.entry_modalidad.place(x=230, y=300)

        self.crear_boton(self.ventana_colaboradores, x=480, y=90, text="Agregar Colaborador", command=self.agregar_colaborador)
        self.crear_boton(self.ventana_colaboradores, x=480, y=130, text="Actualizar Colaborador", command=self.actualizar_colaborador)
        self.crear_boton(self.ventana_colaboradores, x=480, y=170, text="Eliminar Colaborador", command=self.eliminar_colaborador)
        self.crear_boton(self.ventana_colaboradores, x=480, y=210, text="Limpiar Datos", command=self.limpiar_datos_colaborador)
        self.crear_boton(self.ventana_colaboradores, x=320, y=560, text="Regresar", command=self.regresar_colaboradores)
        
        # Filtros
        filtros = self.controlador.obtener_filtros_colaborador()
        #print("Filtros:", filtros)
        dict_filtros = {'Todos': -1}
        filtros_bd = {tup[0] : tup[1] for tup in filtros}
        dict_filtros.update(filtros_bd)
        #print("Dict:", dict_filtros)
        self.combobox_filtro_colaborador = ttk.Combobox(self.ventana_colaboradores, state="readonly")
        self.combobox_filtro_colaborador['values'] = list(dict_filtros.keys())
        self.combobox_filtro_colaborador.place(x=480, y=260)
        self.combobox_filtro_colaborador.bind("<<ComboboxSelected>>", self.filtrar_lista_colaboradores)

        self.tree = ttk.Treeview(self.ventana_colaboradores, columns=("ID", "Nombre", "Correo", "Teléfono", "Rol", "Turno", "Disponibilidad", "Modalidad"), show="headings")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.heading("ID", text="ID")
        
        self.tree.column("Nombre", width=115, anchor="center")
        self.tree.heading("Nombre", text="Nombre")
        
        self.tree.column("Correo", width=115, anchor="center")
        self.tree.heading("Correo", text="Correo")
        
        self.tree.column("Teléfono", width=80, anchor="center")
        self.tree.heading("Teléfono", text="Telefono")
        
        self.tree.column("Rol", width=50, anchor="center")
        self.tree.heading("Rol", text="Rol")
        
        self.tree.column("Turno", width=50, anchor="center")
        self.tree.heading("Turno", text="Turno")
        
        self.tree.column("Disponibilidad", width=90, anchor="center")
        self.tree.heading("Disponibilidad", text="Disponibilidad")
        
        self.tree.column("Modalidad", width=90, anchor="center")
        self.tree.heading("Modalidad", text="Modalidad")
        
        self.tree.place(x=70, y=340, width=640, height=200)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos_colaboradores)
        self.tree.tag_configure("par", background="#E3E4F3", foreground="black")
        self.tree.tag_configure("impar", background="white", foreground="black")

        self.actualizar_lista_colaboradores()
        self.ventana_colaboradores.mainloop()

    def agregar_colaborador(self):
        # Para la conversion de texto a ID
        roles_values = self.controlador.obtener_roles()
        dict_roles = {tup[0] : tup[1] for tup in roles_values}
        turnos_values = self.controlador.obtener_turnos()
        dict_turnos = {tup[0] : tup[1] for tup in turnos_values}
        disponibilidades_values = self.controlador.obtener_disponibilidades()
        dict_disponibilidades = {tup[0] : tup[1] for tup in disponibilidades_values}
        # END
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        telefono = self.entry_telefono.get()
        rol = next((key for key, value in dict_roles.items() if value == self.combobox_id_rol.get()), None)
        turno = next((key for key, value in dict_turnos.items() if value == self.combobox_id_turno.get()), None)
        disponibilidad = next((key for key, value in dict_disponibilidades.items() if value == self.combobox_id_disponibilidad.get()), None)
        mapeo_modalidad = {'Presencial': 1, 'Virtual': 2} # Para devolverle al SQL un 1 o 2 dependiendo de la modalidad que tiene el combobox
        modalidad = mapeo_modalidad.get(self.combobox_modalidad.get(), None)
        label_values = (nombre, correo, telefono, rol, turno, disponibilidad, modalidad)
        if nombre and correo and telefono and rol and turno and disponibilidad and modalidad:
            #Validacion datos de nombre y telefono
            regex_nombre = r"^[a-zA-Z ,.'-]+$"
            if not (re.fullmatch(regex_nombre, nombre)):
                messagebox.showerror("Error", "Por favor digite un nombre válido")
                return
            regex_correo = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
            if not (re.fullmatch(regex_correo, correo)):
                messagebox.showerror("Error", "Por favor digite un correo válido")
                return
            regex_telefono = r"[0-9]{4}(-)?[0-9]{4}"
            if not (re.fullmatch(regex_telefono, telefono)):
                messagebox.showerror("Error", "Por favor digite un número de teléfono válido")
                return
            res_comprobacion_correo = self.controlador.comprobar_correo_colaborador(correo)
            #print(res_comprobacion_correo)
            if not res_comprobacion_correo:
                estado_consulta = self.controlador.agregar_colaborador(
                    nombre, correo, telefono, rol, turno, disponibilidad, modalidad
                )
                if estado_consulta:
                    messagebox.showinfo("Éxito", "Colaborador agregado con éxito")
                    self.actualizar_lista_colaboradores()
                    self.entry_nombre.delete(0, tk.END)
                    self.entry_correo.delete(0, tk.END)
                    self.entry_telefono.delete(0, tk.END)
                    self.combobox_id_rol.delete(0, tk.END)
                    self.combobox_id_turno.delete(0, tk.END)
                    self.combobox_id_disponibilidad.delete(0, tk.END)
                    self.combobox_modalidad.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Hubo un problema al agregar el colaborador")
            else:
                messagebox.showerror("Error", "Ya hay un colaborador con ese correo asociado")
        else:
            messagebox.showerror("Error", "Debe rellenar todos los campos")
           
    def actualizar_lista_colaboradores(self):
        colaboradores = self.controlador.obtener_colaboradores_bonito()
        self.tree.delete(*self.tree.get_children())
        for i, colaborador in enumerate(colaboradores):
            etiqueta_estilo = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", values=colaborador, tags=(etiqueta_estilo,))

    def filtrar_lista_colaboradores(self, event):
        filtro_seleccionado = self.combobox_filtro_colaborador.get()
        if filtro_seleccionado == 'Todos':
            self.actualizar_lista_colaboradores()
        else:
            # Hay que diferenciar el filtro del valor
            filtros = self.controlador.obtener_filtros_colaborador()
            dict_filtros = {'Todos': -1}
            filtros_bd = {tup[0] : tup[1] for tup in filtros}
            dict_filtros.update(filtros_bd)
            
            filtro = filtro_seleccionado.split(':')[0].strip() # Primero saber cuál tabla
            match filtro:
                case 'Rol':
                    filtro = 'C.ID_Rol'
                case 'Turno':
                    filtro = 'C.ID_Turno'
                case 'Disponibilidad':
                    filtro = 'C.ID_Disponibilidad'
                case 'Modalidad':
                    filtro = 'C.Modalidad'
            valor = dict_filtros.get(filtro_seleccionado) # el valor es el ID de la tabla del filtro
            
            print("Filtro y valor:", filtro, valor)
            colaboradores_filtrados = self.controlador.filtrar_colaboradores(filtro, valor)
            self.tree.delete(*self.tree.get_children())
            for i, colaborador in enumerate(colaboradores_filtrados):
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
            self.combobox_id_rol.delete(0, tk.END)
            self.combobox_id_rol.insert(0, values[4])
            self.combobox_id_turno.delete(0, tk.END)
            self.combobox_id_turno.insert(0, values[5])
            self.combobox_id_disponibilidad.delete(0, tk.END)
            self.combobox_id_disponibilidad.insert(0, values[6])
            self.combobox_modalidad.delete(0, tk.END)
            self.combobox_modalidad.insert(0, values[7])
            
    def eliminar_colaborador(self):
        id_colaborador = self.label_info_id.cget("text")
        if id_colaborador:
            estado_consulta = self.controlador.eliminar_colaborador(id_colaborador)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Colaborador eliminado con éxito")
                self.actualizar_lista_colaboradores()
                self.label_info_id.config(text="")
                self.entry_nombre.delete(0, tk.END)
                self.entry_correo.delete(0, tk.END)
                self.entry_telefono.delete(0, tk.END)
                self.combobox_id_rol.delete(0, tk.END)
                self.combobox_id_turno.delete(0, tk.END)
                self.combobox_id_disponibilidad.delete(0, tk.END)
                self.combobox_modalidad.delete(0, tk.END)
            else: 
                messagebox.showerror("Error", "Hubo un problema al eliminar el colaborador")
        else:
            messagebox.showerror("Error", "Debe seleccionar un colaborador")

    def actualizar_colaborador(self):
        # Para la conversion de texto a ID
        roles_values = self.controlador.obtener_roles()
        dict_roles = {tup[0] : tup[1] for tup in roles_values}
        turnos_values = self.controlador.obtener_turnos()
        dict_turnos = {tup[0] : tup[1] for tup in turnos_values}
        disponibilidades_values = self.controlador.obtener_disponibilidades()
        dict_disponibilidades = {tup[0] : tup[1] for tup in disponibilidades_values}
        # END
        id_colaborador = self.label_info_id.cget("text")
        nombre = self.entry_nombre.get()
        correo = self.entry_correo.get()
        telefono = self.entry_telefono.get()
        rol = next((key for key, value in dict_roles.items() if value == self.combobox_id_rol.get()), None)
        turno = next((key for key, value in dict_turnos.items() if value == self.combobox_id_turno.get()), None)
        disponibilidad = next((key for key, value in dict_disponibilidades.items() if value == self.combobox_id_disponibilidad.get()), None)
        mapeo_modalidad = {'Presencial': 1, 'Virtual': 2} # Para devolverle al SQL un 1 o 2 dependiendo de la modalidad que tiene el combobox
        modalidad = mapeo_modalidad.get(self.combobox_modalidad.get(), None)
        if id_colaborador:
            estado_consulta= self.controlador.actualizar_colaborador(
                nombre, correo, telefono, rol, turno, disponibilidad, modalidad, id_colaborador
            )
            if estado_consulta:
                messagebox.showinfo("Éxito", "Colaborador actualizado con éxito")
                self.actualizar_lista_colaboradores()
                self.label_info_id.config(text="")
                self.entry_nombre.delete(0, tk.END)
                self.entry_correo.delete(0, tk.END)
                self.entry_telefono.delete(0, tk.END)
                self.combobox_id_rol.delete(0, tk.END)
                self.combobox_id_turno.delete(0, tk.END)
                self.combobox_id_disponibilidad.delete(0, tk.END)
                self.combobox_modalidad.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar el colaborador")
        else:
            messagebox.showerror("Error", "Debe seleccionar un colaborador")

    def limpiar_datos_colaborador(self):     
        self.actualizar_lista_colaboradores()
        self.label_info_id.config(text="")
        self.entry_nombre.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.combobox_id_rol.delete(0, tk.END)
        self.combobox_id_turno.delete(0, tk.END)
        self.combobox_id_disponibilidad.delete(0, tk.END)
        self.combobox_modalidad.delete(0, tk.END) 

    def regresar_colaboradores(self):
        self.ventana_colaboradores.destroy()
        self.ventana_opcionesColaborador.deiconify()   

#-------HORARIO--------
    def obtener_colaboradores_disponibles(self):
        print(self.controlador.generar_horario())

    def abrir_ventana_horario(self, tipo_usuario):
        if tipo_usuario == "usuario":
            self.ventana_login.withdraw()
        elif tipo_usuario == "administrador":
            self.ventana_opcionesHorario.withdraw()

        self.ventana_horario = tk.Tk()
        self.ventana_horario.title("Horario")
        self.ventana_horario.geometry('900x620')
        self.ventana_horario.resizable(width=False, height=False)

        self.label_dia = ttk.Label(self.ventana_horario, text="Dia Semana:")
        self.label_dia.place(x=170, y=20)
        self.label_info_dia = ttk.Label(self.ventana_horario, text="")
        self.label_info_dia.place(x=280, y=20)

        self.label_ingreso = ttk.Label(self.ventana_horario, text="Ingreso :")
        self.label_ingreso.place(x=170, y=60)
        self.label_info_ingreso = ttk.Label(self.ventana_horario, text="")
        self.label_info_ingreso.place(x=280, y=60)
        

        self.label_salida = ttk.Label(self.ventana_horario, text="Salida :")
        self.label_salida.place(x=170, y=100)
        self.label_info_salida = ttk.Label(self.ventana_horario, text="")
        self.label_info_salida.place(x=280, y=100)

        self.label_prof1 = ttk.Label(self.ventana_horario, text="Profiláctico 1:")
        self.label_prof1.place(x=170, y=140)
        self.entry_prof1 = ttk.Entry(self.ventana_horario)
        self.entry_prof1.place(x=280, y=140)

        self.label_prof2 = ttk.Label(self.ventana_horario, text="Profiláctico 2:")
        self.label_prof2.place(x=170, y=180)
        self.entry_prof2 = ttk.Entry(self.ventana_horario)
        self.entry_prof2.place(x=280, y=180)
        
        self.label_prof3 = ttk.Label(self.ventana_horario, text="Profiláctico 3:")
        self.label_prof3.place(x=170, y=220)
        self.entry_prof3 = ttk.Entry(self.ventana_horario)
        self.entry_prof3.place(x=280, y=220)

        self.label_almuerzo = ttk.Label(self.ventana_horario, text="Almuerzo:")
        self.label_almuerzo.place(x=170, y=260)
        self.entry_almuerzo = ttk.Entry(self.ventana_horario)
        self.entry_almuerzo.place(x=280, y=260)

        self.label_horasExtra = ttk.Label(self.ventana_horario, text="Horas Extra:")
        self.label_horasExtra.place(x=170, y=300)
        self.entry_horasExtra = ttk.Entry(self.ventana_horario)
        self.entry_horasExtra.place(x=280, y=300)

        self.label_colaborador = ttk.Label(self.ventana_horario, text="Colaborador:")
        self.label_colaborador.place(x=570, y=40)

        datos_colaborador = self.controlador.obtener_colaboradores_nombre_id()
        self.id_seleccionado = tk.StringVar()
        self.combobox_colaborador = ttk.Combobox(self.ventana_horario, values=datos_colaborador, state="readonly")
        self.combobox_colaborador.place(x=570, y=60)

        self.crear_boton(self.ventana_horario, x=570, y=90, text="Visualizar Horario", command=self.rellenar_horario)
        self.crear_boton(self.ventana_horario, x=570, y=130, text="Limpiar Datos", command=self.limpiar_datos_horario)
        self.crear_boton(self.ventana_horario, x=570, y=170, text="Reporte General", command=self.generar_archivo_horario_completo)
        self.crear_boton(self.ventana_horario, x=570, y=210, text="Reporte Individual", command=self.generar_archivo_horario_individual)
        
        if tipo_usuario == "administrador":
            self.crear_boton(self.ventana_horario, x=570, y=250, text="Actualizar Horario", command=self.actualizar_horario)

        self.campos_horario = ["","Hora Ingreso","Hora Salida", "Profiláctico 1", "Profiláctico 2","Profiláctico 3", "Almuerzo", "Horas Extra"]
        self.dias_semana = ["","Lunes", "Martes", "Miércoles", "Jueves", "Viernes","Sabado","Domingo"]

        self.tree = ttk.Treeview(self.ventana_horario, columns=self.campos_horario, show="headings", height=7)
        for col in self.campos_horario:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)  

        for dias_semana in self.dias_semana:
            self.tree.insert("", "end", values=[dias_semana] + [""] * len(self.campos_horario))
        self.tree.place(x=50, y=360)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_campos_horario)

        if tipo_usuario =="administrador":
            self.crear_boton(self.ventana_horario, x=380, y=550, text="Regresar", command=self.regresar_Horario)
        self.ventana_horario.mainloop()

    def regresar_Horario(self):
        self.ventana_horario.destroy()
        self.ventana_menuPrincipal.deiconify()

    def seleccionar_campos_horario(self, event):
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, "values")
            self.label_info_dia.config(text = values[0])
            self.label_info_ingreso.config(text = values[1])
            self.label_info_salida.config(text = values[2])
            self.entry_prof1.delete(0, tk.END)
            self.entry_prof1.insert(0, values[3])  
            #self.entry_prof1.config(state="readonly")
            self.entry_prof2.delete(0, tk.END)
            self.entry_prof2.insert(0, values[4])  
            #self.entry_prof2.config(state="readonly")
            self.entry_prof3.delete(0, tk.END)
            self.entry_prof3.insert(0, values[5])  
            self.entry_almuerzo.delete(0, tk.END)
            self.entry_almuerzo.insert(0, values[6])  
            #self.entry_almuerzo.config(state="readonly")
            self.entry_horasExtra.delete(0, tk.END)
            self.entry_horasExtra.insert(0, values[7])  

    def actualizar_horario(self):
        seleccion = self.combobox_colaborador.get()
        id_colaborador = int(seleccion.split(" ")[0])
        dia_semana = self.label_info_dia.cget("text")
        prof1 = self.entry_prof1.get()
        prof2 = self.entry_prof2.get()
        prof3 = self.entry_prof3.get()
        almuerzo = self.entry_almuerzo.get()
        horas_extra = self.entry_horasExtra.get()
        if id_colaborador:
            estado_consulta = self.controlador.actualizar_horario(id_colaborador, dia_semana, prof1, prof2, prof3, almuerzo, horas_extra)
            if estado_consulta:
                messagebox.showinfo("Éxito", "Horario actualizado con éxito")
                self.rellenar_horario()
                #self.entry_ingreso.delete(0, tk.END)
                #self.entry_salida.delete(0, tk.END)
                self.entry_prof1.delete(0, tk.END)
                self.entry_prof2.delete(0, tk.END)
                self.entry_prof3.delete(0, tk.END)
                self.entry_almuerzo.delete(0, tk.END)
                self.entry_horasExtra.delete(0, tk.END)
                 
            else:
                messagebox.showerror("Error", "Hubo un problema al actualizar el horario")
        else:
            messagebox.showerror("Error", "Debe seleccionar un dia de la semana")

    def rellenar_horario(self):
        seleccion = self.combobox_colaborador.get()
        id_colaborador = int(seleccion.split(" ")[0])
        horario_colaborador = self.controlador.obtener_horario_colaborador2(id_colaborador)
        self.tree.delete(*self.tree.get_children())
        for i, dia in enumerate(horario_colaborador):
            
            self.tree.insert("", "end", values=dia)
    
    def limpiar_datos_horario(self):     
        #self.actualizar_horario()
        self.label_info_dia.config(text="")
        self.label_info_ingreso.config(text="")
        self.label_info_salida.config(text="")
        self.entry_prof1.delete(0, tk.END)
        self.entry_prof2.delete(0, tk.END)
        self.entry_prof3.delete(0, tk.END)  
        self.entry_almuerzo.delete(0, tk.END)
        self.entry_horasExtra.delete(0, tk.END)

    def generar_archivo_horario_completo(self):
        self.controlador.generar_archivo_horario_completo()

    def generar_archivo_horario_individual(self):
        seleccion = self.combobox_colaborador.get()
        id_colaborador = int(seleccion.split(" ")[0])
        self.controlador.generar_archivo_horario_individual(id_colaborador)

        

#-------OTROS-----------

    def iniciar_aplicacion(self):
        self.ventana_login.mainloop()
    
    def abrir_ventana_explorador_archivos(self):
        tk.Tk().withdraw()
        filename = askopenfilename()
        res_operacion = self.controlador.cargar_lista_colaboradores(filename)
        if not res_operacion:
            messagebox.showerror("Error", "Hubo un problema al agregar colaboradores")
