import tkinter as tk

global saldo_Usuario
saldo_Usuario = 30

def limpiar_Widgets(app):
    for widget in app.winfo_children():
        widget.pack_forget()

def ver_MenuPrincipal(app):
    limpiar_Widgets(app)
    from Menu import menu_Principal 
    menu_Principal(app)

def ver_Juego(app,difi):
    limpiar_Widgets(app)
    from Juego import juego_Principal
    juego_Principal(app,difi)

def apuesta_Verificar(app,difi):
    global int_apuesta

    if apuesta_box.get() == "":
        int_apuesta = 0
    else:
        int_apuesta = int(apuesta_box.get())
    
    str_apuesta = str(apuesta_box.get())

    if int_apuesta > saldo_Usuario:
        check.config(text="¡No tienes suficientes fondos para apostar!",bg="#161515",fg="red",font=("Arial",11,"bold"))
    elif int_apuesta == 0:
        check.config(text="¡No se puede apostar 0$!",bg="#161515",fg="red",font=("Arial",11,"bold"))
    elif str_apuesta == "":
        check.config(text="¡Debes de apostar!",bg="#161515",fg="red",font=("Arial",11,"bold"))
    else:
        ver_Juego(app,difi)


def apuesta(app,difi):
    global apuesta_box, check

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    apuesta = tk.Label(app, text="Menu de Apuesta",font=("Arial",20,"bold"),bg="#161515",fg="white")
    apuesta.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    etiquetaApuesta = tk.Label(app, text="¿Cuanto dinero deseas apostar?",font=("Arial",12,"bold"),bg="#161515",fg="white")
    etiquetaApuesta.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    etiquetaSaldo = tk.Label(app, text=f"Saldo actual: {saldo_Usuario}$",font=("Arial",12,"bold"),bg="#161515",fg="white")
    etiquetaSaldo.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    apuesta_box = tk.Entry(app,width=15, font=("Arial",12))
    apuesta_box.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonApostar = tk.Button(app, text="Apostar",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white", command=lambda: apuesta_Verificar(app,difi))
    botonApostar.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app, text="Volver al menu",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white", command=lambda: ver_MenuPrincipal(app))
    botonSalir.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    check = tk.Label(app,text="",bg="#161515")
    check.pack()