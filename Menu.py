import tkinter as tk

def limpiar_Widget(app):
    for widget in app.winfo_children():
        widget.pack_forget()

def ver_Login(app):
    limpiar_Widget(app)  
    from login import sistema_Login 
    sistema_Login(app)

def ver_informacion(app):
    limpiar_Widget(app)
    from Informacion import menu_Informacion
    menu_Informacion(app)

def ver_dev(app):
    limpiar_Widget(app)
    from Informacion import info_Dev
    info_Dev(app)

def ver_Dificultades(app):
    limpiar_Widget(app)
    from Dificultad import difficulty_selection
    difficulty_selection(app)

def menu_Principal(app):

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonJugar = tk.Button(app,text="Jugar",font=("Arial",12,"bold"),width=20,bg="#161515",fg="white",command=lambda: ver_Dificultades(app))
    botonJugar.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSobreElDev = tk.Button(app, text="Sobre el desarrollador",font=("Arial",12,"bold"),width=20,bg="#161515",fg="white",command=lambda: ver_dev(app))
    botonSobreElDev.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonAcercaDeLasDifi = tk.Button(app, text="Acerca de las dificultades",font=("Arial",12,"bold"),width=20,bg="#161515",fg="white",command=lambda: ver_informacion(app))
    botonAcercaDeLasDifi.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonCerrarSesion = tk.Button(app, text="Cerrar Sesión",font=("Arial",12,"bold"),width=20,bg="#161515",fg="white",command=lambda: ver_Login(app))
    botonCerrarSesion.pack()
    
    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app, text="Salir",font=("Arial",12,"bold"),width=20,bg="#161515",fg="white",command= app.destroy)
    botonSalir.pack()
    