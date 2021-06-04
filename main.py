import sys
from clientThreads import *
import simpleaudio

"""

<idle>
- server idle

server GUI?

server on startup?

better emojis?

study how to change system settings...

"""



# ""
class Ui(QtWidgets.QMainWindow, Ui_MainWindow):

    # ""
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.oldPos = self.pos()
        FreeRAM(self).start()

        # just defining a spacer here
        self.spacerItem = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(self.spacerItem)

        ########### Connecting MenuBar actions to functions on code #############
        self.scanOnStartBtn.triggered.connect(self.toggle_scan_on_start)
        self.toggleNotificationsBtn.triggered.connect(self.toggle_notifications)
        self.resetIpsBtn.triggered.connect(self.reset_suggestions)

        self.sizeLarge.triggered.connect(partial(self.change_font_size, 2))
        self.sizeNormal.triggered.connect(partial(self.change_font_size, 1))
        self.sizeSmall.triggered.connect(partial(self.change_font_size, 0))
        self.bgColorBtn.triggered.connect(self.change_bg_color)
        self.defaultBgBtn.triggered.connect(lambda: self.update_stylesheet("rgb(10, 30, 60)"))

        self.startServerBtn.triggered.connect(self.start_server)

        self.exitBtn.triggered.connect(self.exit_program)

        ############## Top widgets #################
        self.emojiBtn.clicked.connect(self.open_emoji_menu)
        self.ipInput.returnPressed.connect(self.start_network)
        self.ipToggleBtn.clicked.connect(self.toggle_ip)
        self.ipToggleBtn.hide()
        self.scanBtn.clicked.connect(partial(self.scan_for_servers, 2))
        self.msgBtn.clicked.connect(self.send_msg)
        self.msgInput.textChanged.connect(self.on_text_changed)
        self.usernameBtn.clicked.connect(self.change_username)
        self.usernameLabel.setDisabled(True)
        self.usernameLabel.hide()
        self.typingLabel.hide()

        ############# Bottom widgets ################
        self.msgBtn.hide()
        self.msgInput.keyPressEvent = self._combine_funcs(
            self.msgInput.keyPressEvent, self.combine_kpe)


        ####### defining variables to use later #######
        self.scanThread = None
        self.socket = None
        self.can_close = False
        self.addr = None
        self.platform = sys.platform

        ####### defaults ######
        self.username = None
        self.show_notifications = True
        self.scan_on_start = False
        self.show_ip = True
        self.font_size = 11
        self.padding = 4
        self.color = "rgb(10, 30, 60)"
        self.recent_servers = []

        ####### loading saved variables from pickle file ########
        try:
            with open('extra/data.pkl', "rb") as f:
                self.username, self.font_size, self.show_notifications,\
                self.show_ip, self.scan_on_start, self.padding, self.color,\
                self.recent_servers = load(f)

            self.usernameLabel.setText(emojize(self.username, use_aliases=True))
            self.usernameBtn.setText(emojize(self.username, use_aliases=True))
            self.update_stylesheet(self.color)

        except:
            pass


        ####### updating/togging btns based on loaded values #######
        if self.show_ip is False:
            self.ipToggleBtn.setText(">")

        if self.scan_on_start:
            self.scanOnStartBtn.setText("Do not scan for servers on start")
            QtCore.QTimer().singleShot(500, partial(self.scan_for_servers, 2))

        if self.show_notifications is False:
            self.toggleNotificationsBtn.setText("Enable notifications")

        if self.recent_servers:
            self.update_suggestions()

        ######### dealing with the typing info system #########
        self.typing = False
        self.send_typing = True
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.reset_typing)
        self.timer.start(2000)
        self.hide_typing_label = QtCore.QTimer()
        self.hide_typing_label.timeout.connect(self.typingLabel.hide)

        ######### defining the tray here #########
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(QtGui.QIcon("extra/talk.png"))
        self.tray.setVisible(True)
        self.tray.show()
        self.tray.activated.connect(self.show_window)
        menu_ = QtWidgets.QMenu()
        show_ = menu_.addAction("Show    ")
        quit_ = menu_.addAction("Exit    ")
        quit_.triggered.connect(self.exit_program)
        show_.triggered.connect(self.show_on_front)
        self.tray.setContextMenu(menu_)

    ########### menubar functions ###########
    def toggle_scan_on_start(self):
        self.scan_on_start = not self.scan_on_start
        text = "Do not scan for servers on start" if self.scan_on_start else "Scan for servers on start"
        self.scanOnStartBtn.setText(text)

    # ""
    def toggle_notifications(self):
        self.show_notifications = not self.show_notifications
        text = "Disable notifications" if self.show_notifications else "Enable notifications"
        self.toggleNotificationsBtn.setText(text)

    # ""
    def reset_suggestions(self):
        self.recent_servers = []
        self.update_suggestions()

    # ""
    def change_font_size(self, i):
        sizes = [9, 11, 13]
        paddings = [2, 4, 5]
        self.font_size = sizes[i]
        self.padding = paddings[i]

    # ""
    def change_bg_color(self):
        color = QtWidgets.QColorDialog.getColor()

        if color.isValid():
            self.update_stylesheet(color.name())

    # ""
    def update_stylesheet(self, color):
        self.color = color
        style = f"background-color: {self.color};\n" "border-radius: 10px;"
        self.scrollArea.setStyleSheet(style)
        style = """* {
        background-color: rgb(33, 52, 80);
        }

        QScrollBar::add-page, QScrollBar::sub-page {
        background-color: %s;
        }

        QScrollBar::handle {
        background-color: black; 
        border-radius: 4px; 
        border: 1px solid gray;}

        QScrollBar::add-line, QScrollBar::sub-line {
        border:none;
        background-color:none;}
        """ % self.color
        self.widget.setStyleSheet(style)

    # ""
    @staticmethod
    def start_server():
        system("start server")

    ######## tray functions ######## this is also used on the last item from menubar
    def exit_program(self):
        self.can_close = True
        self.close()

    # ""
    def show_window(self, reason):
        if reason == 1:
            pass

        else:
            self.show_on_front()

    ######### typing related functions ########
    def on_text_changed(self, text):
        if text.replace(" ", "") != "":
            if search(r":\w+:", text):
                emojized = emojize(text, use_aliases=True)
                if emojized != text:
                    self.msgInput.setText(emojized)

            self.msgBtn.show()
            self.is_typing()


        else:
            self.msgBtn.hide()

    # ""
    def is_typing(self):
        if self.msgBtn.isEnabled():
            if self.send_typing:
                if self.username is not None and self.socket is not None:
                    data = {"type": "typing",
                            "username": self.username}
                    client_thread = SendData(self, self.socket, data)
                    client_thread.start()

                    self.send_typing = False

    # ""
    def reset_typing(self):
        self.send_typing = True

    # ""
    def change_typing(self, username):
        self.typingLabel.show()
        username = emojize(username, use_aliases=True)
        self.typingLabel.setText(f"{username}  is typing...")
        self.hide_typing_label.start(3000)

    ######### on event functions from pyqt5 ##########
    def closeEvent(self, event):

        if self.can_close:
            self.save()
            self.tray.setVisible(False)
            self.tray.hide()
            self.tray.setParent(None)
            event.accept()
        else:
            self.hide()
            event.ignore()

    # ""
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        try:
            self.notification.close()
        except:
            pass

    # ""
    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # ""
    def dragEnterEvent(self, e):
        em = e.mimeData().text()
        if search("file:///", em):
            if search("\n", em):
                pass

            else:
                e.accept()

    # ""
    def dropEvent(self, e):
        e = e.mimeData().text()
        if self.socket is not None:
            path = e.replace("file:///", "", 1)
            self.send_file(data=None, path=path)

    # ""
    def changeEvent(self, e):
        try:
            self.notification.close()
        except:
            pass

    ######### file handling functions here #########
    def save(self):
        with open('extra/data.pkl', 'wb') as f:
            data = (self.username, self.font_size,
                    self.show_notifications, self.show_ip,
                    self.scan_on_start, self.padding, self.color,
                    self.recent_servers)
            dump(data, f)

    # ""
    @staticmethod
    def save_file(data):
        filename = data["file_name"]

        file_dialog = str(QtWidgets.QFileDialog.getExistingDirectory(
            caption="Save file...", directory=""))

        if file_dialog:
            target = f"{file_dialog}/{filename}"
            path = f"files/{filename}"
            copyfile(path, target)

    # ""
    def send_file(self, data=None, path=""):
        try:
            self.notification.close()
        except:
            pass

        if data is not None:
            if self.username is None:
                self.change_username()

            client_thread = SendData(self, self.socket, data)
            client_thread.tuple_signal.connect(self.confirm_msg)
            client_thread.start()

            self.timer.stop()
            self.msgBtn.setDisabled(True)

        elif data is None:
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                None, "Send file...", path, "All Files (*)")

            if file_path:
                if self.username is None:
                    self.change_username()

                file_size = getsize(file_path)
                if file_size > 25_000_000:
                    self.notify(
                        "Big file", "You cant send messages until the file is sent.")

                file_name = basename(file_path)

                data = {"type": "file",
                        "username": self.username,
                        "file_size": str(file_size),
                        "file_name": file_name,
                        "data": file_path}

                client_thread = SendData(self, self.socket, data)
                client_thread.tuple_signal.connect(self.confirm_msg)
                client_thread.start()


                self.timer.stop()
                self.msgBtn.setDisabled(True)

    # ""
    def combine_kpe(self, event):
        if event.matches(QtGui.QKeySequence.Paste):
            if QtWidgets.QApplication.clipboard().text(mode=QtGui.QClipboard.Clipboard) == "" and self.socket != None:
                try:
                    from PIL import ImageGrab
                    from io import BytesIO
                    img = ImageGrab.grabclipboard()
                    img_bytes = BytesIO()
                    img.save(img_bytes, format='png')
                    file_size = len(img_bytes.getvalue())
                    file_name = "Screenshot.png"
                    file_bytes = img_bytes.getvalue()

                    data = {"type": "file",
                            "username": self.username,
                            "file_size": str(file_size),
                            "file_name": file_name,
                            "data": file_bytes}

                    if not self.socket is None:
                        self.send_file(data=data)

                except Exception as e:
                    #print(e, 1)
                    pass

    ######### message functions #########
    @staticmethod
    def object_of_widget(data, widget, font_size):
        _type = data["type"]

        size_p = data["sizeP"]
        color = data["color"]
        bg_color = data["bgColor"]
        padding = data["padding"]
        text = data["text"]

        obj = QtWidgets.QLabel(
            widget) if _type == "label" else QtWidgets.QPushButton(widget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed) if size_p == "fixed" else QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        obj.setSizePolicy(size_policy)
        obj.setStyleSheet(f"background-color: rgb{str(bg_color)};\n"
                          f"padding: {str(padding)}px;\n"
                          f"color: {color};")


        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(font_size)
        obj.setFont(font)

        if _type == "label":
            obj.setWordWrap(True)
            obj.setAlignment(data["alignment"])
            obj.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        else:
            obj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        if len(text) > 45 and not search(" ", text) and not search("/", text):
            w = wrap(text, 45, break_long_words=True)
            text = "\n".join(w)

        obj.setText(text)
        obj.setObjectName("obj")

        return obj

    # ""
    def create_message(self, objs, color, space1=None, space2=None):
        widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)

        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        widget.setSizePolicy(size_policy)
        widget.setStyleSheet(f"background-color: transparent;\n"
                               "border-radius: 6px;\n"
                               "padding: 5px;\n")
        widget.setObjectName("widget")
        layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setObjectName("horizontalLayout_9")

        if space1:
            obj = QtWidgets.QSpacerItem(
                0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            layout.addItem(obj)

        widget2 = QtWidgets.QWidget(widget)

        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        widget2.setSizePolicy(size_policy)
        widget2.setStyleSheet(f"background-color: rgb{str(color)};\n"
                             "border-radius: 6px;\n"
                             f"padding: {self.padding}px;\n")
        widget2.setObjectName("widget_6")
        layout2 = QtWidgets.QHBoxLayout(widget2)
        layout2.setContentsMargins(3, 3, 3, 3)
        layout2.setSpacing(3)
        layout2.setObjectName("horizontalLayout_5")
        layout.addWidget(widget2)

        if space2:
            obj = QtWidgets.QSpacerItem(
                0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            layout.addItem(obj)

        to_return = None
        for obj in objs:
            obj["padding"] = self.padding
            widget_obj = self.object_of_widget(obj, widget2, self.font_size)
            if obj["type"] == "btn":
                to_return = widget_obj

            if to_return is None:
                to_return = widget_obj

            layout2.addWidget(widget_obj)

        self.verticalLayout_3.addWidget(widget)
        return widget_obj if to_return is None else to_return

    # ""
    def process_received_data(self, data):
        _type, data = data

        if "username" in data:
            username_obj = {"type": "label", "sizeP": "fixed",
                           "color": "white", "text": emojize(data["username"], use_aliases=True),
                           "alignment": QtCore.Qt.AlignHCenter,
                           "bgColor": (0, 0, 0), "padding": 5}

        if _type == "file":
            size = convertBytesToReadable(
                int(data["file_size"]), system=alternative)
            text = "FILENAME %s     SIZE %s" % (
                data["file_name"], size)

            objs = [
                username_obj,
                {"type": "label",
                    "sizeP": "fixed",
                    "color": "white",
                    "alignment": QtCore.Qt.AlignHCenter,
                    "text": "FILENAME",
                    "bgColor": (0, 0, 0),
                    "padding": 6},

                {"type": "label",
                    "sizeP": "ex",
                    "color": "black",
                    "alignment": QtCore.Qt.AlignLeft,
                    "text": data["file_name"],
                    "bgColor": (56, 228, 255),
                    "padding": 4},

                {"type": "label",
                    "sizeP": "fixed",
                    "color": "white",
                    "alignment": QtCore.Qt.AlignHCenter,
                    "text": "SIZE",
                    "bgColor": (0, 0, 0),
                    "padding": 6},

                {"type": "label",
                    "sizeP": "ex",
                    "color": "black",
                    "alignment": QtCore.Qt.AlignLeft,
                    "text": size,
                    "bgColor": (56, 228, 255),
                    "padding": 4},

                {"type": "btn",
                    "sizeP": "ex",
                    "color": "white",
                    "alignment": QtCore.Qt.AlignHCenter,
                    "text": "Save file",
                    "bgColor": (0, 0, 0),
                    "padding": 6},

            ]

            btn = self.create_message(objs, (56, 228, 255), None, True)
            btn.clicked.connect(partial(self.save_file, data))

            self.last_wid = btn

            playsound('extra/m.wav', block=False)

            self.notify(emojize(data["username"], use_aliases=True), text)

            self.scroll_down()
            self.typingLabel.hide()

        elif _type == "conn":
            conn_number = data["data"]
            self.connNumLabel.setText(f"People online {conn_number}")

            self.notify("People online", conn_number)

        elif _type == "typing":
            username = data["username"]
            self.change_typing(username)

        elif _type == "message":
            text = emojize(data["data"], use_aliases=True)

            objs = [
                username_obj,
                {"type": "label", "sizeP": "ex",
                 "color": "black", "alignment": QtCore.Qt.AlignLeft,
                 "text": text, "bgColor": (56, 228, 255), "padding": 5}]

            self.last_wid = self.create_message(objs, (56, 228, 255), None, True)

            if self.platform == "win32":
                playsound('extra/m.wav', block=False)
            else:
                wave_obj = simpleaudio.WaveObject.from_wave_file('extra/m.wav')
                play_obj = wave_obj.play()
                play_obj.wait_done()

            self.notify(emojize(data["username"], use_aliases=True), text)
            self.typingLabel.hide()

            if self.is_on_bottom():
                self.scroll_down()

        elif _type == "you":
            if data["type"] == "message":
                text = emojize(data["data"], use_aliases=True)

                objs = [
                    {"type": "label",
                     "sizeP": "ex",
                     "color": "black",
                     "alignment": QtCore.Qt.AlignRight,
                     "text": text,
                     "bgColor": (91, 77, 255),
                     "padding": 4}
                ]

                wid = self.create_message(objs, (91, 77, 255), True)
                self.last_wid = wid

            else:
                size = convertBytesToReadable(
                    int(data["file_size"]), system=alternative)

                objs = [
                    {"type": "label",
                     "sizeP": "fixed",
                     "color": "white",
                     "alignment": QtCore.Qt.AlignHCenter,
                     "text": "FILENAME",
                     "bgColor": (0, 0, 0),
                     "padding": 6},

                    {"type": "label",
                     "sizeP": "ex",
                     "color": "black",
                     "alignment": QtCore.Qt.AlignLeft,
                     "text": data["file_name"],
                     "bgColor": (91, 77, 255),
                     "padding": 4},

                    {"type": "label",
                     "sizeP": "fixed",
                     "color": "white",
                     "alignment": QtCore.Qt.AlignHCenter,
                     "text": "SIZE",
                     "bgColor": (0, 0, 0),
                     "padding": 6},

                    {"type": "label",
                     "sizeP": "ex",
                     "color": "black",
                     "alignment": QtCore.Qt.AlignLeft,
                     "text": size,
                     "bgColor": (91, 77, 255),
                     "padding": 4}
                ]

                wid = self.create_message(objs, (91, 77, 255), True)
                self.last_wid = wid


            self.scroll_down()

        elif _type == "s_typing":
            self.timer.start(2000)

        elif _type == "reset":
            text = "The server disconnected"

            objs = [
                {"type": "label", "sizeP": "ex", "color": "black",
                 "alignment": QtCore.Qt.AlignHCenter, "text": text,
                 "bgColor": (106, 0, 148), "padding": 3}]

            wid = self.create_message(objs, (106, 0, 148), True, True)

            playsound('extra/d.mp3', block=False)
            self.notify("Disconnected", text)

            self.reset_window()

            self.last_wid = wid
            self.scroll_down()

    # ""
    def is_on_bottom(self):
        value = self.scrollArea.verticalScrollBar().value()
        maximum = self.scrollArea.verticalScrollBar().maximum()
        return True if maximum == value else False

    # ""
    def scroll_down(self):
        vbar = self.scrollArea.verticalScrollBar()
        func = lambda: vbar.setValue(vbar.maximum())         #partial(self.scrollArea.ensureWidgetVisible, l)
        QtCore.QTimer().singleShot(80, func)

    # ""
    def confirm_msg(self, info):
        if len(info) == 3:
            pass

        else:
            self.process_received_data(("you", info[1]))
            self.msgInput.setText("")

        self.msgBtn.setEnabled(True)

    # ""
    def send_msg(self):
        try:
            self.notification.close()
        except:
            pass
        if self.username is None:
            self.change_username()

        if self.msgInput.text().replace(" ", "") != "":
            data = {"type": "message",
                    "username": self.username,
                    "data": self.msgInput.text()}

            client_thread = SendData(self, self.socket, data)
            client_thread.tuple_signal.connect(self.confirm_msg)
            client_thread.start()

        self.msgBtn.setDisabled(True)

    ######## conn functions #########
    def scan_for_servers(self, l=1):
        if l == 1:
            client_thread = ClientInit(self, loop_times=1, recent_servers=self.recent_servers)
            client_thread.tuple_signal.connect(self.client_socket)
            client_thread.start()
        else:
            if self.scanBtn.text() == "Start Scanning":
                client_thread = ClientInit(self)
                client_thread.tuple_signal.connect(self.client_socket)
                client_thread.start()
                self.scanThread = client_thread
                self.scanBtn.setText("Stop Scanning")

            else:
                self.scanThread.terminate()
                self.scanBtn.setText("Start Scanning")

    # ""
    def client_socket(self, sock):
        ip, i = sock
        if ip != 1:
            self.addr = (ip, 3737)
            if ip not in self.recent_servers:
                self.recent_servers.append(ip)

            #self.ipInput.setText(ip)
            self.socket = i
            self.ipInput.hide()
            self.ipToggleBtn.show()
            self.msgBtn.setEnabled(True)
            self.scanBtn.setDisabled(True)
            self.usernameLabel.setEnabled(True)
            self.usernameLabel.show()
            self.usernameBtn.setDisabled(True)
            self.usernameBtn.hide()
            self.scanBtn.hide()
            self.scanBtn.setText("Start Scanning")
            if self.show_ip:
                self.connLabel.setText("CONNECTED TO %s" % self.addr[0])

            else:
                self.connLabel.setText("CONNECTED")

            self.connLabel.setStyleSheet("color: lime;")
            self.client_thread = ReceiveMessage(self, self.socket)
            self.client_thread.tuple_signal.connect(self.process_received_data)
            self.client_thread.start()

            playsound('extra/c.mp3', block=False)
            self.notify("Connected", "Connected to server")

        else:
            playsound('extra/d.mp3', block=False)
            self.notify("Error", "Could not connect to server")

            self.reset_window()

    # ""
    def start_network(self):
        ip = self.ipInput.text()
        port = 3737

        if ip.replace(" ", "") != "":
            if ip in ["local", "l"]:
                ip = socket.gethostbyname(socket.gethostname())

            self.addr = (ip, port)

            client_thread = ClientInit(self, self.addr)
            client_thread.tuple_signal.connect(self.client_socket)
            client_thread.start()

            self.ipInput.setDisabled(True)

    # ""
    def reset_window(self):
        self.ipToggleBtn.hide()
        self.ipInput.setEnabled(True)
        self.msgBtn.setDisabled(True)
        self.usernameBtn.setEnabled(True)
        self.usernameBtn.show()
        self.usernameLabel.setDisabled(True)
        self.usernameLabel.hide()
        self.ipInput.show()
        self.connLabel.setText("NOT CONNECTED")
        self.connLabel.setStyleSheet("color: white;")
        self.scanBtn.setEnabled(True)
        self.scanBtn.show()
        self.connNumLabel.setText("")
        self.socket = None

        if self.recent_servers:
            self.update_suggestions()

    ######### Last functions here, these functions interact with the frontend in some way #########
    def update_suggestions(self):
        completer = QtWidgets.QCompleter(self.recent_servers)
        completer.popup().setStyleSheet("background-color: rgb(33, 52, 80); color: white;")
        self.ipInput.setCompleter(completer)

    # ""
    def toggle_ip(self):
        self.show_ip = not self.show_ip
        if self.show_ip:
            self.connLabel.setText("CONNECTED TO %s" % self.addr[0])
            self.ipToggleBtn.setText("<")

        else:
            self.connLabel.setText("CONNECTED")
            self.ipToggleBtn.setText(">")

    # ""
    def open_emoji_menu(self):
        from emojiMenu import Menu
        menu = Menu(self)

    # ""
    def change_username(self):
        while True:
            text, result = QtWidgets.QInputDialog.getText(
                None, "Username", "Username")
            if result:
                if text.replace(" ", "") != "":
                    self.username = text
                    self.usernameLabel.setText(emojize(self.username, use_aliases=True))
                    self.usernameBtn.setText(emojize(self.username, use_aliases=True))
                    self.save()

                    break

            else:
                return 0

    # ""
    def show_on_front(self):
        self.activateWindow()
        self.showNormal()
        try:
            self.scroll_down()
        except:
            pass

    # ""
    def notify(self, title, text):
        if not self.isActiveWindow() and self.show_notifications:
            self.notification = Notification()
            self.notification.setNotify(title, text)
            self.notification.doubleClick.connect(self.show_on_front)

    ######### These last ones do not interact with the frontend, only backend here #########
    @staticmethod
    def _combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func


# ""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

