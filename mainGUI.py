# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 492)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(632, 492))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setWindowTitle("PRIVATEAPP")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("extra/talk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(300, 0))
        self.widget.setStyleSheet("* {\n"
"background-color: rgb(33, 52, 80);\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"background-color: rgb(10, 30, 60);\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"background-color: black; \n"
"border-radius: 4px; \n"
"border: 1px solid gray;}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"border:none;\n"
"background-color:none;}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(4, 0, 4, 4)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.emojiBtn = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emojiBtn.sizePolicy().hasHeightForWidth())
        self.emojiBtn.setSizePolicy(sizePolicy)
        self.emojiBtn.setMinimumSize(QtCore.QSize(5, 0))
        self.emojiBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.emojiBtn.setToolTip("Open emojis menu")
        self.emojiBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("extra/emoji.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emojiBtn.setIcon(icon1)
        self.emojiBtn.setIconSize(QtCore.QSize(20, 20))
        self.emojiBtn.setFlat(True)
        self.emojiBtn.setObjectName("emojiBtn")
        self.horizontalLayout_2.addWidget(self.emojiBtn)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.connLabel = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connLabel.sizePolicy().hasHeightForWidth())
        self.connLabel.setSizePolicy(sizePolicy)
        self.connLabel.setToolTip("Connection Status")
        self.connLabel.setStyleSheet("* {\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolTip {\n"
"color:black;\n"
"}")
        self.connLabel.setText("NOT CONNECTED")
        self.connLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.connLabel.setWordWrap(True)
        self.connLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.connLabel.setObjectName("connLabel")
        self.horizontalLayout_5.addWidget(self.connLabel)
        self.ipToggleBtn = QtWidgets.QToolButton(self.widget_6)
        self.ipToggleBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ipToggleBtn.setToolTip("Hide/Show")
        self.ipToggleBtn.setStyleSheet("* {\n"
"color: white;\n"
"}\n"
"\n"
"QToolTip {\n"
"color: black;\n"
"}\n"
"")
        self.ipToggleBtn.setText("<")
        self.ipToggleBtn.setObjectName("ipToggleBtn")
        self.horizontalLayout_5.addWidget(self.ipToggleBtn)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.ipInput = QtWidgets.QLineEdit(self.widget_2)
        self.ipInput.setEnabled(True)
        self.ipInput.setToolTip("Connect to chosen ip")
        self.ipInput.setStyleSheet("* {\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolTip {\n"
"color: black;\n"
"}\n"
"")
        self.ipInput.setText("")
        self.ipInput.setDragEnabled(True)
        self.ipInput.setPlaceholderText("Connect to...")
        self.ipInput.setObjectName("ipInput")
        self.verticalLayout_2.addWidget(self.ipInput)
        self.connNumLabel = QtWidgets.QLabel(self.widget_2)
        self.connNumLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.connNumLabel.setText("")
        self.connNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.connNumLabel.setObjectName("connNumLabel")
        self.verticalLayout_2.addWidget(self.connNumLabel)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.scanBtn = QtWidgets.QPushButton(self.widget_3)
        self.scanBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scanBtn.setToolTip("<html><head/><body><p>Scan for servers you connected before and servers on your local network</p></body></html>")
        self.scanBtn.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.scanBtn.setText("Start Scanning")
        self.scanBtn.setObjectName("scanBtn")
        self.horizontalLayout_2.addWidget(self.scanBtn)
        self.typingLabel = QtWidgets.QLabel(self.widget_3)
        self.typingLabel.setStyleSheet("color: rgb(0, 255, 0);")
        self.typingLabel.setText("")
        self.typingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.typingLabel.setObjectName("typingLabel")
        self.horizontalLayout_2.addWidget(self.typingLabel)
        self.usernameBtn = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameBtn.sizePolicy().hasHeightForWidth())
        self.usernameBtn.setSizePolicy(sizePolicy)
        self.usernameBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.usernameBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.usernameBtn.setText("")
        self.usernameBtn.setFlat(True)
        self.usernameBtn.setObjectName("usernameBtn")
        self.horizontalLayout_2.addWidget(self.usernameBtn)
        self.usernameLabel = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy)
        self.usernameLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.usernameLabel.setText("")
        self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout_2.addWidget(self.usernameLabel)
        self.verticalLayout.addWidget(self.widget_3)
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 350))
        self.scrollArea.setStyleSheet("background-color: rgb(10, 30, 60);\n"
"border-radius: 10px;")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 624, 350))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 36))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.msgInput = QtWidgets.QLineEdit(self.widget_5)
        self.msgInput.setMinimumSize(QtCore.QSize(0, 27))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        self.msgInput.setFont(font)
        self.msgInput.setToolTip("Type and send messages")
        self.msgInput.setStyleSheet("*{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"padding-left: 6px;\n"
"}\n"
"\n"
"QToolTip {\n"
"background-color:white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"}")
        self.msgInput.setText("")
        self.msgInput.setDragEnabled(True)
        self.msgInput.setPlaceholderText("Type a message")
        self.msgInput.setObjectName("msgInput")
        self.horizontalLayout_4.addWidget(self.msgInput)
        self.msgBtn = QtWidgets.QPushButton(self.widget_5)
        self.msgBtn.setEnabled(False)
        self.msgBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.msgBtn.setToolTip("Send message")
        self.msgBtn.setStyleSheet("padding: 0px;")
        self.msgBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("extra/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msgBtn.setIcon(icon2)
        self.msgBtn.setIconSize(QtCore.QSize(30, 30))
        self.msgBtn.setShortcut("Return")
        self.msgBtn.setFlat(True)
        self.msgBtn.setObjectName("msgBtn")
        self.horizontalLayout_4.addWidget(self.msgBtn)
        self.verticalLayout.addWidget(self.widget_5)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 632, 21))
        self.menuBar.setStyleSheet("* {\n"
"background-color: rgb(33, 52, 80);\n"
"color:white;\n"
"}\n"
"QToolTip {\n"
"color:black;\n"
"}\n"
"\n"
"QMenuBar::item::selected {\n"
"background-color: rgb(73, 92, 120);\n"
"}\n"
"\n"
"\n"
"QMenu::item::selected {\n"
"background-color: rgb(73, 92, 120);\n"
"}\n"
"")
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setToolTip("Setting of application")
        self.menuSettings.setToolTipsVisible(True)
        self.menuSettings.setObjectName("menuSettings")
        self.menuFontSize = QtWidgets.QMenu(self.menuSettings)
        self.menuFontSize.setTitle("Message size")
        self.menuFontSize.setObjectName("menuFontSize")
        MainWindow.setMenuBar(self.menuBar)
        self.scanOnStartBtn = QtWidgets.QAction(MainWindow)
        self.scanOnStartBtn.setText("Scan for servers on start")
        self.scanOnStartBtn.setIconText("Scan for networks on start")
        self.scanOnStartBtn.setToolTip("<html><head/><body><p>Enable/Disable scanning for servers you connected before/on your local network on start of application</p></body></html>")
        self.scanOnStartBtn.setObjectName("scanOnStartBtn")
        self.toggleNotificationsBtn = QtWidgets.QAction(MainWindow)
        self.toggleNotificationsBtn.setText("Disable notifications")
        self.toggleNotificationsBtn.setIconText("Disable notifications")
        self.toggleNotificationsBtn.setToolTip("<html><head/><body><p>Disable/Enable notifications</p></body></html>")
        self.toggleNotificationsBtn.setObjectName("toggleNotificationsBtn")
        self.sizeLarge = QtWidgets.QAction(MainWindow)
        self.sizeLarge.setText("Large")
        self.sizeLarge.setIconText("Large")
        self.sizeLarge.setToolTip("Large")
        self.sizeLarge.setObjectName("sizeLarge")
        self.sizeNormal = QtWidgets.QAction(MainWindow)
        self.sizeNormal.setText("Normal")
        self.sizeNormal.setIconText("Normal")
        self.sizeNormal.setToolTip("Normal")
        self.sizeNormal.setObjectName("sizeNormal")
        self.sizeSmall = QtWidgets.QAction(MainWindow)
        self.sizeSmall.setText("Small")
        self.sizeSmall.setIconText("Small")
        self.sizeSmall.setToolTip("Small")
        self.sizeSmall.setObjectName("sizeSmall")
        self.bgColorBtn = QtWidgets.QAction(MainWindow)
        self.bgColorBtn.setText("Background color")
        self.bgColorBtn.setIconText("Background color")
        self.bgColorBtn.setToolTip("<html><head/><body><p>Change the background color of the chat</p></body></html>")
        self.bgColorBtn.setObjectName("bgColorBtn")
        self.defaultBgBtn = QtWidgets.QAction(MainWindow)
        self.defaultBgBtn.setText("Default background")
        self.defaultBgBtn.setIconText("Default background")
        self.defaultBgBtn.setToolTip("<html><head/><body><p>Change chat´s background to default</p></body></html>")
        self.defaultBgBtn.setObjectName("defaultBgBtn")
        self.startServerBtn = QtWidgets.QAction(MainWindow)
        self.startServerBtn.setText("Create a server")
        self.startServerBtn.setToolTip("<html><head/><body><p>Create a new server so people connect to your server</p></body></html>")
        self.startServerBtn.setObjectName("startServerBtn")
        self.exitBtn = QtWidgets.QAction(MainWindow)
        self.exitBtn.setText("Exit")
        self.exitBtn.setToolTip("<html><head/><body><p>Closes program</p></body></html>")
        self.exitBtn.setObjectName("exitBtn")
        self.resetIpsBtn = QtWidgets.QAction(MainWindow)
        self.resetIpsBtn.setText("Reset ip suggestions")
        self.resetIpsBtn.setIconText("Reset ip suggestions")
        self.resetIpsBtn.setToolTip("<html><head/><body><p>Reset all your the list of ips you have conneted before, so they do not appear on suggestions</p></body></html>")
        self.resetIpsBtn.setObjectName("resetIpsBtn")
        self.menuFontSize.addAction(self.sizeLarge)
        self.menuFontSize.addAction(self.sizeNormal)
        self.menuFontSize.addAction(self.sizeSmall)
        self.menuSettings.addAction(self.scanOnStartBtn)
        self.menuSettings.addAction(self.toggleNotificationsBtn)
        self.menuSettings.addAction(self.resetIpsBtn)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.menuFontSize.menuAction())
        self.menuSettings.addAction(self.bgColorBtn)
        self.menuSettings.addAction(self.defaultBgBtn)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.startServerBtn)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.exitBtn)
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.ipInput.returnPressed.connect(self.msgInput.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
