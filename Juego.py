import random
import time
import tkinter as tk

def limpiar_Widgets(app):
    for widget in app.winfo_children():
        widget.pack_forget()

def ver_MenuPrincipal(app):
    limpiar_Widgets(app)  
    from Menu import menu_Principal 
    menu_Principal(app)

def juego_Principal(app,difi):
    dificultad = difi 

    numero_Aleatorio = [random.randint(1,15),random.randint(1,35),random.randint(1,50),random.randint(1,100),random.randint(1,200)]
    
    config_Dificultad = {
        "facil": (4, numero_Aleatorio[0], "15" , "Fácil",),
        "normal": (6, numero_Aleatorio[1], "35" , "Normal"),
        "dificil": (5, numero_Aleatorio[2], "50" , "Difícil"),
        "extremo": (6, numero_Aleatorio[3], "100" , "Extremo"),
        "infierno": (7, numero_Aleatorio[4], "200" , "Infierno")} 

    if dificultad in config_Dificultad:
        max_Intentos, num_Aleatorio, cantidad, inf_dificultad = config_Dificultad[dificultad]

    iniciar_Temporizador = time.time()

    def ganar(app):

        terminar_Temporizador = time.time()
        temporizador = terminar_Temporizador - iniciar_Temporizador
        
        vacio = tk.Label(app,text="",bg="#161515")
        vacio.pack()

        casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
        casino.pack()

        vacio = tk.Label(app,text="",bg="#161515")
        vacio.pack()

        wiin = tk.Label(app,text="¡Ganaste!",font=("Arial",20,"bold"),bg="#161515",fg="green")
        wiin.pack()

        vacio = tk.Label(app,text="",bg="#161515")
        vacio.pack()
        
        etiquetaTimer = tk.Label(app,text=f"Tiempo trascurrido: {temporizador:.0f} segundos",font=("Arial",12,"bold"),bg="#161515",fg="white")
        etiquetaTimer.pack()

        vacio = tk.Label(app,text="",bg="#161515")
        vacio.pack()

        etiquetaIntent = tk.Label(app,text=f"Intentos usados: {str(contador)} de {max_Intentos}",font=("Arial",12,"bold"),bg="#161515",fg="white")
        etiquetaIntent.pack()

        vacio = tk.Label(app,text="",bg="#161515")
        vacio.pack()

        from Apuesta import saldo_Usuario, int_apuesta
        etiquetaApu = tk.Label(app,text=f"Apuesta realizada: {int_apuesta}$",font=("Arial",12,"bold"),bg="#161515",fg="white")
        etiquetaApu.pack()

        vacio = tk.Label(app,text="",bg="#161515")
        vacio.pack()
       
        etiquetaNumeroCorrecto = tk.Label(app,text=f"Numero correcto: {num_Aleatorio}",font=("Arial",12,"bold"),bg="#161515",fg="white")
        etiquetaNumeroCorrecto.pack()

        vacio = tk.Label(app,text="",bg="#161515")
        vacio.pack()
        
        saldo_Usuario = saldo_Usuario+(int_apuesta*2)
        etiquetaSaldo = tk.Label(app,text=f"Saldo actual: {saldo_Usuario}$",font=("Arial",12,"bold"),bg="#161515",fg="white")
        etiquetaSaldo.pack()

        vacio = tk.Label(app,text="",bg="#161515")
        vacio.pack()

        botonSalir = tk.Button(app,text="Volver al menu",font=("Arial",12,"bold"),width=20,bg="#161515",fg="white", command=lambda: ver_MenuPrincipal(app))
        botonSalir.pack()
        

    def perder(app):
    
        respuesta = int(respuesta_box.get())
        if contador == max_Intentos:
            limpiar_Widgets(app)

            terminar_Temporizador = time.time()
            temporizador = terminar_Temporizador - iniciar_Temporizador
            
            vacio = tk.Label(app,text="",bg="#161515")
            vacio.pack()

            casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
            casino.pack()

            vacio = tk.Label(app,text="",bg="#161515")
            vacio.pack()

            wiin = tk.Label(app,text="¡Perdiste!",font=("Arial",20,"bold"),bg="#161515",fg="red")
            wiin.pack()

            vacio = tk.Label(app,text="",bg="#161515")
            vacio.pack()
            
            etiquetaTimer = tk.Label(app,text=f"Tiempo trascurrido: {temporizador:.0f} segundos",font=("Arial",12,"bold"),bg="#161515",fg="white")
            etiquetaTimer.pack()

            vacio = tk.Label(app,text="",bg="#161515")
            vacio.pack()

            etiquetaIntent = tk.Label(app,text=f"Intentos usados: {str(contador)} de {max_Intentos}",font=("Arial",12,"bold"),bg="#161515",fg="white")
            etiquetaIntent.pack()

            vacio = tk.Label(app,text="",bg="#161515")
            vacio.pack()

            etiquetaNumeroCorrecto = tk.Label(app,text=f"Numero correcto: {num_Aleatorio}",font=("Arial",12,"bold"),bg="#161515",fg="white")
            etiquetaNumeroCorrecto.pack()

            vacio = tk.Label(app,text="",bg="#161515")
            vacio.pack()
        
            from Apuesta import saldo_Usuario, int_apuesta
            etiquetaApu = tk.Label(app,text=f"Apuesta realizada: {int_apuesta}$",font=("Arial",12,"bold"),bg="#161515",fg="white")
            etiquetaApu.pack()

            vacio = tk.Label(app,text="",bg="#161515")
            vacio.pack()

            saldo_Usuario = saldo_Usuario-int_apuesta
            etiquetaSaldo = tk.Label(app,text=f"Saldo actual: {saldo_Usuario}$",font=("Arial",12,"bold"),bg="#161515",fg="white")
            etiquetaSaldo.pack()

            vacio = tk.Label(app,text="",bg="#161515")
            vacio.pack()

            botonSalir = tk.Button(app,text="Volver al menu",font=("Arial",12,"bold"),width=20,bg="#161515",fg="white", command=lambda: ver_MenuPrincipal(app))
            botonSalir.pack()
        else:

            if  respuesta > num_Aleatorio:
            
                check.config(text=f"¡Incorrecto, El numero es menor a {respuesta}!",font=("Arial",11,"bold"),bg="#161515",fg="red")
                check.pack()
            else:
                check.config(text=f"¡Incorrecto, El numero es mayor a {respuesta}!",font=("Arial",11,"bold"),bg="#161515",fg="red")
                check.pack()

    global contador
    contador = 1

    def verificar_Respuesta(app):
        
        if respuesta_box.get() == "":
            int_Respuesta = 0
        else:
            int_Respuesta = int(respuesta_box.get())

        str_Respuesta = str(respuesta_box.get())

        global contador

        if str_Respuesta == "" or int_Respuesta == 0:
            pass
        else:
            contador += 1
            etiquetaIntentos.config(text=f"Intento numero {str(contador)} de {max_Intentos}")

        if int_Respuesta == 0:
            check.config(text="¡Coloca un numero igual o mayor a 1!",font=("Arial",11,"bold"),bg="#161515",fg="red")
        elif str_Respuesta == "":
            check.config(text="¡Coloca un numero igual o mayor a 1!",font=("Arial",11,"bold"),bg="#161515",fg="red")
        elif int_Respuesta == num_Aleatorio:
            limpiar_Widgets(app)
            ganar(app)
        else:
            perder(app)
        
            
    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    casino = tk.Label(app,text="Casino Fiesta Latino",font=("Arial",24,"bold"),bg="#161515",fg="white")
    casino.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    etiquetaNum = tk.Label(app,text=f"Adivina un numero aleatorio del 1 al {cantidad}",font=("Arial",12,"bold"),bg="#161515",fg="white")
    etiquetaNum.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    etiquetaPartida = tk.Label(app,text=f"En la partida pasada: En desarrollo",font=("Arial",12,"bold"),bg="#161515",fg="white")
    etiquetaPartida.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    etiquetaIntentos = tk.Label(app,text=f"Intento numero {contador} de {max_Intentos}",font=("Arial",12,"bold"),bg="#161515",fg="white")
    etiquetaIntentos.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    etiquetaDifi = tk.Label(app,text=f"Dificultad: {inf_dificultad}",font=("Arial",12,"bold"),bg="#161515",fg="white")
    etiquetaDifi.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    respuesta_box = tk.Entry(app,width=15, font=("Arial",12))
    respuesta_box.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonRespuesta = tk.Button(app,text="Enviar respuesta",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: verificar_Respuesta(app))
    botonRespuesta.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    botonSalida = tk.Button(app,text="Salir de la partida",font=("Arial",12,"bold"),width=15,bg="#161515",fg="white",command=lambda: ver_MenuPrincipal(app))
    botonSalida.pack()

    vacio = tk.Label(app,text="",bg="#161515")
    vacio.pack()

    #debug_Num = tk.Label(app,text=f"Numero correcto: {num_Aleatorio}",font=("Arial",12,"bold"),bg="#161515",fg="white")
    #debug_Num.pack()

    check = tk.Label(app,text="",bg="#161515")
    check.pack()