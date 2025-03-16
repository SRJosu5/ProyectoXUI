user_database = "data/user_data.txt"

def guardar_Usuarios(nue_usuario,nue_clave,nue_edad):
    with open(user_database, "a") as file:
        file.writelines(f"Usuario:{nue_usuario},Clave:{nue_clave},Edad:{nue_edad}\n")
        
def validacion(usuario,clave):
    with open(user_database, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == f"Usuario:{usuario}" and data[1] == f"Clave:{clave}":
                return True      
    return False