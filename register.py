import tkinter as tk

def guardar_Informacion():
    usuario = usuario_box.get()
    clave = clave_box.get()
    
    if edad_box.get()=="":
        edad=0
    else:
        edad = int(edad_box.get())
    str_edad = edad_box.get()

    if usuario == "" and clave == "" and str_edad == "":
        check.config(text="¡Por favor llena todos los campos!",font=("Arial",11,"bold"),bg="#161515",fg="red")
    elif usuario == "":
        check.config(text="¡Crea un usuario!",font=("Arial",11,"bold"),bg="#161515",fg="red")
    elif clave == "":
        check.config(text="¡Crea una contraseña!",font=("Arial",11,"bold"),bg="#161515",fg="red")
    elif usuario == clave:
        check.config(text="¡No puedes colocar el mismo usuario en la contraseña!",font=("Arial",11,"bold"),bg="#161515",fg="red")
    elif str_edad == "":
        check.config(text="¡Coloca tu edad!",font=("Arial",11,"bold"),bg="#161515",fg="red")    
    elif edad < 18:
        check.config(text="¡No cumples con el rango minimo de edad!",font=("Arial",11,"bold"),bg="#161515",fg="red")
    else:
        check.config(text="¡Usuario registrado con exito!",font=("Arial",11,"bold"),bg="#161515",fg="green")
        from Explorador import guardar_Usuarios
        guardar_Usuarios(usuario,clave,edad)
        

def limpiar_Widgets(app):
    for widget in app.winfo_children():
        widget.pack_forget()

def ver_Login(app):
    limpiar_Widgets(app)  
    from login import sistema_Login 
    sistema_Login(app)

def register(app):
    global usuario_box,clave_box,check,edad_box

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    crear_Cuenta = tk.Label(app, text="Crear Cuenta",font=("Arial",20,"bold"),bg="#161515",fg="white")
    crear_Cuenta.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    user = tk.Label(app, text="Usuario",font=("Arial",16,"bold"),bg="#161515",fg="white")
    user.pack()

    usuario_box = tk.Entry(app,font=("Arial",12),width=20)
    usuario_box.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    clave = tk.Label(app, text="Contraseña",font=("Arial",16,"bold"),bg="#161515",fg="white")
    clave.pack()

    clave_box = tk.Entry(app,font=("Arial",12),width=20)
    clave_box.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    edad = tk.Label(app, text="Edad",font=("Arial",16,"bold"),bg="#161515",fg="white")
    edad.pack()

    edad_box = tk.Entry(app,font=("Arial",12),width=20)
    edad_box.pack()
   
    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    boton_save = tk.Button(app, text="Registrar",font=("Arial",12,"bold"),width=18,bg="#161515",fg="white",command=guardar_Informacion)
    boton_save.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    boton_back = tk.Button(app, text="Volver al loguearse",font=("Arial",12,"bold"),width=18,bg="#161515",fg="white",command=lambda: ver_Login(app))
    boton_back.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    check = tk.Label(app,bg="#161515",fg="white")
    check.pack()