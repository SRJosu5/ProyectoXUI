import tkinter as tk

def limpiar_Widgets(app):
    for widget in app.winfo_children():
        widget.pack_forget()

def ver_MenuPrincipal(app):
    limpiar_Widgets(app)
    from Menu import menu_Principal
    menu_Principal(app)

def ver_Register(app):
    limpiar_Widgets(app)
    from register import register
    register(app)

def verificar_Credenciales(app):
    usuario = usuario_box.get()
    clave = clave_box.get()
    
    if usuario == "" and clave == "":
        check.config(text="¡Coloca las credenciales!",font=("Arial",11,"bold"),bg="#161515",fg="red")
    elif usuario == "":
        check.config(text="¡Coloca el usuario!",font=("Arial",11,"bold"),bg="#161515",fg="red")
    elif clave == "":
        check.config(text="¡Coloca una contrasña!",font=("Arial",11,"bold"),bg="#161515",fg="red")
    else:
        from Explorador import validacion
        if validacion(usuario,clave):
            ver_MenuPrincipal(app)
        else:
            check.config(text="¡Usuario o contraseña incorrecta!",font=("Arial",11,"bold"),bg="#161515",fg="red")

def sistema_Login(app):
    global usuario_box,clave_box,check

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app, text="Casino Fiesta Latino", font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    login = tk.Label(app,text="Login",font=("Arial",20,"bold"),bg="#161515",fg="white")
    login.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    usuario = tk.Label(app,text="Usuario",font=("Arial",16,"bold"),bg="#161515",fg="white")
    usuario.pack()

    usuario_box = tk.Entry(app,font=("Arial",12),width=20)
    usuario_box.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    clave = tk.Label(app,text="Contraseña",font=("Arial",16,"bold"),bg="#161515",fg="white")
    clave.pack()

    clave_box = tk.Entry(app,font=("Arial",12),width=20)
    clave_box.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    boton_IniciarSesion = tk.Button(app,text="Iniciar sesion",font=("Arial",12,"bold"),width=18,bg="#161515",fg="white",command=lambda: verificar_Credenciales(app))
    boton_IniciarSesion.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    boton_register = tk.Button(app,text="Registrarme",font=("Arial",12,"bold"),width=18,bg="#161515",fg="white",command=lambda: ver_Register(app))
    boton_register.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app, text="Salir",font=("Arial",12,"bold"),width=18,bg="#161515",fg="white",command= app.destroy)
    botonSalir.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    check = tk.Label(app,bg="#161515",fg="white")
    check.pack()