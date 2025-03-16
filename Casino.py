import tkinter as tk
from login import sistema_Login

def iniciar_app():
    app = tk.Tk()
    app.title("Casino Fiesta Latino") 
    app.geometry("800x600")
    app.resizable(False, False)
    app.configure(bg="#161515")
    app.iconbitmap("assets/casino.ico")

    sistema_Login(app)
    app.mainloop()

if __name__ == "__main__":
    iniciar_app()