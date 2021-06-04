import socket
from encrypt import encryption
from threading import Thread
from json import dumps, loads
import gc

# ""
class Server:

    def __init__(self, addr):
        self.connections = {}
        self.conn_number = 1
        self.spacing = " " * 40

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(addr)
        server.listen(5)
        print(f"Server started, acceping connections at {addr[0]}:{addr[1]}")

        while True:
            conn, addr = server.accept()

            Thread(target=self.conn_handle, args=(
                conn, addr, self.conn_number), daemon=True).start()
            self.connections[self.conn_number] = conn

            self.conn_number += 1
            data = {
                "type": "conn",
                "data": str(len(self.connections))
            }
            
            Thread(target=self.send_message, args=(data, None)).start()

    # ""
    @staticmethod
    def receive(conn, size):
        try:
            _bytes = bytearray()
            while len(_bytes) < size:
                packet = conn.recv(size - len(_bytes))
                if not packet:
                    break

                _bytes.extend(packet)

            return _bytes

        except:
            return b""

    # "" Conn Handle
    def conn_handle(self, conn, addr, conn_number):
        print("%s connected%s" % (addr[0], self.spacing))

        header = 18
        formatt = "utf-8"

        connected = True

        while connected:
            msg_lenth = ""
            data = ""
            msg_lenth = self.receive(conn, header).decode(formatt)

            if msg_lenth:
                msg_lenth = int(msg_lenth)

                data = self.receive(conn, msg_lenth).decode(formatt)

                if not data:
                    print("%s disconnected [No msg]%s" % (addr[0], self.spacing))
                    break

                data = loads(data)

                for key, item in data.items():
                    data[key] = encryption().decrypt(item)

                _type = data["type"]

                if _type == "message":
                    msg = data["data"]
                    name = data["username"]
                    print(f"RECEIVED {_type} [{msg}] from {name}/{addr[0]}")
                    Thread(target=self.send_message, args=(
                        data, conn), daemon=True).start()

                elif _type == "file":
                    filename = data["file_name"]
                    name = data["username"]
                    size = int(data["file_size"])

                    print(
                        f"RECEIVED {_type} [{filename} size {size}] from {name}/{addr[0]}", flush=False)

                    self.send_message(data, conn)

                elif _type == "typing":
                    name = data["username"]
                    print(f"RECEIVED {_type} from {name}/{addr[0]}", end="\r")
                    Thread(target=self.send_message, args=(
                        data, conn), daemon=True).start()

            else:
                print("%s disconnected [No msg_length]%s" % (addr[0], self.spacing))
                connected = False

            del gc.garbage[:]
            gc.collect()

        try:
            self.connections.pop(conn_number)
        except:
            pass

        data = {
            "type": "conn",
            "data": str(len(self.connections))
        }
        Thread(target=self.send_message, args=(data, None)).start()
        conn.close()

    # ""
    def send_message(self, data, current_conn=None):

        type_ = data["type"]
        file = True if type_ == "file" else None
        if file:
            file_size = int(data["file_size"])

        self.data = {}
        failed = False
        self.e = None
        for key, item in data.items():
            self.data[key] = encryption().encrypt(item)

        header = 18
        formatt = "utf-8"

        for conn in self.connections.values():
            if conn != current_conn:
                try:
                    data = str.encode(dumps(self.data))
                    msg_lenth = len(data)
                    send_lenth = str(msg_lenth).encode(formatt)
                    send_lenth += b" " * (header - len(send_lenth))
                    conn.send(send_lenth)
                    conn.send(data)

                except Exception as e:
                    self.e = e
                    failed = True

        if file:
            try:
                received = 0
                while received < file_size:
                    packet = current_conn.recv(file_size - received)
                    if not packet:
                        break

                    received += len(packet)
                    for conn in self.connections.values():
                        if conn != current_conn:
                            conn.sendall(packet)
                   
                    del packet
                    del gc.garbage[:]
                    gc.collect()

                    data = str.encode(dumps({"type": encryption().encrypt("s_typing")}))
                    msg_lenth = len(data)
                    send_lenth = str(msg_lenth).encode(formatt)
                    send_lenth += b" " * (header - len(send_lenth))
                    current_conn.send(send_lenth)
                    current_conn.send(data)


            except Exception as e:
                self.e = e
                failed = True

        if failed is False:
            if type_ != "typing":
                print("MSG SENT" + self.spacing)

        else:
            print(f"{self.e} MSG NOT SENT" + self.spacing)


        del gc.garbage[:]
        gc.collect()

