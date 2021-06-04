from serverClass import *

if __name__ == "__main__":
    from re import search
    port = 3737

    IP = input("Give me your ip: ")
    ip = search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', IP)

    if not ip:
        IP = socket.gethostbyname(socket.gethostname())

    addr = (IP, port)
    Server(addr)
