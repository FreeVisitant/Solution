import string
import config_client

# Function to validate a single string
def validar_cadena(cadena):
    longitud = len(cadena)
    cantidad_espacios = cadena.count(" ")
    espacios_consecutivos = "  " in cadena
    espacios_inicio_fin = cadena.startswith(" ") or cadena.endswith(" ")
    caracteres_validos = all(caracter in string.ascii_letters + string.digits + " " for caracter in cadena)
    
    return (
        50 <= longitud <= 100 and
        3 <= cantidad_espacios <= 5 and
        not espacios_consecutivos and
        not espacios_inicio_fin and
        caracteres_validos
    )

# Function to validate all the strings in a file
def validar_cadenas(archivo):
    with open(archivo, 'r') as f:
        cadenas = f.readlines()
    
    cadenas_no_validas = []
    for i, cadena in enumerate(cadenas, start=1):
        if not validar_cadena(cadena.strip()):
            cadenas_no_validas.append((i, cadena.strip()))
    
    return cadenas_no_validas

if __name__ == "__main__":
    # Validate all the strings in the file specified in the configuration
    cadenas_no_validas = validar_cadenas(config_client.CHAINS_FILE_PATH)
    if cadenas_no_validas:
        print("Se encontraron cadenas no válidas:")
        for numero_linea, cadena in cadenas_no_validas:
            print(f"Linea {numero_linea}: {cadena}")
    else:
        print("Todas las cadenas son válidas")