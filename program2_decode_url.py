import tkinter as tk
from urllib.parse import urlsplit, urlunsplit, unquote


def decode_domain(netloc: str) -> str:
    if not netloc:
        return netloc

    user_info = ""
    host_port = netloc

    if "@" in netloc:
        user_info, host_port = netloc.rsplit("@", 1)
        user_info += "@"

    host = host_port
    port = ""

    if ":" in host_port and not host_port.startswith("["):
        host, port = host_port.rsplit(":", 1)
        port = ":" + port

    try:
        host = host.encode("ascii").decode("idna")
    except Exception:
        pass

    return user_info + host + port


def decode_url(url: str) -> str:
    parts = urlsplit(url)

    decoded_netloc = decode_domain(parts.netloc)
    decoded_path = unquote(parts.path)
    decoded_query = unquote(parts.query)
    decoded_fragment = unquote(parts.fragment)

    decoded = urlunsplit((
        parts.scheme,
        decoded_netloc,
        decoded_path,
        decoded_query,
        decoded_fragment
    ))

    return decoded


def copy_to_clipboard(text: str):
    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()


def main():
    encoded_url = input("Введіть закодоване посилання: ").strip()

    decoded = decode_url(encoded_url)

    print("\nДЕКОДОВАНЕ ПОСИЛАННЯ:")
    print(decoded)

    try:
        copy_to_clipboard(decoded)
        print("\nПосилання скопійовано в буфер обміну.")
    except Exception as error:
        print("\nНе вдалося скопіювати в буфер обміну.")
        print("Причина:", error)


if __name__ == "__main__":
    main()