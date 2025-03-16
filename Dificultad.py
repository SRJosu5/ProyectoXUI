import tkinter as tk

def clear_widgets(app):
    for widget in app.winfo_children():
        widget.pack_forget()

def show_main_dash(app):
    clear_widgets(app)  
    from Menu import menu_Principal 
    menu_Principal(app)

def show_facil(app,difi):
    clear_widgets(app)
    from Apuesta import apuesta
    apuesta(app,difi)

def show_normal(app,difi):
    clear_widgets(app)
    from Apuesta import apuesta
    apuesta(app,difi)

def show_dificil(app,difi):
    clear_widgets(app)
    from Apuesta import apuesta
    apuesta(app,difi)

def show_extremo(app,difi):
    clear_widgets(app)
    from Apuesta import apuesta
    apuesta(app,difi)

def show_infierno(app,difi):
    clear_widgets(app)
    from Apuesta import apuesta
    apuesta(app,difi)

def difficulty_selection(app):
    clear_widgets(app)

    vacio = tk.Label(app, text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    dificiultades = tk.Label(app, text="Dificultades", font=("Arial",20,"bold"),bg="#161515",fg="white", width=15)
    dificiultades.pack()

    vacio = tk.Label(app, text="",bg="#161515")
    vacio.pack()

    botonFacil = tk.Button(app, text="Facil", bg="#161515",fg="white",font=("Arial",12,"bold"), width=15, command=lambda: show_facil(app,"facil"))
    botonFacil.pack()

    vacio = tk.Label(app, text="",bg="#161515")
    vacio.pack()

    botonNormal = tk.Button(app, text="Normal", bg="#161515",fg="white",font=("Arial",12,"bold"), width=15, command=lambda: show_normal(app,"normal"))
    botonNormal.pack()

    vacio = tk.Label(app, text="",bg="#161515")
    vacio.pack()

    botonDificil = tk.Button(app, text="Dificil", bg="#161515",fg="white",font=("Arial",12,"bold"), width=15, command=lambda: show_dificil(app,"dificil"))
    botonDificil.pack()

    vacio = tk.Label(app, text="",bg="#161515")
    vacio.pack()

    botonExtremo = tk.Button(app, text="Extremo", bg="#161515",fg="white",font=("Arial",12,"bold"), width=15, command=lambda: show_extremo(app,"extremo"))
    botonExtremo.pack()

    vacio = tk.Label(app, text="",bg="#161515")
    vacio.pack()

    botonInfierno = tk.Button(app, text="Infierno", bg="#161515",fg="white",font=("Arial",12,"bold"), width=15, command=lambda: show_infierno(app,"infierno"))
    botonInfierno.pack()

    vacio = tk.Label(app, text="",bg="#161515")
    vacio.pack()

    botonSalir = tk.Button(app, text="Volver al menu", bg="#161515",fg="white",font=("Arial",12,"bold"), width=15, command=lambda: show_main_dash(app))
    botonSalir.pack()