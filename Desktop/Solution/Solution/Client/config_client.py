# Client Configuration

# IP address of the server to which the client will connect
SERVER_IP = '127.0.0.1'

# Port number of the server to which the client will connect
SERVER_PORT = 65432

# File path for the text file containing the generated strings
CHAINS_FILE_PATH = 'chains.txt'

# File path for the text file where the responses from the server will be stored
RESPONSES_FILE_PATH = 'responses.txt'

# Number of strings to generate and send to the server
NUM_CHAINS_TO_GENERATE = 1000000

# Minimum allowed length for the strings
MIN_CADENA_LONGITUD = 1

# Maximum allowed length for the strings
MAX_CADENA_LONGITUD = 1000

# List of characters that are not allowed in the strings
CARACTERES_NO_PERMITIDOS = ["@", "#", "$", "%"]

# Time to wait between sending requests to the server, in seconds
DELAY_ENTRE_PETICIONES = 0.1