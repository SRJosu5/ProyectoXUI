import tkinter as tk

def limpiar_Widgets(app):
    for widget in app.winfo_children():
        widget.pack_forget()

def ver_MenuPrincipal(app):
    limpiar_Widgets(app)  
    from Menu import menu_Principal 
    menu_Principal(app)

def info_Facil(app):
    limpiar_Widgets(app)

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    facil = tk.Label(app, text="Acerca de Facil",font=("Arial",20,"bold"),bg="#161515",fg="white")
    facil.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    frame = tk.Frame(app,bg="#404b62",padx=10,pady=10,bd=2,relief="solid")
    frame.pack(padx=15,pady=15)

    info_Facil = "¿Crees que tienes suerte? En este modo, tendrás que adivinar un número entre 1 y 15. Tienes 4 intentos para lograrlo. Si aciertas, no solo recuperarás tu dinero, sino que también ganarás 10$ extra. Pero si fallas, perderás lo que apostaste. ¿Te atreves?"

    etiquetaFacil = tk.Label(frame,text=info_Facil,font=("Arial",12,"bold"),bg="#161515",fg="white",wraplength=300,justify="left")
    etiquetaFacil.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app,text="Volver al menu",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: ver_MenuPrincipal(app))
    botonSalir.pack()

def info_Normal(app):
    limpiar_Widgets(app)

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    normal = tk.Label(app,text="Acerca de normal",font=("Arial",20,"bold"),bg="#161515",fg="white")
    normal.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    frame = tk.Frame(app,bg="#404b62",padx=10,pady=10,bd=2,relief="solid")
    frame.pack(padx=15,pady=15)

    info_Normal = "El desafío se intensifica. Ahora el número está entre 1 y 35, pero tienes 6 intentos para encontrarlo. Si lo logras, obtendrás 50$ adicionales junto con tu apuesta. Si no, perderás todo. ¿Estás listo para el reto?"

    etiquetaNormal = tk.Label(frame, text=info_Normal,font=("Arial",12,"bold"),bg="#161515",fg="white",wraplength=300,justify="left")
    etiquetaNormal.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app,text="Volver al menu",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: ver_MenuPrincipal(app))
    botonSalir.pack()

def info_Dificil(app):
    limpiar_Widgets(app)

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    dificil = tk.Label(app, text="Acerca de dificil",font=("Arial",20,"bold"),bg="#161515",fg="white")
    dificil.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    frame = tk.Frame(app, bg="#404b62",padx=10,pady=10,bd=2,relief="solid")
    frame.pack(padx=15,pady=15)

    info_Dificil = "Aquí las cosas se ponen serias. El número está entre 1 y 50, y tienes 7 intentos para encontrarlo. Si lo consigues, ganarás 125$ extra además de tu apuesta. Pero si no, será una pérdida total. ¿Aceptas el reto?"

    etiquetaDificil = tk.Label(frame, text=info_Dificil,font=("Arial",12,"bold"),bg="#161515",fg="white",wraplength=300,justify="left")
    etiquetaDificil.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app,text="Volver al menu",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: ver_MenuPrincipal(app))
    botonSalir.pack()

def info_Extremo(app):
    limpiar_Widgets(app)

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    extremo = tk.Label(app, text="Acerca de extremo",font=("Arial",20,"bold"),bg="#161515",fg="white")
    extremo.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    frame = tk.Frame(app, bg="#404b62", padx=10,pady=10,bd=2,relief="solid")
    frame.pack(padx=15,pady=15)

    info_Extremo = "Este no es para cualquiera. El número está entre 1 y 100, y tienes 8 intentos para encontrarlo. Si lo logras, ganarás 300$ adicionales junto con tu apuesta. Pero si fallas, perderás todo. ¿Te sientes con suerte hoy?"

    etiquetaExtremo = tk.Label(frame, text=info_Extremo,font=("Arial",12,"bold"),bg="#161515",fg="white",wraplength=300,justify="left")
    etiquetaExtremo.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app,text="Volver al menu",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: ver_MenuPrincipal(app))
    botonSalir.pack()

def info_Dev(app):

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    devAcerca = tk.Label(app, text="Acerca del desarollador",font=("Arial",20,"bold"),bg="#161515",fg="white")
    devAcerca.pack()

    frame = tk.Frame(app, bg="#404b62", padx=10,pady=10,bd=2,relief="solid")
    frame.pack(padx=15,pady=15)

    info_Dev = "Soy David Cascante, estudiante del CTP Calle Zamora con interés en la programación. Me apasiona Python y siempre busco mejorar mis habilidades en desarrollo y resolución de problemas."

    etiquetaDev = tk.Label(frame, text=info_Dev,font=("Arial",12,"bold"),bg="#161515",fg="white",wraplength=300,justify="left")
    etiquetaDev.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app,text="Volver al menu",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: ver_MenuPrincipal(app))
    botonSalir.pack()
    
def info_Infierno(app):
    limpiar_Widgets(app)

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    infierno = tk.Label(app, text="Acerca de infierno",font=("Arial",20,"bold"),bg="#161515",fg="white")
    infierno.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    frame = tk.Frame(app, bg="#404b62", padx=10,pady=10,bd=2,relief="solid")
    frame.pack(padx=15,pady=15)

    infiernoInfo = "Solo para los valientes. El número está entre 1 y 150, y tienes 10 intentos para encontrarlo. Si lo logras, cuadruplicarás tu apuesta. Pero si fallas, perderás todo. ¿Tienes lo que se necesita para ganar?"

    etiquetaInfierno = tk.Label(frame, text=infiernoInfo,font=("Arial",12,"bold"),bg="#161515",fg="white",wraplength=300,justify="left")
    etiquetaInfierno.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app, text="Volver al menu",font=("Arial",12,"bold"),bg="#161515",fg="white", command=lambda: ver_MenuPrincipal(app))
    botonSalir.pack()

def menu_Informacion(app):

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    acercaDifi = tk.Label(app, text="Acerca de dificultades",font=("Arial",20,"bold"),bg="#161515",fg="white")
    acercaDifi.pack()

    vacio1 = tk.Label(app,text="",bg="#161515")
    vacio1.pack()

    acercaDeFacil = tk.Button(app, text="Facil",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: info_Facil(app))
    acercaDeFacil.pack()

    vacio2 = tk.Label(app,text="",bg="#161515")
    vacio2.pack()
    
    acercaDeNormal = tk.Button(app, text="Normal",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: info_Normal(app))
    acercaDeNormal.pack()

    vacio3 = tk.Label(app,text="",bg="#161515")
    vacio3.pack()
    
    acercaDeDificil = tk.Button(app, text="Dificil",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: info_Dificil(app))
    acercaDeDificil.pack()

    vacio4 = tk.Label(app,text="",bg="#161515")
    vacio4.pack()
    
    acercaDeExtremo = tk.Button(app, text="Extremo",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: info_Extremo(app))
    acercaDeExtremo.pack()

    vacio5 = tk.Label(app,text="",bg="#161515")
    vacio5.pack()

    acercaDeInfierno = tk.Button(app, text="Infierno",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: info_Infierno(app))
    acercaDeInfierno.pack()
    
    vacio6 = tk.Label(app,text="",bg="#161515")
    vacio6.pack()

    botonSalir = tk.Button(app, text="Volver al menu",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: ver_MenuPrincipal(app))
    botonSalir.pack()