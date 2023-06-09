# Honeypot

This project consists of two files: `honeypot` and `server.py`. The `honeypot` file starts a server using `server.py` on a random available port and exposes it to the internet using `ngrok`.

## Installation

Before running the `honeypot` script, you'll need to install the `ngrok` tool. You can download it from the [ngrok website](https://ngrok.com/download).

## Usage

1. Open a terminal window and navigate to the directory where the `honeypot` file is located.
2. Make the `honeypot` script executable by typing:

```sh
chmod +x honeypot
```

3. Run `./honeypot`.

The server will be available on the URL provided by ngrok.

## Details

The `honeypot` script defines two functions: `pick_port()` and `start_server()`. `pick_port()` chooses a random available port using `lsof`, and `start_server()` starts the server by running `server.py` on the selected port.

The `server.py` file defines a `start_server()` function which binds to the localhost on the specified port and listens for incoming requests. When a request is received, the server sends a 200 OK response and closes the connection.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
