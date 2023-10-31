import http.client
import urllib.parse
import time
import config_client

def enviar_cadena(cadena):
    """
    Sends a string to the server for processing.
    
    :param cadena: The string to be sent
    :return: The server's response as a string
    """
    cadena = cadena.strip()
    
    # Validate the string before sending
    if not es_cadena_valida(cadena):
        return f"Error: La cadena no es válida - '{cadena}'"
    
    # Prepare the data for sending
    params = urllib.parse.urlencode({'cadena': cadena})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    
    # Establish a connection and send the request
    conn = http.client.HTTPConnection(config_client.SERVER_IP, config_client.SERVER_PORT, timeout=10)
    conn.request("POST", "/", params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    
    return data.decode("utf-8")

def es_cadena_valida(cadena):
    """
    Validates a string based on certain criteria.
    
    :param cadena: The string to be validated
    :return: True if the string is valid, False otherwise
    """
    if not cadena:
        return False
    if len(cadena) < config_client.MIN_CADENA_LONGITUD or len(cadena) > config_client.MAX_CADENA_LONGITUD:
        return False
    for char in config_client.CARACTERES_NO_PERMITIDOS:
        if char in cadena:
            return False
    return True

if __name__ == "__main__":
    # Open the file to write the responses
    with open(config_client.RESPONSES_FILE_PATH, "w") as f:
        # Read the strings from the file
        with open(config_client.CHAINS_FILE_PATH, "r") as file:
            lineas = file.readlines()
            for i, linea in enumerate(lineas, start=1):
                # Send each string to the server and write the response to the file
                respuesta = enviar_cadena(linea)
                f.write(f"Linea {i}: {linea.strip()} - Ponderación: {respuesta}\n")
                print(f"Linea {i}: {linea.strip()} - Ponderación: {respuesta}")
                time.sleep(config_client.DELAY_ENTRE_PETICIONES)