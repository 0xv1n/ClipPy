import socket


def start_server(host="localhost", port=1337):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    print(f"Clipboard contents: {data.decode('utf-8')}")


if __name__ == "__main__":
    start_server()
