from find_servers import *
from importer import *
from encrypt import encryption
from json import loads, dumps

# ""
class ClientInit(QtCore.QThread):
    tuple_signal = QtCore.pyqtSignal(tuple)

    def __init__(self, parent, addr=None, loop_times=100000, recent_servers=[]):
        QtCore.QThread.__init__(self, parent=parent)
        self.addr = addr
        self.loop_times = loop_times
        self.recent_servers = recent_servers

    def run(self):
        if self.addr is None:
            try:
                client = 1
                ipfound = 1
                for i in range(self.loop_times):
                    client, ipfound = SearchServer().look_for_server(3737, self.recent_servers)
                    if client != 1:
                        break

                self.tuple_signal.emit((ipfound, client))
            except Exception as e:
                #print(e, 1)
                pass

        else:
            try:
                socket.setdefaulttimeout(None)
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(self.addr)
                self.tuple_signal.emit((self.addr[0], client))

            except Exception as e:
                #print(e, 2)
                self.tuple_signal.emit((1, "COULD NOT CONNECT"))

        gc.collect()

# ""
class SendData(QtCore.QThread):
    tuple_signal = QtCore.pyqtSignal(tuple)

    def __init__(self, parent, _socket, data):
        QtCore.QThread.__init__(self, parent=parent)
        self.socket = _socket
        self.unencrypted_data = data
        self.data = {}
        self.file = None
        self.file_size = None

        for key, item in data.items():
            if "file_name" in data and key == "data":
                self.file = data["data"]
                self.file_size = int(data["file_size"])

            else:
                self.data[key] = encryption().encrypt(item)


    def run(self):
        header = 18
        formatt = "utf-8"

        try:
            data = str.encode(dumps(self.data))
            msg_lenth = len(data)
            send_lenth = str(msg_lenth).encode(formatt)
            send_lenth += b" " * (header - len(send_lenth))
            self.socket.send(send_lenth)
            self.socket.send(data)
            if not self.file is None:
                sent = 0
                if isinstance(self.file, bytes):
                    self.socket.sendall(self.file)

                    del gc.garbage[:]
                    gc.collect()

                else:
                    with open(self.file, "rb") as f:
                        while sent < self.file_size:
                            chunk = self.file_size - len(str(sent)) if sent < 50000 else 50000
                            send = self.socket.send(f.read(chunk))
                            sent += send

                            del send
                            del gc.garbage[:]
                            gc.collect()


                        #print(sent, self.file_size)

            self.tuple_signal.emit(
                ("DATA SENT", self.unencrypted_data))

        except Exception as e:
            #print(e)
            self.tuple_signal.emit(("DATA NOT SENT", 1, 1))

        gc.collect()

# ""
class ReceiveMessage(QtCore.QThread):
    tuple_signal = QtCore.pyqtSignal(tuple)

    def __init__(self, parent, _socket):
        QtCore.QThread.__init__(self, parent=parent)
        self.socket = _socket

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

        except Exception as e:
            #print(e)
            return b""

    def run(self):
        header = 18
        formatt = "utf-8"

        connected = True

        while connected:
            msg_lenth = ""
            data = ""

            msg_lenth = self.receive(self.socket, header).decode(formatt)

            if msg_lenth:
                msg_lenth = int(msg_lenth)

                data = self.receive(self.socket, msg_lenth).decode(formatt)

                if not data:
                    break

                data = loads(data)

                for key, item in data.items():
                    data[key] = encryption().decrypt(item)

                _type = data["type"]

                if _type == "conn":
                    self.tuple_signal.emit(("conn", data))

                elif _type == "message":
                    self.tuple_signal.emit(("message", data))

                elif _type == "file":
                    size = int(data["file_size"])
                    name = data["file_name"]
                    try:
                        received = 0
                        f = open(f"files/{name}", "wb")
                        f.close()
                        while received < size:
                            packet = self.socket.recv(size - received)
                            if not packet:
                                break

                            received += len(packet)

                            with open(f"files/{name}", "ab") as f:
                                f.write(packet)


                            del packet
                            del gc.garbage[:]
                            gc.collect()


                        self.tuple_signal.emit(("file", data))

                    except Exception as e:
                        #print(e)
                        pass

                elif _type == "typing":
                    self.tuple_signal.emit(("typing", data))

                elif _type == "s_typing":
                    self.tuple_signal.emit(("s_typing", data))

                gc.collect()

            else:
                connected = False

        self.tuple_signal.emit(("reset", "The server disconnected."))
        self.socket.close()

# ""
class FreeRAM(QtCore.QThread):
    def __init__(self, parent):
        QtCore.QThread.__init__(self, parent=parent)


    def run(self):
        while True:
            del gc.garbage[:]
            gc.collect()
            sleep(20)