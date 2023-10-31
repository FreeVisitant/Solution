import http.server
import socketserver
import config_server
import string
import logging
import time
from urllib.parse import parse_qs

# Setting up the logging configuration
logging.basicConfig(filename=config_server.LOGS_DIR + 'server.log', level=logging.INFO)

# RequestHandler class to handle HTTP POST requests
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        start_time = time.time()
        
        # Reading the content length and data from the request
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(data)
        cadena = params.get('cadena', [''])[0]
        
        # Logging the received string
        logging.info(f"Recibida la cadena: '{cadena}'")
        
        # Processing the string and sending the response
        respuesta, metrica = self.procesar_cadena(cadena)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str(respuesta).encode('utf-8'))
        
        # Calculating and logging the processing time
        elapsed_time = time.time() - start_time
        logging.info(f"Procesamiento completado en {elapsed_time:.2f} segundos.")

    def procesar_cadena(self, cadena):
        # Check for 'aa' rule and calculate the string metric
        if "aa" in cadena.lower():
            logging.warning(f"Regla de 'aa' detectada >> '{cadena}'")
            return "1000", 1000
        else:
            letras = sum(c.isalpha() for c in cadena)
            numeros = sum(c.isdigit() for c in cadena)
            espacios = cadena.count(" ")

            if espacios == 0:
                error_message = f"La cadena '{cadena}' no tiene espacios. No se puede calcular la métrica."
                logging.error(error_message)
                return error_message, None

            metrica = (letras * 1.5 + numeros * 2) / espacios
            return str(metrica), metrica

if __name__ == "__main__":
    # Starting the server
    start_time = time.time()
    with socketserver.TCPServer((config_server.SERVER_IP, config_server.SERVER_PORT), RequestHandler) as httpd:
        logging.info(f"Servidor ejecutándose en {config_server.SERVER_IP}:{config_server.SERVER_PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        
    # Calculating and logging the total runtime
    elapsed_time = time.time() - start_time
    logging.info(f"Servidor detenido. Tiempo total de ejecución: {elapsed_time:.2f} segundos.")