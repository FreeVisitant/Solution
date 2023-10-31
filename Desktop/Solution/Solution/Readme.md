# Solution

# String Weighting System

This project implements a client-server solution in Python to evaluate and calculate the weight of text strings based on specific rules.


## Requirements

- Python 3.8 or higher
- Operating System: Windows, Linux, or MacOS


## Usage

### Client

To start and generate the chains:

```bash
python client.py
```

To check if every chains is generated correctly:

```bash
python validate_chains.py
```

### Server

To start the server, run:

```bash
python server.py
```

The server will start and listen for incoming connections.

### Client

To send the strings to the server and receive the responses, run:

```bash
python client.py
```

The server's responses will be stored in the file specified in the client's configuration.

## Configuration

Configure the system by editing the `config_client.py` and `config_server.py` files. Set the server's IP address and port, the paths of the strings and responses files, and other relevant parameters.

## Architecture

The system consists of two main components:

- **Client**: Generates text strings, sends them to the server for processing, and saves the responses in a file.
- **Server**: Receives text strings, processes them to calculate their weight, and sends the responses back to the client.

## Features

- Capability to process a million text strings.
- Validation and processing of strings according to specific rules.
- Event and result logging to log files.
